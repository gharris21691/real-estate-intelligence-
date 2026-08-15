# California automated acquisition readiness plan

Status: `Prepared — no production collection authorized`

## Decision

Prepare the first automated acquisition wave in this order:

1. **San Bernardino Treasurer-Tax Collector open data** — documented CKAN and dataset APIs, weekly CSV/Parquet resources, and the most directly useful delinquency fields.
2. **Riverside Parcel Basic** — official ArcGIS REST layer with APN and geometry only, updated Monday through Friday.
3. **Yolo public parcels** — official ArcGIS FeatureServer with parcel, assessment, land-use, acreage, and geometry fields; the Recorder portal remains excluded from automation.
4. **San Bernardino Assessor bulk files** — direct monthly and annual ZIP downloads, subject to field-level minimization and reuse confirmation.
5. **Kern parcel data** — available as a paid county dataset; the map viewer exposes an ArcGIS service reference, but direct metadata requests currently return `499 Token Required`. An approved token or a delivered file is required, and unattended or commercial use must also be confirmed because the county's website policy restricts documents to informational or personal use.
6. **Stanislaus and Fresno file products** — automate only after subscription, delivery, licensing, and credential handling are documented.

All registry entries are disabled. `Technical ready` means the endpoint and pagination/download pattern are documented; it does not mean the compliance gate has passed.

## Automated-source matrix

| Rank | County and source | Method | Cadence | Initial value | Current gate |
| ---: | --- | --- | --- | --- | --- |
| 1 | San Bernardino defaulted bills, five years or newer | CKAN metadata API plus CSV/Parquet download | Weekly, Sunday | Default date/number, balances, redemption and payment-plan status | Dataset page reports no license; confirm commercial storage and reuse |
| 2 | San Bernardino bills and installments, five years or newer | CKAN metadata API plus CSV/Parquet download | Weekly, Sunday | Current and historical bill, installment, balance, delinquency, and TRA data | Same license confirmation |
| 3 | Riverside Parcel Basic | ArcGIS REST query | Daily, Monday-Friday | APN, parcel flag, geometry | Confirm unattended query and retention terms |
| 4 | Yolo public parcels | ArcGIS REST query/extract | Source revision field available; published cadence not stated | Assessment number, land/structure values, TRA, land use, acreage, geometry | Confirm automated reuse; exclude Recorder entirely |
| 5 | San Bernardino current-year bills | CKAN metadata API plus CSV/Parquet download | Weekly, Sunday | Current bill and installment status | Same license confirmation |
| 6 | San Bernardino Assessor secured roll | Direct ZIP download | Monthly and annual | Assessment-roll and parcel-change context | Field minimization and commercial-use confirmation |
| 7 | Kern parcel data | Token-protected ArcGIS candidate or paid file delivery | Final edition annually; preliminary editions vary | APN and parcel geometry | Approved access method plus written policy clarification before unattended use |
| 8 | Stanislaus parcel shapes and secured roll | Free shape download plus authenticated subscription | Monthly roll updates after purchase | APN geometry, assessment roll, ownership changes | Purchase, terms acceptance, no-transfer restriction, credential plan |
| 9 | Fresno GIS and Assessor files | Shapefile download plus purchased CSV/text files | GIS varies; roll annual; ownership monthly; sales quarterly | APN geometry, situs, assessment roll, and sales | Purchase/delivery agreement and reuse terms |

## Wave 1 pull design

### 1. San Bernardino tax open data

Use the CKAN API to resolve the current resource URL on every run instead of hard-coding the linked `county-reports.com` CSV URL. Prefer the county-hosted Parquet resource when present.

Run sequence:

1. Call `package_show` using the stable dataset name recorded in the source registry.
2. Confirm the title, expected resource formats, metadata-modified timestamp, and license field.
3. Select the Parquet resource when available; otherwise use CSV.
4. Download to an uncommitted run directory.
5. Record URL, dataset UUID, resource UUID, response headers, byte count, retrieval time, and SHA-256 checksum.
6. Reject the run if required columns are missing, types drift unexpectedly, or the file is empty.
7. Keep the raw file immutable; create normalized outputs in a separate run path.

The initial datasets are:

- `Defaulted Bills 5 Years or Newer`
- `Bills and Installments 5 Years or Newer`
- `Bills and Installments Current Year`

Do not infer property ownership from tax account data. Account number, bill number, and TRA are source identifiers, not confirmed APN equivalents.

### 2. Riverside Parcel Basic

Use only layer 40 of the county's official OpenData Assessor MapServer. The published fields are `OBJECTID`, `APN`, `FLAG`, and geometry. Do not use the `PARCELS_CREST` layer or CREST tables in the first wave because those sources expose names and mailing information.

Run sequence:

