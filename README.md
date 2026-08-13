# Real Estate Intelligence

Documentation-first groundwork for a California real-estate intelligence platform. The project is intended to organize public-record research, preserve source provenance, and eventually support compliant property-data ingestion and lead analysis.

## Current phase

The repository is in **Phase 1: source discovery and specification**. It contains no production ingestion code, scrapers, database migrations, or user interface implementation.

## Repository map

- `docs/` — product boundaries, architecture, roadmap, conceptual data model, and scoring principles.
- `research/` — county source catalog and county-specific research records.
- `backend/` — reserved for later application and ingestion services.
- `frontend/` — reserved for later analyst workflows and user interface code.
- `data/` — reserved for local development fixtures; raw public-record exports must not be committed.
- `scripts/` — reserved for later operational tooling.
- `tests/` — reserved for future automated validation.

## Working sequence

1. Define the documentation and research framework.
2. Research and approve Sacramento County sources.
3. Expand the California county catalog using the same evidence standard.
4. Design an ingestion pilot only after source access, legal, privacy, and quality reviews pass.

See [the roadmap](docs/roadmap.md) for phase gates and [the Sacramento research specification](research/california/sacramento/source-research-spec.md) for the required evidence.

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
