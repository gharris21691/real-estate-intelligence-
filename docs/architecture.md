# Architecture

## Status

The source-specific architecture remains conceptual. A local, standard-library Python foundation and SQLite metadata schema are implemented for synthetic testing; no hosting vendor, production database, live connector, or County parser is approved.

## System boundaries

The future platform may consist of five separable layers:

1. **Source registry** — source ownership, access details, restrictions, field notes, verification history, and approval state.
2. **Acquisition** — source-specific retrieval jobs with rate limiting, retries, immutable run metadata, and raw-content checksums.
3. **Normalization** — canonical parcels, parties, addresses, filings, cases, taxes, violations, and source references.
4. **Analysis** — transparent, versioned indicators and scores built only from approved fields.
5. **Analyst experience** — search, evidence review, freshness warnings, and export controls.

## Data flow

`Official source → acquisition run → raw snapshot → normalized record → resolved property → indicator → analyst review`

Every normalized fact must retain the source, retrieval time, source record identifier when available, and transformation version. A later correction must not erase the ability to explain the earlier result.

## Core design decisions

- **Registry-driven:** acquisition is configured from approved source records rather than hard-coded assumptions.
- **Append-oriented provenance:** observations and run history are retained; current-state views are derived.
- **Source isolation:** failures or schema changes in one agency source do not corrupt unrelated sources.
- **Human review:** identity resolution and high-impact signals support review and correction.
- **Minimum necessary data:** collect only fields required for an approved use case.
- **Jurisdiction-aware:** county and city sources can overlap; the data model preserves the responsible jurisdiction.

## Implemented Phase 1 boundary

- `REI_DATA_ROOT` must resolve outside the Git repository.
- Source manifests contain filename, size, SHA-256, timing, and source metadata but omit the full external path.
- The SQLite schema records source definitions, artifacts, runs, parcel observations, and validation issues.
- Privacy filtering rejects prohibited fields before a record can enter the provisional canonical model.
- Tests and fixtures are synthetic and do not require the external drive.
- There is no downloader, scraper, scheduled job, live endpoint query, or real-roll parser.

## Non-functional requirements before a pilot

- Reproducible retrieval and transformation runs.
- Idempotent processing and duplicate detection.
- Field-level provenance and freshness.
- Audit logging for access and exports.
- Secrets management outside the repository.
- Retention and deletion controls.
- Monitoring for source drift, volume anomalies, and stale data.
- Documented recovery and manual fallback procedures.

## Open decisions

- Hosting and database platform.
- Geocoding and address-normalization provider.
- Parcel and party resolution strategy.
- Retention periods for raw and normalized records.
- Permitted user roles and export limits.
- Whether any commercial data should supplement official sources.
