# Roadmap

## Phase 1 — Foundation and research framework

**Deliverables:** repository structure, documentation framework, Sacramento research specification, California county catalog, source worksheets, and a synthetic data-safe software foundation.

**Implementation progress:** External-drive configuration guards, metadata manifests and checksums, SQLite provenance migrations, privacy field enforcement, canonical validation, synthetic Sacramento fixtures, and automated tests are implemented. No real County data or live source is processed.

**Exit gate:** stakeholders agree on scope, status vocabulary, research fields, and evidence requirements.

## Phase 2 — Sacramento source verification

Research Recorder, Assessor, Tax Collector, Courts, GIS/Open Data, and Code Enforcement sources. Capture official evidence, sample access, field inventories, identifiers, cadence, costs, terms, and blockers.

**Exit gate:** each candidate is marked `Verified`, `Blocked`, or intentionally deferred; no unverified source proceeds.

## Phase 3 — Pilot design

Choose a narrow use case and the smallest approved source set. Define privacy and compliance controls, canonical fields, service-level expectations, test fixtures, and acceptance metrics.

**Progress:** A provisional Sacramento parcel-research charter, data contract, acceptance plan, and agency request package are drafted. Synthetic foundation work may proceed, but real-data implementation remains blocked pending Assessor/GIS responses and a recorded source/field approval.

**Parallel source work:** Recorder expansion is defined as a separate gate. The preferred path is the Assessor’s monthly two-year transfer file, followed by an official Recorder bulk product if one exists; portal scraping is excluded.

**Exit gate:** written approval for named sources and fields, plus a reviewed pilot plan.

## Phase 4 — Backend ingestion pilot

Implement acquisition and normalization for the approved Sacramento sources only. This phase is intentionally outside the current repository initialization request.

**Exit gate:** provenance, freshness, reconciliation, failure recovery, and data-quality tests pass.

## Phase 5 — Analysis and analyst workflow

Add explainable indicators, review queues, and a limited interface. Validate whether the workflow improves research speed without hiding uncertainty.

## Phase 6 — County expansion

Prioritize additional counties using source availability, opportunity, cost, policy constraints, and operational reuse. County rollout is gated independently.

**Preparation:** An August 2026 market/source shortlist and a disabled automation registry now identify San Bernardino tax data, Riverside parcels, and Yolo parcels as the leading machine-readable candidates. This preparation does not move those counties into Phase 4; each source still requires independent terms, privacy, data, and operations approval.

## Explicit non-goals for Phases 1–2

- Production scraping or ingestion.
- Automated outreach or marketing.
- A predictive valuation model.
- A statewide person-level identity graph.
- Purchasing data before official-source gaps are documented.
