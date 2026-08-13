"""Machine-enforced source approval policies."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Mapping

REQUIRED_GATES = ("access", "terms", "privacy", "data", "operations")


class PolicyError(ValueError):
    """Raised when a source policy is invalid or cannot authorize execution."""


class SourceNotApprovedError(PolicyError):
    """Raised when a source is disabled or has incomplete approval gates."""


@dataclass(frozen=True)
class SourcePolicy:
    source_id: str
    county: str
    source_name: str
    data_class: str
    approval_status: str
    enabled: bool
    gates: dict[str, bool]
    allowed_fields: tuple[str, ...]
    prohibited_fields: tuple[str, ...]
    hold_reasons: tuple[str, ...]

    @property
    def executable(self) -> bool:
        if not self.enabled or not all(self.gates.get(gate, False) for gate in REQUIRED_GATES):
            return False
        if self.data_class == "synthetic":
            return self.approval_status == "synthetic_only"
        return self.approval_status == "approved_for_pilot"

    def public_status(self) -> dict[str, object]:
        return {
            "id": self.source_id,
            "county": self.county,
            "source_name": self.source_name,
            "data_class": self.data_class,
            "approval_status": self.approval_status,
            "enabled": self.enabled,
            "executable": self.executable,
            "gates": self.gates,
            "allowed_field_count": len(self.allowed_fields),
            "prohibited_field_count": len(self.prohibited_fields),
            "hold_reasons": list(self.hold_reasons),
        }


def load_source_policies(path: Path) -> dict[str, SourcePolicy]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping) or payload.get("version") != 1:
        raise PolicyError("Source policy file must be a version 1 JSON object")
    sources = payload.get("sources")
    if not isinstance(sources, list):
        raise PolicyError("Source policy file must contain a sources array")

    policies: dict[str, SourcePolicy] = {}
    for raw in sources:
        policy = _parse_source_policy(raw)
        if policy.source_id in policies:
            raise PolicyError(f"Duplicate source policy id: {policy.source_id}")
        policies[policy.source_id] = policy
    return policies


def require_source_approved(policy: SourcePolicy) -> SourcePolicy:
    if policy.executable:
        return policy
    incomplete = [gate for gate in REQUIRED_GATES if not policy.gates.get(gate, False)]
    reasons = "; ".join(policy.hold_reasons) or "source is not approved"
    gate_text = ", ".join(incomplete) or "approval status"
    raise SourceNotApprovedError(
        f"Source {policy.source_id} is blocked by {gate_text}: {reasons}"
    )


def _parse_source_policy(raw: object) -> SourcePolicy:
    if not isinstance(raw, Mapping):
        raise PolicyError("Each source policy must be an object")
    required_text = ("id", "county", "source_name", "data_class", "approval_status")
    missing = [field for field in required_text if not isinstance(raw.get(field), str)]
    if missing:
        raise PolicyError("Source policy has missing text fields: " + ", ".join(missing))
    if raw["data_class"] not in {"synthetic", "real"}:
        raise PolicyError(f"Invalid data_class for source {raw['id']}")
    if not isinstance(raw.get("enabled"), bool):
        raise PolicyError(f"Source {raw['id']} enabled must be boolean")

    gates = raw.get("gates")
    if not isinstance(gates, Mapping) or any(
        not isinstance(gates.get(gate), bool) for gate in REQUIRED_GATES
    ):
        raise PolicyError(f"Source {raw['id']} must define every boolean approval gate")

    allowed = _string_tuple(raw.get("allowed_fields"), "allowed_fields", str(raw["id"]))
    prohibited = _string_tuple(
        raw.get("prohibited_fields"), "prohibited_fields", str(raw["id"])
    )
    hold_reasons = _string_tuple(raw.get("hold_reasons"), "hold_reasons", str(raw["id"]))
    overlap = {field.casefold() for field in allowed} & {
        field.casefold() for field in prohibited
    }
    if overlap:
        raise PolicyError(f"Source {raw['id']} has fields both allowed and prohibited")

    return SourcePolicy(
        source_id=str(raw["id"]),
        county=str(raw["county"]),
        source_name=str(raw["source_name"]),
        data_class=str(raw["data_class"]),
        approval_status=str(raw["approval_status"]),
        enabled=bool(raw["enabled"]),
        gates={gate: bool(gates[gate]) for gate in REQUIRED_GATES},
        allowed_fields=allowed,
        prohibited_fields=prohibited,
        hold_reasons=hold_reasons,
    )


def _string_tuple(value: object, field: str, source_id: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise PolicyError(f"Source {source_id} {field} must be a string array")
    return tuple(value)
