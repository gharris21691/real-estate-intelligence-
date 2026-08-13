# Phase 2 Source Verification Findings

Verified on 2026-08-12 using official Sacramento County and Sacramento Superior Court sources. “Verified” means the source and stated operating facts were checked; it does not approve automation or ingestion.

## Decision summary

| Source family | Research result | Pilot recommendation | Principal blocker |
| --- | --- | --- | --- |
| Assessor | Electronic assessment rolls and a monthly two-year transfer file are available at no charge | Leading candidate via agency-delivered files | Obtain layouts, samples, terms, corrections, and approved fields |
| GIS | Official parcel REST layer supports pagination and JSON/GeoJSON/PBF | Candidate for geometry plus minimal APN/status | Confirm automation, license, cadence, and owner/mailing-field privacy conflict |
| Recorder | Official index covers 1849 onward and normally updates within two business days | Manual validation only | No documented bulk/API route; no online images |
| Tax Collector | e-PropTax exposes current/recent bills and prior secured delinquency by 14-digit APN | Manual validation only | No documented bulk/API route and payment-posting lag |
| Superior Court | Account-based portals expose permitted case information and documents | Defer from initial pilot | No documented bulk route; masking, identity, privacy, and fairness risks |
| Code Enforcement | County search covers unincorporated areas; records requests are available | Manual field/status discovery | No documented bulk/API route; seven cities require separate research |

## Recommended narrow pilot

Design the first pilot around an agency-delivered **secured assessment roll** joined to **parcel geometry with a minimal APN/status field set**. Do not include Recorder, tax, court, or code-enforcement acquisition until their agencies answer the access and terms questions in the worksheets.

Exclude owner/mailing fields from the GIS service, court-party resolution, complainant information, document images, and automated portal queries.

## Agency questions before pilot approval

1. Assessor: layouts, delivery format, roll-as-of date, correction files, definitions, terms, retention, and redistribution.
2. GIS/Assessor: approved REST fields, automation permission, refresh cadence, license, and the owner/mailing fields exposed in the REST schema despite Parcel Viewer privacy restrictions.
3. Recorder, Tax Collector, Court, and Code Enforcement: whether an official bulk, subscription, licensed export, or approved API exists and which uses are permitted.

## Gate status

- Research gate: **Passed for source discovery**.
- Compliance gate: **Open**.
- Data gate: **Open pending samples and dictionaries**.
- Operations gate: **Open pending delivery and cadence confirmation**.
- Pilot gate: **Not approved**.

No ingestion code should be implemented until the pilot gate records approved sources, fields, frequency, retention, and use case.
