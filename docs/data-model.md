# Conceptual Data Model

This is a vocabulary for research and design, not a database schema.

| Entity | Purpose | Important concepts |
| --- | --- | --- |
| `Jurisdiction` | County, city, court, or district responsible for records | name, type, geography, parent jurisdiction |
| `Agency` | Official record owner or publisher | department, contact, jurisdiction |
| `Source` | A discoverable access point | official URL, access method, format, terms, cadence, status |
| `SourceVersion` | Time-bounded source definition | schema notes, effective dates, verification evidence |
| `AcquisitionRun` | One future retrieval attempt | timestamps, outcome, counts, checksum, error summary |
| `SourceRecord` | Immutable representation of a retrieved record | source identifier, observed time, raw reference |
| `Parcel` | Jurisdiction-specific land unit | APN, geometry reference, jurisdiction |
| `Address` | Normalized location with original text retained | components, geocode, confidence |
| `Party` | Person or organization appearing in a record | source spelling, role, resolution confidence |
| `Document` | Recorded instrument or other filing | type, recording number, dates, parties, parcel links |
| `TaxAccount` | Tax status associated with a parcel | year, amounts, status, dates |
| `Case` | Court matter and public docket metadata | court, case number, type, status, dates |
| `Violation` | Code or nuisance enforcement event | agency, case number, status, dates |
| `Observation` | Time-stamped fact from a source | value, field, source record, confidence |
| `Indicator` | Explainable derived signal | definition version, inputs, output, freshness |

## Identity rules

- APNs are scoped to the issuing jurisdiction and preserved as strings.
- Recording, case, tax, and enforcement numbers are source-system identifiers, not global IDs.
- Addresses do not prove parcel or party identity by themselves.
- Party resolution must preserve the source spelling and a confidence or review state.
- Corrections create new observations; they do not silently rewrite provenance.

## Required provenance

Every future normalized fact should answer: who published it, where it was retrieved, when it was observed, which source record supports it, and which transformation produced it.
