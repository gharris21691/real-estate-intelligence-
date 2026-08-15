"""Runtime configuration with explicit external-data safety checks."""

from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path


class ConfigurationError(ValueError):
    """Raised when a runtime path violates the project's data boundaries."""


@dataclass(frozen=True)
class Settings:
    repository_root: Path
    data_root: Path
    database_path: Path

    @classmethod
    def from_environment(
        cls,
        *,
        repository_root: Path | None = None,
        environ: dict[str, str] | None = None,
    ) -> "Settings":
        values = os.environ if environ is None else environ
        repo = (repository_root or Path.cwd()).resolve()

        raw_data_root = values.get("REI_DATA_ROOT")
        if not raw_data_root:
            raise ConfigurationError("REI_DATA_ROOT must point to the external data directory")

        data_root = Path(raw_data_root).expanduser().resolve()
        database_path = Path(
            values.get("REI_DATABASE_PATH", str(repo / "data/local/rei_metadata.sqlite"))
        ).expanduser().resolve()

        if _is_within(data_root, repo):
            raise ConfigurationError("REI_DATA_ROOT must be outside the Git repository")
        if data_root == Path(data_root.anchor):
            raise ConfigurationError("REI_DATA_ROOT cannot be a filesystem root")

        return cls(repo, data_root, database_path)

    def require_data_root(self) -> Path:
        if not self.data_root.is_dir():
            raise ConfigurationError(f"External data directory is unavailable: {self.data_root}")
        return self.data_root


def _is_within(candidate: Path, parent: Path) -> bool:
    try:
        candidate.relative_to(parent)
    except ValueError:
        return False
    return True
