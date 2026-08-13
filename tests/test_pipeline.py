from datetime import UTC, datetime
import json
from pathlib import Path
import tempfile
import unittest

from rei.pipeline import (
    SYNTHETIC_NOTICE,
    SyntheticFixtureError,
    load_synthetic_fixture,
    run_synthetic_pipeline,
)


class SyntheticPipelineTests(unittest.TestCase):
    def test_repository_fixture_reconciles(self) -> None:
        payload = load_synthetic_fixture(
            Path("data/fixtures/sacramento_assessment_synthetic.json")
        )
        report = run_synthetic_pipeline(
            payload, generated_at=datetime(2026, 8, 13, tzinfo=UTC)
        )
        self.assertEqual(report.input_count, 2)
        self.assertEqual(report.accepted_count, 2)
        self.assertEqual(report.review_count, 0)
        self.assertEqual(report.rejected_count, 0)
        self.assertTrue(report.reconciliation_passed)
        self.assertEqual(report.transformation_version, "sacramento-synthetic-v1")
        self.assertEqual(len(report.input_sha256), 64)

        repeated = run_synthetic_pipeline(
            payload, generated_at=datetime(2026, 8, 14, tzinfo=UTC)
        )
        self.assertEqual(report.input_sha256, repeated.input_sha256)
        self.assertEqual(report.records, repeated.records)

    def test_refuses_unmarked_input(self) -> None:
        with self.assertRaises(SyntheticFixtureError):
            run_synthetic_pipeline({"records": []})

    def test_rejects_prohibited_fields_without_echoing_values(self) -> None:
        sensitive_value = "Example Owner"
        report = run_synthetic_pipeline(
            {
                "fixture_notice": SYNTHETIC_NOTICE,
                "records": [
                    {
                        "source_apn": "000-0000-003-0000",
                        "roll_year": 2026,
                        "owner_name": sensitive_value,
                    }
                ],
            }
        )
        self.assertEqual(report.rejected_count, 1)
        self.assertEqual(report.issue_counts, {"prohibited_field": 1})
        self.assertNotIn(sensitive_value, report.to_json())

    def test_routes_duplicates_and_unknown_fields_to_review(self) -> None:
        report = run_synthetic_pipeline(
            {
                "fixture_notice": SYNTHETIC_NOTICE,
                "records": [
                    {"source_apn": "DUPLICATE", "roll_year": 2026},
                    {
                        "source_apn": "DUPLICATE",
                        "roll_year": 2026,
                        "unapproved_note": "synthetic",
                    },
                ],
            }
        )
        self.assertEqual(report.review_count, 2)
        self.assertEqual(report.issue_counts["duplicate_apn"], 2)
        self.assertEqual(report.issue_counts["unapproved_field_omitted"], 1)

    def test_loader_requires_object_records(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / "bad.json"
            fixture.write_text(
                json.dumps({"fixture_notice": SYNTHETIC_NOTICE, "records": ["bad"]}),
                encoding="utf-8",
            )
            with self.assertRaises(SyntheticFixtureError):
                load_synthetic_fixture(fixture)


if __name__ == "__main__":
    unittest.main()
