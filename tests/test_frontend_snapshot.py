from pathlib import Path
import unittest

from scripts.export_frontend_snapshot import build_public_snapshot


class FrontendSnapshotTests(unittest.TestCase):
    def setUp(self) -> None:
        self.snapshot = build_public_snapshot(Path.cwd())

    def test_snapshot_is_synthetic_and_reconciled(self) -> None:
        self.assertEqual(self.snapshot["environment"], "synthetic")
        run = self.snapshot["latest_run"]
        self.assertTrue(run["reconciliation_passed"])
        self.assertEqual(
            run["input_count"],
            run["accepted_count"] + run["review_count"] + run["rejected_count"],
        )

    def test_snapshot_exposes_only_public_policy_status(self) -> None:
        for source in self.snapshot["sources"]:
            self.assertNotIn("allowed_fields", source)
            self.assertNotIn("prohibited_fields", source)
        self.assertNotIn("source_apn", str(self.snapshot).casefold())
        self.assertNotIn("owner_name", str(self.snapshot).casefold())

    def test_only_synthetic_source_is_executable(self) -> None:
        executable = [source for source in self.snapshot["sources"] if source["executable"]]
        self.assertEqual(len(executable), 1)
        self.assertEqual(executable[0]["data_class"], "synthetic")


if __name__ == "__main__":
    unittest.main()
