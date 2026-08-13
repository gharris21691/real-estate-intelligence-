# Sacramento pilot data contract

Status: `Provisional — pending agency samples and approval`

## Grain and keys

- Canonical grain: one observation of one Sacramento County parcel for one assessment roll year.
- Primary source key: the Assessor APN exactly as delivered.
- Geometry relationship: zero or one active parcel geometry per canonical APN, with exceptions recorded rather than discarded.
- No address or owner-name matching may silently replace an APN join.

## Proposed Assessor fields

Final source names and types must come from the agency data dictionary.

| Canonical field | Purpose | Provisional rule |
| --- | --- | --- |
| `source_apn` | Parcel key | Required string; preserve leading zeros and original value |
| `roll_year` | Observation period | Required; agency-defined assessment year |
| `situs_address_raw` | Analyst lookup/display | Optional; store exactly as delivered before normalization |
| `assessed_land_value` | Assessment context | Optional non-negative amount |
| `assessed_improvement_value` | Assessment context | Optional non-negative amount |
| `total_assessed_value` | Assessment context | Optional; source value controls if components do not reconcile |
| `exemption_value` | Assessment context | Optional non-negative amount |
| `tax_rate_area_code` | Geographic/tax reference | Optional string |
| `assessor_land_use_code` | Assessment-use classification | Optional string; never label as zoning |
| `recorder_book_page` | Source cross-reference | Optional source text; not a global document ID |

## Proposed GIS fields

Only this minimal set is proposed from the Active GIS Parcel Base layer:

| Source field | Canonical use | Rule |
| --- | --- | --- |
| `PARCEL_NUMBER` | APN join candidate | Required string; compare format with Assessor sample before approval |
| `APN_DASH` | Display/reference | Optional string |
| `PRCL_KEY` | GIS source key | Preserve as source string |
| `PARCEL_STATUS` | Active-status review | Preserve source value; obtain domain definitions |
| `SHAPE` | Parcel geometry | Preserve source spatial reference and transformation metadata |

## Prohibited fields

Do not request, retrieve, normalize, or store GIS `OWNER`, `NAME`, `CARE_OF_NAME`, `MAIL1`, `MAIL2`, `MAIL_CITY`, `MAIL_STATE`, `MAILING_ZIP`, or foreign-mailing fields. This prohibition remains until a field-level decision record explicitly changes it.

## Provenance required on every record

- source agency and source name;
- source file/service identifier;
- source roll year or effective date;
- retrieval timestamp;
- source record key;
- raw-file checksum or service-query fingerprint;
- transformation version; and
- validation status and exception reason.

## Exception handling

- Duplicate APNs, multiple active geometries, null keys, invalid geometries, and unmatched records go to review queues.
- Corrections create a new observation or run; prior evidence is not overwritten.
- Rejected records retain a non-sensitive reason code and source reference.
- Unknown source codes remain unknown until the agency supplies definitions.

## Pending decisions

- Actual roll field names, formats, and null conventions.
- APN normalization and parcel-change rules.
- Approved geometry delivery method and refresh schedule.
- Retention period for raw files and normalized observations.
- Whether situs address is necessary for the pilot or can be omitted.
