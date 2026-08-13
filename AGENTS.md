# Repository Working Agreement

## Scope

Build a documented, source-grounded California real-estate intelligence system. Research comes before ingestion code.

## Rules

- Treat `research/` as evidence, not implementation guidance unless a source is marked `Approved for pilot`.
- Cite official agency pages or documents and include a verification date.
- Do not label guessed URLs, fields, update cadences, costs, or terms as verified facts.
- Do not implement scraping, ingestion, database, or UI code during the documentation phase.
- Never commit credentials, API keys, session cookies, purchased datasets, or raw records containing personal information.
- Preserve source-system identifiers and provenance in all future transformations.
- Add decision records when an architectural choice materially changes privacy, compliance, cost, or data lineage.

## Definition of done for source research

A source is `Verified` only when its owning agency, official URL, record scope, geography, access method, identifiers, format, cadence, cost, authentication, historical depth, restrictions, and verification date are documented. Approval for automation is a separate decision.
