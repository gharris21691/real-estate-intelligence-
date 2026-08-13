# Scoring Principles

No lead score is implemented or approved. This document defines the guardrails for a later design.

## Requirements

- Scores must be explainable as named indicators with visible source dates.
- Each indicator must document its purpose, inputs, exclusions, lookback window, missing-data behavior, and known biases.
- Missing or stale data must not be treated as a negative event.
- Conflicting source records must surface uncertainty rather than be silently collapsed.
- Sensitive or legally restricted attributes must not be used without explicit review.
- A score should prioritize analyst review; it must not automatically trigger contact or an adverse decision.

## Validation plan

Before deployment, evaluate precision, recall, freshness, geographic coverage, subgroup impacts where lawful and appropriate, false-positive cost, and stability across time. Maintain a versioned change log and a way for analysts to report incorrect evidence.

## Candidate indicator template

| Field | Required entry |
| --- | --- |
| Name | Human-readable label |
| Decision supported | Specific analyst action |
| Source fields | Approved inputs and provenance |
| Logic | Plain-language rule or calculation |
| Window | Relevant observation period |
| Freshness limit | Age after which the indicator is stale |
| Missing data | Explicit behavior |
| Exclusions | Records or cases that must not qualify |
| Risks | Bias, ambiguity, or compliance concerns |
| Validation | Test and acceptance criteria |
