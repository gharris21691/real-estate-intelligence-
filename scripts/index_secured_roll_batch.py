"""Create a metadata-only intake record for a Sacramento secured-roll ZIP."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
from xml.etree import ElementTree
from zipfile import ZipFile


MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PACKAGE_REL = "http://schemas.openxmlformats.org/package/2006/relationships"
CELL_ROW = re.compile(r"^[A-Z]+(\d+)$")
RANGE = re.compile(r"^[A-Z]+(\d+):([A-Z]+)(\d+)$")

PROHIBITED_HEADERS = {
    "OWNER",
    "MAIL_ADDRESS",
    "MAIL_CITY",
    "MAIL_STATE",
    "MAIL_ZIP",
    "CARE_OF",
}
PROVISIONAL_CANDIDATE_HEADERS = {
    "MAPB",
    "PG",
    "PCL",
    "PSUB",
    "TAX_RATE_AREA",
    "SITUS_NUMBER",
    "SITUS_CITY",
    "SITUS_STREET",
    "SITUS_ZIP",
    "LAND_USE_CODE",
    "RECORDING_PAGE",
    "LAND",
    "IM",
    "EX",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _sheet_target(archive: ZipFile) -> tuple[str, str]:
    workbook = ElementTree.fromstring(archive.read("xl/workbook.xml"))
    relationships = ElementTree.fromstring(
        archive.read("xl/_rels/workbook.xml.rels")
    )
    targets = {
        item.attrib["Id"]: item.attrib["Target"]
        for item in relationships.findall(f"{{{PACKAGE_REL}}}Relationship")
    }
    sheet = workbook.find(f".//{{{MAIN}}}sheet")
    if sheet is None:
        raise ValueError("Workbook has no worksheet")
    target = targets[sheet.attrib[f"{{{REL}}}id"]]
    return sheet.attrib["name"], "xl/" + target.lstrip("/")


def _shared_strings(archive: ZipFile, needed: set[int]) -> dict[int, str]:
    found: dict[int, str] = {}
    with archive.open("xl/sharedStrings.xml") as stream:
        index = -1
        for _, element in ElementTree.iterparse(stream, events=("end",)):
            if element.tag != f"{{{MAIN}}}si":
                continue
            index += 1
            if index in needed:
                found[index] = "".join(
                    node.text or "" for node in element.findall(f".//{{{MAIN}}}t")
                )
            element.clear()
            if len(found) == len(needed):
                break
    return found


def workbook_structure(path: Path) -> dict[str, object]:
    with ZipFile(path) as archive:
        sheet_name, sheet_path = _sheet_target(archive)
        dimension = None
        header_refs: list[tuple[str, str]] = []
        with archive.open(sheet_path) as stream:
            for _, element in ElementTree.iterparse(stream, events=("end",)):
                if element.tag == f"{{{MAIN}}}dimension":
                    dimension = element.attrib.get("ref")
                    element.clear()
                elif element.tag == f"{{{MAIN}}}c":
                    reference = element.attrib.get("r", "")
                    match = CELL_ROW.fullmatch(reference)
                    if match and match.group(1) == "1":
                        value = element.find(f"{{{MAIN}}}v")
                        if value is not None and value.text is not None:
                            header_refs.append((element.attrib.get("t", ""), value.text))
                    element.clear()
                elif element.tag == f"{{{MAIN}}}row" and element.attrib.get("r") == "1":
                    break

        needed = {int(value) for kind, value in header_refs if kind == "s"}
        shared = _shared_strings(archive, needed)

    headers = [
        shared.get(int(value), value) if kind == "s" else value
        for kind, value in header_refs
    ]
    range_match = RANGE.fullmatch(dimension or "")
    if not range_match:
        raise ValueError("Workbook used range could not be determined")
    return {
        "sheet_name": sheet_name,
        "used_range": dimension,
        "row_count_including_header": int(range_match.group(3)),
        "record_count": int(range_match.group(3)) - 1,
        "last_column": range_match.group(2),
        "field_count": len(headers),
        "headers": headers,
    }


def build_index(path: Path) -> dict[str, object]:
    with ZipFile(path) as archive:
        members = [item for item in archive.infolist() if not item.is_dir()]
        workbook_member = next(
            (item for item in members if item.filename.lower().endswith(".xlsx")), None
        )
        layout_member = next(
            (item for item in members if item.filename.lower().endswith(".doc")), None
        )
        if workbook_member is None or layout_member is None:
            raise ValueError("Secured-roll ZIP must contain one XLSX and one DOC layout")
        with tempfile.NamedTemporaryFile(suffix=".xlsx") as temporary:
            with archive.open(workbook_member) as source:
                shutil.copyfileobj(source, temporary)
            temporary.flush()
            workbook = workbook_structure(Path(temporary.name))

    headers = set(workbook.pop("headers"))
    prohibited = sorted(headers & PROHIBITED_HEADERS)
    candidates = sorted(headers & PROVISIONAL_CANDIDATE_HEADERS)
    unresolved = sorted(headers - set(prohibited) - set(candidates))
    return {
        "schema_version": 1,
        "batch_id": "ca-sacramento-secured-roll-2026-20260813",
        "county": "Sacramento",
        "agency": "Office of the Assessor",
        "source_name": "2026 Secured Public Roll",
        "retrieved_date": "2026-08-13",
        "roll_year": 2026,
        "connection_status": "quarantined_metadata_only",
        "archive": {
            "filename": path.name,
            "size_bytes": path.stat().st_size,
            "sha256": sha256(path),
            "member_count": len(members),
            "members": [
                {
                    "filename": Path(item.filename).name,
                    "format": Path(item.filename).suffix.lower().lstrip("."),
                    "uncompressed_size_bytes": item.file_size,
                }
                for item in members
            ],
        },
        "workbook": workbook,
        "field_review": {
            "provisional_candidate_count": len(candidates),
            "prohibited_count": len(prohibited),
            "unresolved_count": len(unresolved),
            "prohibited_headers": prohibited,
            "schema_discrepancies": [
                "Layout document lists SITUS_STREET_SUB; workbook supplies SITUS_CITY"
            ],
        },
        "safety": {
            "row_values_exported": False,
            "hosted_exposure": "metadata_and_field_classification_counts_only",
            "real_data_processing_enabled": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("frontend/data/sacramento-secured-roll-batch.json"),
    )
    args = parser.parse_args()
    result = build_index(args.path.expanduser().resolve(strict=True))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        f"Indexed {result['workbook']['record_count']} rows; "
        "real-data processing remains disabled"
    )


if __name__ == "__main__":
    main()
