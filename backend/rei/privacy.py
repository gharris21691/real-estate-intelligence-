"""Field-level privacy policy enforcement."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, TypeVar

T = TypeVar("T")


class ProhibitedFieldError(ValueError):
    """Raised when a record contains an explicitly prohibited field."""


@dataclass(frozen=True)
class FilteredRecord:
    values: dict[str, object]
    omitted_fields: tuple[str, ...]


SACRAMENTO_PROHIBITED_FIELDS = frozenset(
    {
        "owner",
        "owner_name",
        "name",
        "care_of_name",
        "mail1",
        "mail2",
        "mail_city",
        "mail_state",
        "mailing_address",
        "mailing_zip",
        "foreign_mail_address",
        "phone",
        "email",
    }
)

SACRAMENTO_PROVISIONAL_CANONICAL_FIELDS = frozenset(
    {
        "source_apn",
        "roll_year",
        "situs_address_raw",
        "assessed_land_value",
        "assessed_improvement_value",
        "total_assessed_value",
        "exemption_value",
        "tax_rate_area_code",
        "assessor_land_use_code",
        "recorder_book_page",
    }
)


def enforce_field_policy(
    record: Mapping[str, T],
    *,
    allowed_fields: set[str] | frozenset[str],
    prohibited_fields: set[str] | frozenset[str],
    reject_prohibited: bool = True,
) -> FilteredRecord:
    prohibited_normalized = {field.casefold() for field in prohibited_fields}
    present_prohibited = sorted(
        field for field in record if field.casefold() in prohibited_normalized
    )
    if present_prohibited and reject_prohibited:
        raise ProhibitedFieldError(
            "Record contains prohibited fields: " + ", ".join(present_prohibited)
        )

    values = {field: value for field, value in record.items() if field in allowed_fields}
    omitted = tuple(sorted(set(record) - set(values)))
    return FilteredRecord(values=values, omitted_fields=omitted)
