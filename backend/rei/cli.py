"""Local commands for safe project setup and source metadata."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from .config import ConfigurationError, Settings
from .database import initialize_database
from .manifest import build_manifest


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="rei")
    commands = root.add_subparsers(dest="command", required=True)

    check = commands.add_parser("check-config", help="validate external data configuration")
    check.set_defaults(handler=_check_config)

    database = commands.add_parser("init-db", help="initialize the local metadata database")
    database.set_defaults(handler=_init_db)

    manifest = commands.add_parser("manifest", help="print a metadata-only file manifest")
    manifest.add_argument("path", type=Path)
    manifest.add_argument("--source-id", required=True)
    manifest.add_argument("--jurisdiction", required=True)
    manifest.add_argument("--effective-date")
    manifest.set_defaults(handler=_manifest)
    return root


def _check_config(_: argparse.Namespace) -> int:
    settings = Settings.from_environment()
    settings.require_data_root()
    print(f"External data directory available: {settings.data_root}")
    print(f"Metadata database path: {settings.database_path}")
    return 0


def _init_db(_: argparse.Namespace) -> int:
    settings = Settings.from_environment()
    initialize_database(settings.database_path)
    print(f"Initialized metadata database: {settings.database_path}")
    return 0


def _manifest(args: argparse.Namespace) -> int:
    settings = Settings.from_environment()
    data_root = settings.require_data_root()
    artifact = args.path.expanduser().resolve(strict=True)
    try:
        artifact.relative_to(data_root)
    except ValueError as error:
        raise ConfigurationError("Manifest source must be inside REI_DATA_ROOT") from error
    result = build_manifest(
        artifact,
        source_id=args.source_id,
        jurisdiction=args.jurisdiction,
        effective_date=args.effective_date,
    )
    print(result.to_json(), end="")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        return args.handler(args)
    except (ConfigurationError, FileNotFoundError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
