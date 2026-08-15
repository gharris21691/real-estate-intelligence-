"""Create non-sensitive metadata manifests without changing source files."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import UTC, datetime
import hashlib
import json
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class SourceManifest:
    schema_version: int
    source_id: str
    jurisdiction: str
    source_file_name: str
    byte_size: int
    sha256: str
    observed_at: str
    effective_date: str | None
    classification: str
    approved_fields: tuple[str, ...]
    contains_personal_data: bool | None

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, sort_keys=True) + "\n"


def sha256_file(path: Path, *, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def build_manifest(
    path: Path,
    *,
    source_id: str,
    jurisdiction: str,
    effective_date: str | None = None,
    approved_fields: Iterable[str] = (),
    contains_personal_data: bool | None = None,
    observed_at: datetime | None = None,
) -> SourceManifest:
    resolved = path.expanduser().resolve(strict=True)
    if not resolved.is_file():
        raise ValueError(f"Source artifact is not a file: {resolved}")

    timestamp = (observed_at or datetime.now(UTC)).astimezone(UTC)
    return SourceManifest(
        schema_version=1,
        source_id=source_id,
        jurisdiction=jurisdiction,
        source_file_name=resolved.name,
        byte_size=resolved.stat().st_size,
        sha256=sha256_file(resolved),
        observed_at=timestamp.isoformat().replace("+00:00", "Z"),
        effective_date=effective_date,
        classification="restricted-source-metadata",
        approved_fields=tuple(sorted(set(approved_fields))),
        contains_personal_data=contains_personal_data,
    )
