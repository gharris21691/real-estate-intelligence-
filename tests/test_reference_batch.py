from pathlib import Path
import json
import unittest


class SacramentoReferenceBatchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = json.loads(
            Path("frontend/data/sacramento-land-use-reference.json").read_text(
                encoding="utf-8"
            )
        )

    def test_reference_batch_has_expected_assets(self) -> None:
        self.assertEqual(self.payload["connection_status"], "reference_ready")
        self.assertEqual(len(self.payload["assets"]), 2)
        self.assertEqual({asset["format"] for asset in self.payload["assets"]}, {"pdf", "xlsx"})

    def test_reference_batch_does_not_expose_external_paths_or_records(self) -> None:
        serialized = json.dumps(self.payload)
        self.assertNotIn("/Volumes/", serialized)
        self.assertFalse(self.payload["safety"]["contains_parcel_records"])
        self.assertFalse(self.payload["safety"]["contains_owner_or_mailing_fields"])

    def test_general_code_families_are_complete(self) -> None:
        families = self.payload["general_code_families"]
        self.assertEqual(len(families), 11)
        self.assertEqual(families[0]["code_pattern"], "Axxxxx")
        self.assertEqual(families[-1]["status"], "retired")
        self.assertTrue(all(len(item["code_pattern"]) == 6 for item in families))


if __name__ == "__main__":
    unittest.main()
