from datetime import UTC, datetime
from contextlib import closing
from pathlib import Path
import sqlite3
import tempfile
import unittest

from rei.audit import audit_summary, persist_synthetic_run
from rei.pipeline import load_synthetic_fixture, run_synthetic_pipeline
from rei.policy import load_source_policies


class SyntheticAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = Path("data/fixtures/sacramento_assessment_synthetic.json").resolve()
        self.payload = load_synthetic_fixture(self.fixture)
        self.policy = load_source_policies(Path("config/source-policies.json"))[
            "synthetic_sacramento_assessment_fixture"
        ]

    def test_persists_reconciled_run_and_reuses_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "audit.sqlite"
            report = run_synthetic_pipeline(
                self.payload, generated_at=datetime(2026, 8, 13, tzinfo=UTC)
            )
            first_run = persist_synthetic_run(
                database, self.fixture, self.payload, report, self.policy
            )
            second_run = persist_synthetic_run(
                database, self.fixture, self.payload, report, self.policy
            )
            summary = audit_summary(database)

            self.assertNotEqual(first_run, second_run)
            self.assertEqual(summary["totals"]["run_count"], 2)
            self.assertEqual(summary["totals"]["accepted_count"], 4)
            self.assertEqual(summary["artifact_count"], 1)
            self.assertEqual(summary["observation_count"], 4)
            self.assertEqual(summary["issue_count"], 0)

            with closing(sqlite3.connect(database)) as connection:
                artifact = connection.execute(
                    "SELECT external_uri, file_name FROM source_artifact"
                ).fetchone()
                source = connection.execute(
                    "SELECT approval_status FROM source_definition"
                ).fetchone()
            self.assertEqual(
                artifact[0], "data/fixtures/sacramento_assessment_synthetic.json"
            )
            self.assertNotIn(str(self.fixture.parent.parent.parent), artifact[0])
            self.assertEqual(source, ("approved_for_pilot",))

    def test_persists_non_sensitive_issue_codes(self) -> None:
        payload = {
            "fixture_notice": self.payload["fixture_notice"],
            "records": [
                {
                    "source_apn": "000-0000-004-0000",
                    "roll_year": 2026,
                    "unapproved_note": "synthetic only",
                }
            ],
        }
        report = run_synthetic_pipeline(
            payload, generated_at=datetime(2026, 8, 13, tzinfo=UTC)
        )
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "audit.sqlite"
            persist_synthetic_run(database, self.fixture, payload, report, self.policy)
            with closing(sqlite3.connect(database)) as connection:
                issue = connection.execute(
                    "SELECT issue_code, non_sensitive_detail FROM validation_issue"
                ).fetchone()
        self.assertEqual(issue, ("unapproved_field_omitted", None))

    def test_refuses_mismatched_report_and_payload(self) -> None:
        report = run_synthetic_pipeline(
            self.payload, generated_at=datetime(2026, 8, 13, tzinfo=UTC)
        )
        changed = dict(self.payload)
        changed["records"] = []
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "does not match"):
                persist_synthetic_run(
                    Path(directory) / "audit.sqlite",
                    self.fixture,
                    changed,
                    report,
                    self.policy,
                )


if __name__ == "__main__":
    unittest.main()
