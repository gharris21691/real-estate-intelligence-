from pathlib import Path
from contextlib import closing
import sqlite3
import tempfile
import unittest

from rei.database import initialize_database


class DatabaseTests(unittest.TestCase):
    def test_initialization_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "metadata.sqlite"
            initialize_database(database)
            initialize_database(database)
            with closing(sqlite3.connect(database)) as connection:
                tables = {
                    row[0]
                    for row in connection.execute(
                        "SELECT name FROM sqlite_master WHERE type = 'table'"
                    )
                }
                version = connection.execute(
                    "SELECT version FROM schema_migration"
                ).fetchone()
            self.assertTrue(
                {
                    "source_definition",
                    "acquisition_run",
                    "source_artifact",
                    "parcel_observation",
                    "validation_issue",
                }.issubset(tables)
            )
            self.assertEqual(version, (1,))


if __name__ == "__main__":
    unittest.main()
