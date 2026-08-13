from datetime import UTC, datetime
from pathlib import Path
import tempfile
import unittest

from rei.manifest import build_manifest, sha256_file


class ManifestTests(unittest.TestCase):
    def test_hashes_without_storing_full_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "synthetic.txt"
            source.write_bytes(b"synthetic source\n")
            manifest = build_manifest(
                source,
                source_id="test_source",
                jurisdiction="Test County",
                observed_at=datetime(2026, 8, 13, tzinfo=UTC),
            )
            self.assertEqual(manifest.source_file_name, "synthetic.txt")
            self.assertNotIn(directory, manifest.to_json())
            self.assertEqual(manifest.sha256, sha256_file(source))
            self.assertEqual(manifest.observed_at, "2026-08-13T00:00:00Z")


if __name__ == "__main__":
    unittest.main()
