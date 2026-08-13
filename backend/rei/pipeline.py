"""Synthetic-only pilot pipeline and reconciliation reporting."""

from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
import hashlib
import json
from pathlib import Path
from typing import Mapping, Sequence

from .privacy import (
    ProhibitedFieldError,
    SACRAMENTO_PROHIBITED_FIELDS,
    SACRAMENTO_PROVISIONAL_CANONICAL_FIELDS,
    enforce_field_policy,
)
from .validation import validate_parcel_observation

SYNTHETIC_NOTICE = "Synthetic test data only. These records do not describe real parcels."


class SyntheticFixtureError(ValueError):
    """Raised when input is not explicitly marked as synthetic test data."""


@dataclass(frozen=True)
class RecordResult:
    record_index: int
    status: str
    issue_codes: tuple[str, ...]


@dataclass(frozen=True)
class QualityReport:
    schema_version: int
    transformation_version: str
    fixture_notice: str
    input_sha256: str
    generated_at: str
    input_count: int
    accepted_count: int
    review_count: int
    rejected_count: int
    reconciliation_passed: bool
    issue_counts: dict[str, int]
    records: tuple[RecordResult, ...]

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, sort_keys=True) + "\n"


def load_synthetic_fixture(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise SyntheticFixtureError("Synthetic fixture must be a JSON object")
    if payload.get("fixture_notice") != SYNTHETIC_NOTICE:
        raise SyntheticFixtureError("Input is not explicitly marked as synthetic test data")
    records = payload.get("records")
    if not isinstance(records, list) or not all(isinstance(item, dict) for item in records):
        raise SyntheticFixtureError("Synthetic fixture records must be a JSON object array")
    return payload


def run_synthetic_pipeline(
    payload: Mapping[str, object],
    *,
    generated_at: datetime | None = None,
) -> QualityReport:
    if payload.get("fixture_notice") != SYNTHETIC_NOTICE:
        raise SyntheticFixtureError("Input is not explicitly marked as synthetic test data")
    records = payload.get("records")
    if not isinstance(records, Sequence) or isinstance(records, (str, bytes)):
        raise SyntheticFixtureError("Synthetic fixture records must be a sequence")
    if not all(isinstance(item, Mapping) for item in records):
        raise SyntheticFixtureError("Every synthetic record must be an object")

    apn_counts = Counter(
        item.get("source_apn")
        for item in records
        if isinstance(item.get("source_apn"), str) and item.get("source_apn")
    )
    results: list[RecordResult] = []
    issue_counts: Counter[str] = Counter()

    for index, record in enumerate(records):
        codes: set[str] = set()
        try:
            filtered = enforce_field_policy(
                record,
                allowed_fields=SACRAMENTO_PROVISIONAL_CANONICAL_FIELDS,
                prohibited_fields=SACRAMENTO_PROHIBITED_FIELDS,
            )
        except ProhibitedFieldError:
            codes.add("prohibited_field")
            status = "rejected"
        else:
            issues = validate_parcel_observation(filtered.values)
            codes.update(issue.code for issue in issues)
            if issues:
                status = "rejected"
            else:
                if filtered.omitted_fields:
                    codes.add("unapproved_field_omitted")
                source_apn = filtered.values.get("source_apn")
                if isinstance(source_apn, str) and apn_counts[source_apn] > 1:
                    codes.add("duplicate_apn")
                status = "review" if codes else "accepted"

        issue_counts.update(codes)
        results.append(RecordResult(index, status, tuple(sorted(codes))))

    accepted = sum(result.status == "accepted" for result in results)
    review = sum(result.status == "review" for result in results)
    rejected = sum(result.status == "rejected" for result in results)
    timestamp = (generated_at or datetime.now(UTC)).astimezone(UTC)
    canonical_input = json.dumps(
        payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    return QualityReport(
        schema_version=1,
        transformation_version="sacramento-synthetic-v1",
        fixture_notice=SYNTHETIC_NOTICE,
        input_sha256=hashlib.sha256(canonical_input).hexdigest(),
        generated_at=timestamp.isoformat().replace("+00:00", "Z"),
        input_count=len(results),
        accepted_count=accepted,
        review_count=review,
        rejected_count=rejected,
        reconciliation_passed=len(results) == accepted + review + rejected,
        issue_counts=dict(sorted(issue_counts.items())),
        records=tuple(results),
    )
