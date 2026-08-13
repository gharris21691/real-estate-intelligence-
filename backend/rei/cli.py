"""Local commands for safe project setup and source metadata."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .config import ConfigurationError, Settings
from .database import initialize_database
from .manifest import build_manifest
from .pipeline import load_synthetic_fixture, run_synthetic_pipeline
from .policy import PolicyError, load_source_policies, require_source_approved


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

    synthetic = commands.add_parser(
        "validate-synthetic", help="validate an explicitly synthetic fixture"
    )
    synthetic.add_argument("path", type=Path)
    synthetic.add_argument("--output", type=Path)
    synthetic.add_argument(
        "--policy-file", type=Path, default=Path("config/source-policies.json")
    )
    synthetic.set_defaults(handler=_validate_synthetic)

    status = commands.add_parser("source-status", help="show machine-enforced source status")
    status.add_argument("--source-id")
    status.add_argument(
        "--policy-file", type=Path, default=Path("config/source-policies.json")
    )
    status.set_defaults(handler=_source_status)
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


def _validate_synthetic(args: argparse.Namespace) -> int:
    policies = load_source_policies(args.policy_file.expanduser().resolve(strict=True))
    synthetic_policy = policies.get("synthetic_sacramento_assessment_fixture")
    if synthetic_policy is None:
        raise PolicyError("Synthetic Sacramento source policy is missing")
    require_source_approved(synthetic_policy)

    repository_root = Path.cwd().resolve()
    fixture_root = repository_root / "data/fixtures"
    fixture = args.path.expanduser().resolve(strict=True)
    try:
        fixture.relative_to(fixture_root)
    except ValueError as error:
        raise ConfigurationError("Synthetic fixtures must be inside data/fixtures") from error

    report = run_synthetic_pipeline(load_synthetic_fixture(fixture))
    if args.output:
        output = args.output.expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(report.to_json(), encoding="utf-8")
        print(f"Wrote synthetic quality report: {output}")
    else:
        print(report.to_json(), end="")
    return 0 if report.reconciliation_passed and report.rejected_count == 0 else 1


def _source_status(args: argparse.Namespace) -> int:
    policies = load_source_policies(args.policy_file.expanduser().resolve(strict=True))
    if args.source_id:
        if args.source_id not in policies:
            raise PolicyError(f"Unknown source policy id: {args.source_id}")
        selected = [policies[args.source_id]]
    else:
        selected = [policies[source_id] for source_id in sorted(policies)]
    print(
        json.dumps(
            {"version": 1, "sources": [policy.public_status() for policy in selected]},
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        return args.handler(args)
    except (ConfigurationError, FileNotFoundError, ValueError, OSError, PolicyError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
