# Assessor and GIS request package

These drafts track the project owner's agency requests. Access to the Assessor secured assessment roll has been obtained, but access alone does not authorize automated processing or resolve the remaining use terms.

## Access checklist

| Item | Status | Updated | Notes |
| --- | --- | --- | --- |
| Assessor request submitted | Complete | 2026-08-13 | Project owner confirmed submission. |
| Electronic secured assessment roll access | Complete | 2026-08-13 | Project owner confirmed access. Do not store the roll in Git. |
| File layout or data dictionary | Pending confirmation | 2026-08-13 | Record the County-provided documentation or request it separately. |
| Roll effective date and file format | Pending confirmation | 2026-08-13 | Inspect only after an approved storage location is established. |
| Update and correction schedule | Pending | 2026-08-13 | Written confirmation still needed. |
| Parcel-status and land-use code definitions | Pending | 2026-08-13 | Written definitions still needed. |
| Storage, retention, automation, and derived-use terms | Pending | 2026-08-13 | Access is not treated as permission for unattended processing. |
| Redistribution terms | Pending | 2026-08-13 | Source records must not be redistributed meanwhile. |
| Two-year Change in Ownership file | Pending | 2026-08-13 | Confirm whether separate access was granted or must be requested. |
| GIS automation/field approval | Pending | 2026-08-13 | Separate from Assessor roll access. |

## Assessor request

**To:** assessor@saccounty.gov

**Subject:** Request for electronic secured assessment roll and data documentation

Hello,

I’m researching a small internal parcel-data pilot for Sacramento County. Your fee schedule says the electronic secured assessment roll is available at no charge, and I’d like to request the current electronic roll or instructions for obtaining it.

Could you also provide any available file layout or data dictionary, the roll’s effective date, file format, update and correction schedule, and the meaning of its parcel-status or land-use codes?

The pilot would initially use parcel identifiers, assessment values, tax-rate-area code, land-use code, and possibly situs address. It would not use owner names or mailing addresses unless the County confirms those fields are appropriate for this use.

Please let me know whether there are terms covering storage, retention, automated processing, derived data, or redistribution, and whether a two-year Change in Ownership transfer file must be requested separately.

Thank you,

Gabriel Harris

## Assessor Mapping / GIS request

**To:** ASR-Mapping@saccounty.gov

**Subject:** Questions about approved use of Sacramento County parcel GIS data

Hello,

I’m evaluating Sacramento County’s Active GIS Parcel Base for a small internal parcel-research pilot. The proposed use is limited to parcel geometry and a minimal set of identifiers: `PARCEL_NUMBER`, `APN_DASH`, `PRCL_KEY`, and `PARCEL_STATUS`.

Could you confirm whether automated read-only queries to the County ArcGIS REST service are permitted for this purpose, or whether the County prefers a downloadable parcel file? I’d also appreciate the expected refresh schedule, parcel-status definitions, license or attribution requirements, rate limits, and any restrictions on storing derived geometry.

The published REST schema includes owner and mailing fields, while the Assessor’s Parcel Viewer documentation says owner information is not displayed online because of privacy concerns. We plan to exclude those fields. Please confirm that this is the correct approach and whether any other fields should be excluded.

Thank you,

Gabriel Harris

## Response log

| Date | Agency/contact | Response summary | Evidence location | Decision impact |
| --- | --- | --- | --- | --- |
| 2026-08-13 | Sacramento County Assessor | Project owner confirmed access to the electronic secured assessment roll. The County's detailed response and terms have not yet been recorded. | Project owner confirmation; source data and credentials intentionally excluded from Git | Access gate satisfied; documentation, terms, privacy, and data-quality gates remain pending. |
