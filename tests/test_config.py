from pathlib import Path
import tempfile
import unittest

from rei.config import ConfigurationError, Settings


class SettingsTests(unittest.TestCase):
    def test_accepts_external_data_root(self) -> None:
        with tempfile.TemporaryDirectory() as repo_dir, tempfile.TemporaryDirectory() as data_dir:
            settings = Settings.from_environment(
                repository_root=Path(repo_dir),
                environ={"REI_DATA_ROOT": data_dir},
            )
            self.assertEqual(settings.data_root, Path(data_dir).resolve())

    def test_rejects_data_root_inside_repository(self) -> None:
        with tempfile.TemporaryDirectory() as repo_dir:
            repo = Path(repo_dir)
            with self.assertRaises(ConfigurationError):
                Settings.from_environment(
                    repository_root=repo,
                    environ={"REI_DATA_ROOT": str(repo / "data/raw")},
                )

    def test_requires_data_root_setting(self) -> None:
        with self.assertRaises(ConfigurationError):
            Settings.from_environment(repository_root=Path.cwd(), environ={})


if __name__ == "__main__":
    unittest.main()
