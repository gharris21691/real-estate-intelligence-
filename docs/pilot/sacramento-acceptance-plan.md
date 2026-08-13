# Sacramento pilot acceptance plan

Targets are provisional until agency samples establish a baseline. Hard guardrails are not negotiable.

## Primary KPIs

| KPI | Definition | Provisional target | Decision use |
| --- | --- | --- | --- |
| Usable parcel coverage | Distinct secured-roll APNs that pass key validation and are available to the analyst ÷ distinct source APNs | At least 99.5%, with 100% of exclusions explained | Determines whether the roll can support the workflow |
| Geometry match rate | Valid secured-roll APNs matched to exactly one approved active geometry ÷ valid secured-roll APNs | Baseline first; proposed gate ≥98%, with all unmatched/multiple matches reported | Tests whether the two-source pilot is operationally useful |
| Evidence completeness | Displayed facts with source, effective date, retrieval time, source key, and transformation version ÷ displayed facts | 100% | Ensures every result is explainable |

## Drivers

- Required-field validity: valid values ÷ records for each required field.
- Duplicate-key exception rate: APNs with more than one record at the intended grain ÷ valid APNs.
- Geometry validity rate: valid, non-empty geometries ÷ received candidate geometries.
- Review resolution rate: resolved exceptions ÷ exceptions opened during the pilot review window.

## Hard guardrails

| Guardrail | Target |
| --- | --- |
| Prohibited fields retrieved or stored | 0 |
| Source-system write attempts | 0 |
| Facts without provenance | 0 |
| Raw public-record or personal-data files committed to Git | 0 |
| Undocumented record drops or silent join fallbacks | 0 |
| Portal scraping or access outside written approval | 0 |

## Reliability checks

- The same inputs and transformation version produce identical record counts, checksums, and exception sets.
- Totals reconcile from raw input to accepted, rejected, duplicate, and review records.
- Geometry transformations record source and target spatial references.
- Missing and stale data appear explicitly; they are not converted into negative signals.

## Analyst validation

Use a small sample selected across valid matches, unmatched APNs, duplicate cases, missing values, and parcel-status variations. Record whether the analyst can find the evidence, understand freshness, and explain each exception without consulting implementation logs.

Do not set a time-saved target until a manual baseline is measured on the same tasks. After baseline measurement, compare median completion time and evidence-error rate for at least 20 representative parcel reviews.

## Go/no-go rule

The pilot may proceed to a limited implementation only when:

1. agency access and field permissions are documented;
2. every hard guardrail passes;
3. evidence completeness is 100%;
4. coverage and match results meet agreed targets or have an accepted exception plan; and
5. the analyst review finds no unresolved provenance or interpretation defect.

Any privacy, access, or source-ownership ambiguity is a no-go regardless of technical metrics.
