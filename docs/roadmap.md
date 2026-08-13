# Roadmap

## Phase 1 — Foundation and research framework

**Deliverables:** repository structure, documentation framework, Sacramento research specification, California county catalog, and source worksheets.

**Exit gate:** stakeholders agree on scope, status vocabulary, research fields, and evidence requirements.

## Phase 2 — Sacramento source verification

Research Recorder, Assessor, Tax Collector, Courts, GIS/Open Data, and Code Enforcement sources. Capture official evidence, sample access, field inventories, identifiers, cadence, costs, terms, and blockers.

**Exit gate:** each candidate is marked `Verified`, `Blocked`, or intentionally deferred; no unverified source proceeds.

## Phase 3 — Pilot design

Choose a narrow use case and the smallest approved source set. Define privacy and compliance controls, canonical fields, service-level expectations, test fixtures, and acceptance metrics.

**Progress:** A provisional Sacramento parcel-research charter, data contract, acceptance plan, and agency request package are drafted. Implementation remains blocked pending Assessor/GIS responses and a recorded source/field approval.

**Exit gate:** written approval for named sources and fields, plus a reviewed pilot plan.

## Phase 4 — Backend ingestion pilot

Implement acquisition and normalization for the approved Sacramento sources only. This phase is intentionally outside the current repository initialization request.

**Exit gate:** provenance, freshness, reconciliation, failure recovery, and data-quality tests pass.

## Phase 5 — Analysis and analyst workflow

Add explainable indicators, review queues, and a limited interface. Validate whether the workflow improves research speed without hiding uncertainty.

## Phase 6 — County expansion

Prioritize additional counties using source availability, opportunity, cost, policy constraints, and operational reuse. County rollout is gated independently.

## Explicit non-goals for Phases 1–2

- Production scraping or ingestion.
- Automated outreach or marketing.
- A predictive valuation model.
- A statewide person-level identity graph.
- Purchasing data before official-source gaps are documented.
