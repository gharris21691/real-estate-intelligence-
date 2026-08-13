"""Validation for canonical synthetic or approved parcel observations."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from typing import Mapping


@dataclass(frozen=True)
class ValidationIssue:
    field: str
    code: str
    message: str


def validate_parcel_observation(record: Mapping[str, object]) -> tuple[ValidationIssue, ...]:
    issues: list[ValidationIssue] = []
    apn = record.get("source_apn")
    if not isinstance(apn, str) or not apn.strip():
        issues.append(ValidationIssue("source_apn", "required", "APN must be a non-empty string"))

    roll_year = record.get("roll_year")
    if not isinstance(roll_year, int) or not 1900 <= roll_year <= 2200:
        issues.append(ValidationIssue("roll_year", "invalid_year", "Roll year must be an integer from 1900 through 2200"))

    for field in (
        "assessed_land_value",
        "assessed_improvement_value",
        "total_assessed_value",
        "exemption_value",
    ):
        value = record.get(field)
        if value is None:
            continue
        try:
            number = Decimal(str(value))
        except (InvalidOperation, ValueError):
            issues.append(ValidationIssue(field, "invalid_amount", "Value must be numeric"))
            continue
        if number < 0:
            issues.append(ValidationIssue(field, "negative_amount", "Value cannot be negative"))

    land_use = record.get("assessor_land_use_code")
    if land_use is not None and (not isinstance(land_use, str) or len(land_use) != 6):
        issues.append(ValidationIssue("assessor_land_use_code", "invalid_code", "Land-use code must be a six-character string"))

    return tuple(issues)
