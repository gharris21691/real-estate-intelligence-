"""Persist and summarize policy-approved synthetic pilot runs."""

from __future__ import annotations

from contextlib import closing
import json
from pathlib import Path
import sqlite3
from uuid import NAMESPACE_URL, uuid4, uuid5

from .database import initialize_database
from .manifest import sha256_file
from .pipeline import QualityReport, fingerprint_payload
from .policy import SourcePolicy, require_source_approved
from .privacy import enforce_field_policy

SYNTHETIC_SOURCE_ID = "synthetic_sacramento_assessment_fixture"
SACRAMENTO_FIPS = "067"


def persist_synthetic_run(
    database_path: Path,
    fixture_path: Path,
    payload: dict[str, object],
    report: QualityReport,
    policy: SourcePolicy,
) -> str:
    require_source_approved(policy)
    if policy.source_id != SYNTHETIC_SOURCE_ID or policy.data_class != "synthetic":
        raise ValueError("Only the approved synthetic Sacramento source can use this writer")
    if not report.reconciliation_passed:
        raise ValueError("Cannot persist an unreconciled run")
    if report.input_sha256 != fingerprint_payload(payload):
        raise ValueError("Quality report does not match the supplied synthetic payload")

    initialize_database(database_path)
    run_id = str(uuid4())
    artifact_sha256 = sha256_file(fixture_path)
    artifact_id = str(uuid5(NAMESPACE_URL, f"{policy.source_id}:{artifact_sha256}"))
    observed_at = report.generated_at
    records = payload["records"]
    if not isinstance(records, list):
        raise ValueError("Synthetic payload records must be a list")

    with closing(sqlite3.connect(database_path)) as connection, connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute(
            """
            INSERT INTO source_definition (
                source_id, jurisdiction, agency, source_name, approval_status,
                allowed_fields_json, prohibited_fields_json
            ) VALUES (?, ?, ?, ?, 'approved_for_pilot', ?, ?)
            ON CONFLICT(source_id) DO UPDATE SET
                jurisdiction = excluded.jurisdiction,
                agency = excluded.agency,
                source_name = excluded.source_name,
                approval_status = excluded.approval_status,
                allowed_fields_json = excluded.allowed_fields_json,
                prohibited_fields_json = excluded.prohibited_fields_json,
                updated_at = CURRENT_TIMESTAMP
            """,
            (
                policy.source_id,
                policy.county,
                "Synthetic test fixture",
                policy.source_name,
                json.dumps(policy.allowed_fields),
                json.dumps(policy.prohibited_fields),
            ),
        )
        connection.execute(
            """
            INSERT INTO acquisition_run (
                run_id, source_id, started_at, completed_at, status,
                transformation_version, accepted_count, rejected_count, review_count
            ) VALUES (?, ?, ?, ?, 'succeeded', ?, ?, ?, ?)
            """,
            (
                run_id,
                policy.source_id,
                observed_at,
                observed_at,
                report.transformation_version,
                report.accepted_count,
                report.rejected_count,
                report.review_count,
            ),
        )
        connection.execute(
            """
            INSERT OR IGNORE INTO source_artifact (
                artifact_id, run_id, source_id, file_name, external_uri, byte_size,
                sha256, observed_at, classification
            ) VALUES (?, NULL, ?, ?, ?, ?, ?, ?, 'synthetic-test-fixture')
            """,
            (
                artifact_id,
                policy.source_id,
                fixture_path.name,
                f"data/fixtures/{fixture_path.name}",
                fixture_path.stat().st_size,
                artifact_sha256,
                observed_at,
            ),
        )

        for result in report.records:
            source_record_key = f"synthetic:{result.record_index}"
            observation_id: str | None = None
            if result.status in {"accepted", "review"}:
                raw_record = records[result.record_index]
                if not isinstance(raw_record, dict):
                    raise ValueError("Synthetic record must be an object")
                filtered = enforce_field_policy(
                    raw_record,
                    allowed_fields=set(policy.allowed_fields),
                    prohibited_fields=set(policy.prohibited_fields),
                )
                values = filtered.values
                observation_id = str(
                    uuid5(NAMESPACE_URL, f"{run_id}:{source_record_key}")
                )
                connection.execute(
                    """
                    INSERT INTO parcel_observation (
                        observation_id, run_id, source_artifact_id, jurisdiction_fips,
                        source_apn, roll_year, situs_address_raw, assessed_land_value,
                        assessed_improvement_value, total_assessed_value, exemption_value,
                        tax_rate_area_code, assessor_land_use_code, recorder_book_page,
                        source_record_key, transformation_version, validation_status, observed_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        observation_id,
                        run_id,
                        artifact_id,
                        SACRAMENTO_FIPS,
                        values["source_apn"],
                        values["roll_year"],
                        values.get("situs_address_raw"),
                        _text(values.get("assessed_land_value")),
                        _text(values.get("assessed_improvement_value")),
                        _text(values.get("total_assessed_value")),
                        _text(values.get("exemption_value")),
                        values.get("tax_rate_area_code"),
                        values.get("assessor_land_use_code"),
                        values.get("recorder_book_page"),
                        source_record_key,
                        report.transformation_version,
                        result.status,
                        observed_at,
                    ),
                )

            for issue_code in result.issue_codes:
                issue_id = str(
                    uuid5(NAMESPACE_URL, f"{run_id}:{source_record_key}:{issue_code}")
                )
                connection.execute(
                    """
                    INSERT INTO validation_issue (
                        issue_id, run_id, observation_id, source_record_key, issue_code
                    ) VALUES (?, ?, ?, ?, ?)
                    """,
                    (issue_id, run_id, observation_id, source_record_key, issue_code),
                )
    return run_id


def audit_summary(database_path: Path, *, limit: int = 10) -> dict[str, object]:
    initialize_database(database_path)
    with closing(sqlite3.connect(database_path)) as connection:
        connection.row_factory = sqlite3.Row
        totals = connection.execute(
            """
            SELECT
                COUNT(*) AS run_count,
                COALESCE(SUM(accepted_count), 0) AS accepted_count,
                COALESCE(SUM(review_count), 0) AS review_count,
                COALESCE(SUM(rejected_count), 0) AS rejected_count
            FROM acquisition_run
            """
        ).fetchone()
        latest = connection.execute(
            """
            SELECT run_id, source_id, started_at, completed_at, status,
                   transformation_version, accepted_count, review_count, rejected_count
            FROM acquisition_run
            ORDER BY started_at DESC, run_id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        artifact_count = connection.execute(
            "SELECT COUNT(*) FROM source_artifact"
        ).fetchone()[0]
        observation_count = connection.execute(
            "SELECT COUNT(*) FROM parcel_observation"
        ).fetchone()[0]
        issue_count = connection.execute(
            "SELECT COUNT(*) FROM validation_issue"
        ).fetchone()[0]
    return {
        "version": 1,
        "totals": dict(totals),
        "artifact_count": artifact_count,
        "observation_count": observation_count,
        "issue_count": issue_count,
        "latest_runs": [dict(row) for row in latest],
    }


def _text(value: object) -> str | None:
    return None if value is None else str(value)
