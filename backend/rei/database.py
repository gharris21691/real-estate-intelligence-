"""SQLite metadata database initialization."""

from __future__ import annotations

from importlib.resources import files
from pathlib import Path
import sqlite3


def initialize_database(path: Path) -> None:
    resolved = path.expanduser().resolve()
    resolved.parent.mkdir(parents=True, exist_ok=True)
    migration = files("rei").joinpath("migrations/0001_foundation.sql").read_text(encoding="utf-8")
    with sqlite3.connect(resolved) as connection:
        connection.executescript(migration)
