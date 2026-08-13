# Sacramento County Source-Research Specification

## Objective

Produce an evidence-backed inventory of official Sacramento County and relevant city sources that could support a narrowly defined real-estate research pilot. This specification ends at a source approval recommendation; it does not include ingestion implementation.

## Required source record

For every candidate, document:

| Field | Requirement |
| --- | --- |
| Source name | Official product, portal, report, or office name |
| Owning agency | Department and jurisdiction |
| Official URL | Direct agency-controlled page where possible |
| Record scope | Included and excluded record types |
| Geographic scope | Countywide, unincorporated area, city, court district, or other boundary |
| Access method | Portal search, bulk download, API, GIS service, report, subscription, or request |
| Authentication | None, account, agreement, API key, or other requirement |
| Cost | Search, document, subscription, bulk, or request fees; cite a schedule |
| Formats | HTML, PDF, CSV, JSON, XML, GIS formats, images, or physical copies |
| Identifiers | APN, recording number, case number, tax account, address, enforcement case, etc. |
| Search inputs | Supported query keys and limitations |
| Fields available | Field inventory with examples from non-sensitive samples where allowed |
| Update cadence | Published cadence plus observed cadence, clearly distinguished |
| Historical depth | Earliest available date and known gaps |
| Terms and restrictions | Terms, robots guidance, licensing, redistribution, rate limits, and statutory constraints |
| Reliability | Availability, pagination, anti-automation behavior, schema stability, and support channel |
| Verification evidence | Page title, URL, checked date, and claim supported |
| Open questions | Items requiring agency confirmation or counsel review |
| Recommendation | Verified, Approved for pilot, Blocked, or Deferred, with rationale |

## Research procedure

1. Confirm the owning agency and jurisdiction on an official government domain.
2. Separate search/view access from document-copy or bulk-data access.
3. Capture published help, fee, technical, and policy documentation.
4. Perform only minimal manual sampling permitted by the public interface; do not bulk collect records.
5. Record exact identifiers and whether they join reliably to parcels or addresses.
6. Note field variability, missingness, duplicates, corrections, and lag.
7. Identify city/county coverage gaps and overlapping authorities.
8. Complete privacy, terms, and automation reviews before recommending a pilot.

## Evaluation rubric

Score each dimension from 0 to 3 only after evidence is recorded:

- Authority: aggregator/unclear → official system of record.
- Accessibility: manual/fragile → documented bulk or API access.
- Coverage: unclear/sparse → documented complete scope.
- Freshness: unknown/stale → timely and measurable.
- Identifier quality: weak text matching → stable parcel/source identifiers.
- Operational stability: brittle → documented, supportable interface.
- Compliance fit: unresolved restrictions → explicit permitted use.
- Cost fit: unknown/prohibitive → predictable and acceptable.

A high technical score cannot override unresolved terms, privacy, or legal concerns.

## Approval gates

- **Research gate:** all required fields are complete or marked unknown with an owner and next step.
- **Compliance gate:** access, storage, reuse, redistribution, and contact-use questions are resolved.
- **Data gate:** sample fields, identifiers, freshness, and quality support the stated use case.
- **Operations gate:** rate, cost, monitoring, failure handling, and support assumptions are documented.
- **Pilot gate:** a reviewer records the approved source, fields, frequency, retention, and use case.

## Evidence log template

| Checked (YYYY-MM-DD) | Official page/document | URL | Claim supported | Researcher | Notes |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Decision record

- Status: `In research`
- Decision owner: TBD
- Approved use case: None yet
- Approved fields: None yet
- Next review date: TBD
