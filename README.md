# Real Estate Intelligence

Documentation-first groundwork for a California real-estate intelligence platform. The project is intended to organize public-record research, preserve source provenance, and eventually support compliant property-data ingestion and lead analysis.

## Current phase

The repository is in **Phase 1: source discovery and data-safe foundation**. It now contains a local metadata/provenance schema, privacy controls, synthetic fixtures, validation, and tests. It contains no production ingestion, scrapers, live County connectors, or user interface implementation.

## Repository map

- `docs/` — product boundaries, architecture, roadmap, conceptual data model, and scoring principles.
- `research/` — county source catalog and county-specific research records.
- `backend/` — privacy-safe Python foundation and SQLite metadata schema; no live acquisition code.
- `frontend/` — reserved for later analyst workflows and user interface code.
- `data/` — synthetic development fixtures and ignored local metadata; raw public-record exports must not be committed.
- `scripts/` — reserved for later operational tooling.
- `tests/` — automated configuration, privacy, provenance, schema, and validation checks.

## Working sequence

1. Define the documentation and research framework.
2. Research and approve Sacramento County sources.
3. Expand the California county catalog using the same evidence standard.
4. Build and test a synthetic, data-safe foundation while approval questions are pending.
5. Design and run a real-data ingestion pilot only after source access, legal, privacy, and quality reviews pass.

See [the roadmap](docs/roadmap.md) for phase gates and [the Sacramento research specification](research/california/sacramento/source-research-spec.md) for the required evidence.

The current pilot proposal is documented in the [Sacramento pilot charter](docs/pilot/sacramento-pilot-charter.md). It remains provisional until the County confirms access and field-level terms.

The first statewide expansion screen is documented in the [August 2026 California county shortlist](research/california/expansion-shortlist-2026-08.md). It recommends a research sequence only; every county remains subject to the same approval gates as Sacramento.

The [California automated acquisition readiness plan](docs/pilot/california-automated-acquisition-plan.md) and [disabled source registry](research/california/automation-source-registry.json) prepare the highest-value machine-readable sources for a later approved pilot. They do not enable collection or add production ingestion code.

## Principles

- Prefer authoritative public agencies over aggregators.
- Record access terms, costs, update cadence, identifiers, and provenance before automation.
- Treat a source as unapproved until its access method and restrictions are verified.
- Keep raw personal data and credentials out of Git.
- Separate factual source research from implementation assumptions.

## Status legend

- `Not started` — no source research has been completed.
- `In research` — candidates are being evaluated.
- `Verified` — an official source and its operating details have been checked and dated.
- `Approved for pilot` — legal, technical, and data-quality gates have passed.
- `Blocked` — access, policy, cost, or quality prevents current use.
