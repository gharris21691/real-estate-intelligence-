import unittest

from rei.privacy import (
    ProhibitedFieldError,
    SACRAMENTO_PROHIBITED_FIELDS,
    SACRAMENTO_PROVISIONAL_CANONICAL_FIELDS,
    enforce_field_policy,
)


class PrivacyPolicyTests(unittest.TestCase):
    def test_rejects_prohibited_field_case_insensitively(self) -> None:
        with self.assertRaises(ProhibitedFieldError):
            enforce_field_policy(
                {"source_apn": "000", "OWNER_NAME": "Do not retain"},
                allowed_fields=SACRAMENTO_PROVISIONAL_CANONICAL_FIELDS,
                prohibited_fields=SACRAMENTO_PROHIBITED_FIELDS,
            )

    def test_omits_unknown_fields(self) -> None:
        result = enforce_field_policy(
            {"source_apn": "000", "unapproved_note": "omit"},
            allowed_fields=SACRAMENTO_PROVISIONAL_CANONICAL_FIELDS,
            prohibited_fields=SACRAMENTO_PROHIBITED_FIELDS,
        )
        self.assertEqual(result.values, {"source_apn": "000"})
        self.assertEqual(result.omitted_fields, ("unapproved_note",))


if __name__ == "__main__":
    unittest.main()