1. Fetch layer metadata with `f=json` and compare the schema fingerprint.
2. Request object IDs for `where=1=1`.
3. Retrieve deterministic ID batches no larger than the service's 2,000-record limit.
4. Request only `OBJECTID,APN,FLAG` plus geometry.
5. Preserve source spatial reference `EPSG:2230` and record any transformation separately.
6. Validate unique object IDs, nonblank APNs, geometry validity, and batch completeness.

### 3. Yolo public parcels

The parcel layer supports pagination, extraction, JSON, GeoJSON, and PBF. The first pull should request only:

- `OBJECTID`
- `MPTS_ASMT_NUMBER`
- `Roll_Asmt`
- `Roll_Land`
- `Roll_Structure`
- `Roll_TRA`
- `REVDATE`
- `MAPYEAR`
- `GIS_Acres`
- `Roll_Acres`
- `LU_LandUseCode`
- `LU_Descr`
- `Jurisdiction`
- geometry

Exclude `Name`, all `Situs_*` fields, and `Situs_Address` from the first pull. Do not query or automate Yolo's Official Records Search; the county expressly prohibits scripted, unattended, robotic, mining, and scraping access to that utility.

## Data minimization boundary

The first automated wave is property- and obligation-oriented, not person-oriented.

Allowed initially:

- parcel or assessment identifiers;
- parcel geometry and source spatial reference;
- assessed land, improvement, and total values;
- tax rate areas and land-use codes;
- bill, balance, delinquency, default, redemption, and payment-plan status;
- source dates, update dates, and technical run metadata.

Excluded initially:

- owner or assessee names;
- mailing addresses and care-of names;
- phone numbers and email addresses;
- document images;
- court-party data;
- automated Recorder searches;
- contact enrichment or skip tracing.

Changing this boundary requires a field-level decision record.

## Metadata-only preflight results

Checked 2026-08-13 without downloading record rows:

- **San Bernardino CKAN:** all three priority datasets resolved successfully through `package_show`; Parquet resource UUIDs are captured in the registry. Each dataset returned a blank license field.
- **Riverside Parcel Basic:** returned a `Feature Layer` with a 2,000-record limit, JSON/GeoJSON/PBF support, query capability, and the expected `OBJECTID`, `APN`, `FLAG`, and geometry fields.
- **Yolo public parcels:** returned a `Feature Layer` with a 2,000-record limit, query/extract capability, and the expected assessment, value, land-use, revision, acreage, situs, and geometry-related fields. The registry allowlist excludes names and situs fields.
- **Kern parcels:** both official service host variants returned `499 Token Required`. Do not build an unauthenticated collector against this endpoint.

## Required implementation controls

- Source registry entry must be `enabled: true` only after a named reviewer signs the compliance and data gates.
- A run must begin with metadata/schema discovery and stop on unexpected changes.
- Concurrency and request rate start at one; increase only after the source documents a limit or the agency approves one.
- Retry only idempotent metadata and download requests, with bounded exponential backoff.
- Respect `Retry-After`, authentication failures, service errors, and maintenance windows.
- Never commit raw downloads, credentials, owner data, or exports.
- Store a checksum, byte count, retrieval timestamp, source URL, HTTP validators, schema fingerprint, and registry version for every artifact.
- Maintain a kill switch per source and a global acquisition kill switch.

## Approval checklist before the first data pull

| Gate | Required evidence | Owner | Status |
| --- | --- | --- | --- |
| Business | Exact use case and fields approved | TBD | Pending |
| Access | Endpoint/download mechanism and cadence confirmed | Research | Prepared |
| Terms | Automation, storage, commercial use, retention, and redistribution confirmed | TBD | Pending |
| Privacy | Initial field allowlist and exclusions approved | TBD | Pending |
| Technical | Pagination/download, checksum, schema, and retry plan reviewed | TBD | Prepared |
| Operations | Storage path, retention, monitoring, and kill switches configured | TBD | Pending |
| Data quality | Small sample reconciled to official manual lookup | TBD | Pending |

## Immediate next actions

1. Submit the prepared [San Bernardino ATC request](../../research/california/access-requests/san-bernardino-atc.md) to confirm that automated scheduled downloads, internal commercial analysis, retention, and derived indicators are permitted despite the catalog's blank license field.
2. Submit the prepared [Riverside GIS request](../../research/california/access-requests/riverside-gis.md) to confirm unattended REST queries of Parcel Basic, acceptable frequency, retention, and internal commercial use.
3. Send the prepared [Yolo GIS request](../../research/california/access-requests/yolo-gis.md) for the parcel FeatureServer while affirming that the Recorder portal will not be automated.
4. Send the prepared [Kern Assessor GIS request](../../research/california/access-requests/kern-assessor-gis.md) for an approved API token/service or the paid delivered dataset and written clarification before unattended commercial acquisition.
5. Request current Stanislaus and Fresno subscription/order terms only after Wave 1 feasibility is proven.

No production ingestion code or source data was added by this plan.

Verified 2026-08-13.
