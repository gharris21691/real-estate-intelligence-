import unittest

from rei.validation import validate_parcel_observation


class ParcelValidationTests(unittest.TestCase):
    def test_accepts_valid_synthetic_record(self) -> None:
        issues = validate_parcel_observation(
            {
                "source_apn": "000-0000-001-0000",
                "roll_year": 2026,
                "assessed_land_value": "125000",
                "assessor_land_use_code": "A1A00A",
            }
        )
        self.assertEqual(issues, ())

    def test_reports_invalid_values(self) -> None:
        issues = validate_parcel_observation(
            {
                "source_apn": 123,
                "roll_year": "2026",
                "assessed_land_value": "-1",
                "assessor_land_use_code": "short",
            }
        )
        self.assertEqual(
            {issue.code for issue in issues},
            {"required", "invalid_year", "negative_amount", "invalid_code"},
        )


if __name__ == "__main__":
    unittest.main()
