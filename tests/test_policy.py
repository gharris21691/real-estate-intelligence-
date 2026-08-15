from pathlib import Path
import json
import tempfile
import unittest

from rei.policy import (
    PolicyError,
    SourceNotApprovedError,
    load_source_policies,
    require_source_approved,
)


class SourcePolicyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.policies = load_source_policies(Path("config/source-policies.json"))

    def test_only_synthetic_source_is_executable(self) -> None:
        executable = {
            source_id for source_id, policy in self.policies.items() if policy.executable
        }
        self.assertEqual(executable, {"synthetic_sacramento_assessment_fixture"})

    def test_real_sacramento_sources_are_blocked(self) -> None:
        for source_id in (
            "ca_sacramento_assessor_secured_roll",
            "ca_sacramento_gis_active_parcel_base",
        ):
            with self.subTest(source_id=source_id):
                policy = self.policies[source_id]
                self.assertFalse(policy.enabled)
                self.assertEqual(policy.allowed_fields, ())
                with self.assertRaises(SourceNotApprovedError):
                    require_source_approved(policy)

    def test_public_status_does_not_expose_field_names(self) -> None:
        status = self.policies["ca_sacramento_assessor_secured_roll"].public_status()
        self.assertNotIn("allowed_fields", status)
        self.assertNotIn("prohibited_fields", status)
        self.assertGreater(status["prohibited_field_count"], 0)

    def test_rejects_enabled_real_source_without_approval(self) -> None:
        fixture = {
            "version": 1,
            "sources": [
                {
                    "id": "unsafe",
                    "county": "Test",
                    "source_name": "Unsafe source",
                    "data_class": "real",
                    "approval_status": "access_obtained_compliance_hold",
                    "enabled": True,
                    "gates": {
                        "access": True,
                        "terms": True,
                        "privacy": True,
                        "data": True,
                        "operations": True,
                    },
                    "allowed_fields": [],
                    "prohibited_fields": [],
                    "hold_reasons": [],
                }
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "policy.json"
            path.write_text(json.dumps(fixture), encoding="utf-8")
            policy = load_source_policies(path)["unsafe"]
        self.assertFalse(policy.executable)
        with self.assertRaises(SourceNotApprovedError):
            require_source_approved(policy)

    def test_rejects_allowed_prohibited_overlap(self) -> None:
        fixture = {
            "version": 1,
            "sources": [
                {
                    "id": "overlap",
                    "county": "Test",
                    "source_name": "Overlap",
                    "data_class": "synthetic",
                    "approval_status": "synthetic_only",
                    "enabled": True,
                    "gates": {gate: True for gate in ("access", "terms", "privacy", "data", "operations")},
                    "allowed_fields": ["Owner"],
                    "prohibited_fields": ["owner"],
                    "hold_reasons": [],
                }
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "policy.json"
            path.write_text(json.dumps(fixture), encoding="utf-8")
            with self.assertRaises(PolicyError):
                load_source_policies(path)


if __name__ == "__main__":
    unittest.main()
