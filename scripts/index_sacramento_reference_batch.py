"""Index Sacramento Assessor reference files without copying the source documents."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
from xml.etree import ElementTree
from zipfile import ZipFile


PDF_NAME = "36-11_B_Land Use Code Tables (JG-2023r) (SH-2023) (ES)(2).pdf"
XLSX_NAME = "36-11_CX_Land Use Code Quick Reference.xlsx"
REFERENCE_SUBPATH = Path(
    "reference/california/sacramento/assessor/land-use-codes"
)
CELL_REFERENCE = re.compile(r"([A-Z]+)([0-9]+)")
GENERAL_FAMILY = re.compile(r"^[A-Z]x{5}$")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pdf_page_count(path: Path) -> int:
    payload = path.read_bytes()
    return len(re.findall(rb"/Type\s*/Page(?!s)\b", payload))


def _xlsx_strings(archive: ZipFile) -> list[str]:
    namespace = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    try:
        root = ElementTree.fromstring(archive.read("xl/sharedStrings.xml"))
    except KeyError:
        return []
    return [
        "".join(node.text or "" for node in item.findall(".//m:t", namespace))
        for item in root.findall("m:si", namespace)
    ]


def _xlsx_sheets(archive: ZipFile) -> list[tuple[str, str]]:
    main = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
    relationships = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    package = "http://schemas.openxmlformats.org/package/2006/relationships"
    workbook = ElementTree.fromstring(archive.read("xl/workbook.xml"))
    rels = ElementTree.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
    targets = {
        item.attrib["Id"]: item.attrib["Target"]
        for item in rels.findall(f"{{{package}}}Relationship")
    }
    return [
        (
            sheet.attrib["name"],
            "xl/" + targets[sheet.attrib[f"{{{relationships}}}id"]].lstrip("/"),
        )
        for sheet in workbook.findall(f".//{{{main}}}sheet")
    ]


def _worksheet_cells(
    archive: ZipFile, path: str, shared_strings: list[str]
) -> dict[str, str]:
    namespace = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
    root = ElementTree.fromstring(archive.read(path))
    cells: dict[str, str] = {}
    for cell in root.findall(f".//{{{namespace}}}c"):
        reference = cell.attrib.get("r")
        if not reference:
            continue
        value = cell.find(f"{{{namespace}}}v")
        if value is None or value.text is None:
            continue
        text = value.text
        if cell.attrib.get("t") == "s":
            text = shared_strings[int(text)]
        cells[reference] = text.strip()
    return cells


def workbook_summary(path: Path) -> dict[str, object]:
    with ZipFile(path) as archive:
        shared_strings = _xlsx_strings(archive)
        sheets = _xlsx_sheets(archive)
        first_cells = _worksheet_cells(archive, sheets[0][1], shared_strings)

    rows = [
        int(match.group(2))
        for reference in first_cells
        if (match := CELL_REFERENCE.fullmatch(reference))
    ]
    families = []
    for row in range(1, max(rows, default=0) + 1):
        code = first_cells.get(f"G{row}", "")
        description = first_cells.get(f"H{row}", "")
        if GENERAL_FAMILY.fullmatch(code) and description:
            families.append(
                {
                    "code_pattern": code,
                    "description": description.replace("***RETIRED*** ", ""),
                    "status": "retired" if "RETIRED" in description else "active",
                }
            )
    return {
        "sheet_count": len(sheets),
        "sheet_names": [name for name, _ in sheets],
        "quick_reference_rows": max(rows, default=0),
        "families": families,
    }


def build_index(data_root: Path) -> dict[str, object]:
    source_dir = data_root / REFERENCE_SUBPATH
    pdf = source_dir / PDF_NAME
    workbook = source_dir / XLSX_NAME
    for path in (pdf, workbook):
        if not path.is_file():
            raise FileNotFoundError(f"Required reference file not found: {path.name}")

    workbook_data = workbook_summary(workbook)
    return {
        "schema_version": 1,
        "batch_id": "ca-sacramento-assessor-land-use-2023-04",
        "county": "Sacramento",
        "agency": "Office of the Assessor",
        "reference_name": "Land Use Codes",
        "effective_date": "2023-04",
        "connection_status": "reference_ready",
        "safety": {
            "contains_parcel_records": False,
            "contains_owner_or_mailing_fields": False,
            "hosted_exposure": "metadata_and_general_code_families_only",
        },
        "assets": [
            {
                "asset_id": "operations-manual-36-11b",
                "filename": pdf.name,
                "format": "pdf",
                "size_bytes": pdf.stat().st_size,
                "sha256": sha256(pdf),
                "page_count": pdf_page_count(pdf),
            },
            {
                "asset_id": "land-use-quick-reference",
                "filename": workbook.name,
                "format": "xlsx",
                "size_bytes": workbook.stat().st_size,
                "sha256": sha256(workbook),
                "sheet_count": workbook_data["sheet_count"],
                "sheet_names": workbook_data["sheet_names"],
                "quick_reference_rows": workbook_data["quick_reference_rows"],
            },
        ],
        "general_code_families": workbook_data["families"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_root", type=Path)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("frontend/data/sacramento-land-use-reference.json"),
    )
    args = parser.parse_args()
    result = build_index(args.data_root.expanduser().resolve(strict=True))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"Indexed {len(result['assets'])} reference assets")


if __name__ == "__main__":
    main()
