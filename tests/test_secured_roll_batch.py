from pathlib import Path
import json
import unittest


class SacramentoSecuredRollBatchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = json.loads(
            Path("frontend/data/sacramento-secured-roll-batch.json").read_text(
                encoding="utf-8"
            )
        )

    def test_batch_is_quarantined_and_metadata_only(self) -> None:
        self.assertEqual(self.payload["connection_status"], "quarantined_metadata_only")
        self.assertFalse(self.payload["safety"]["row_values_exported"])
        self.assertFalse(self.payload["safety"]["real_data_processing_enabled"])
        self.assertNotIn("/Volumes/", json.dumps(self.payload))

    def test_structural_counts_reconcile(self) -> None:
        workbook = self.payload["workbook"]
        self.assertEqual(workbook["record_count"] + 1, workbook["row_count_including_header"])
        self.assertEqual(workbook["field_count"], 30)
        review = self.payload["field_review"]
        self.assertEqual(
            review["provisional_candidate_count"]
            + review["prohibited_count"]
            + review["unresolved_count"],
            workbook["field_count"],
        )

    def test_prohibited_fields_are_detected_without_values(self) -> None:
        review = self.payload["field_review"]
        self.assertEqual(review["prohibited_count"], 6)
        self.assertIn("OWNER", review["prohibited_headers"])
        self.assertIn("MAIL_ADDRESS", review["prohibited_headers"])
        self.assertEqual(len(review["schema_discrepancies"]), 1)


if __name__ == "__main__":
    unittest.main()
