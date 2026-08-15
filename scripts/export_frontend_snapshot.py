"""Export a public, synthetic-only control-room snapshot for the frontend."""

from __future__ import annotations

from dataclasses import asdict
from datetime import UTC, datetime
import json
from pathlib import Path

from rei.pipeline import load_synthetic_fixture, run_synthetic_pipeline
from rei.policy import load_source_policies


def build_public_snapshot(repository_root: Path) -> dict[str, object]:
    policies = load_source_policies(repository_root / "config/source-policies.json")
    fixture_path = repository_root / "data/fixtures/sacramento_assessment_synthetic.json"
    report = run_synthetic_pipeline(load_synthetic_fixture(fixture_path))

    return {
        "schema_version": 1,
        "environment": "synthetic",
        "generated_at": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        "notice": report.fixture_notice,
        "sources": [
            policies[source_id].public_status() for source_id in sorted(policies)
        ],
        "latest_run": {
            "transformation_version": report.transformation_version,
            "input_sha256": report.input_sha256,
            "input_count": report.input_count,
            "accepted_count": report.accepted_count,
            "review_count": report.review_count,
            "rejected_count": report.rejected_count,
            "reconciliation_passed": report.reconciliation_passed,
            "issue_counts": report.issue_counts,
            "records": [asdict(record) for record in report.records],
        },
    }


def main() -> None:
    repository_root = Path(__file__).resolve().parents[1]
    output = repository_root / "frontend/data/control-room.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(build_public_snapshot(repository_root), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote public frontend snapshot: {output.relative_to(repository_root)}")


if __name__ == "__main__":
    main()
