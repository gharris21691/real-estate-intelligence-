# Sacramento parcel research pilot charter

## Decision to be tested

Can an analyst use a small, approved set of Sacramento County records to identify a parcel, review its current assessment context, and trace every displayed fact to its source faster and more reliably than using separate public portals?

This is a parcel-research pilot. It is not a lead-scoring, valuation, outreach, or contact-automation pilot.

## Proposed users and workflow

The initial user is an internal property researcher. Given an APN or situs address, the user should be able to:

1. locate the corresponding secured-roll parcel;
2. view approved assessment fields and parcel geometry;
3. see source, roll year, retrieval date, and freshness;
4. recognize missing, stale, conflicting, or unmatched records; and
5. export a small evidence record for manual review.

## Proposed source scope

| Source | Proposed use | Approval state |
| --- | --- | --- |
| Assessor secured assessment roll | Parcel identity and approved assessment attributes | Candidate; sample, layout, and terms requested |
| GIS Active Parcel Base | Geometry and minimal parcel identifiers/status | Candidate; field-level and automation approval requested |

Recorder, Tax Collector, Superior Court, and Code Enforcement are excluded from the first pilot. Their public portals remain manual research tools until an official bulk or approved programmatic route is confirmed.

## Privacy and use boundaries

- Exclude owner names, mailing addresses, phone numbers, email addresses, court parties, complainants, and document images.
- Do not infer occupancy, distress, willingness to sell, or legal status.
- Do not trigger marketing, contact, pricing, or eligibility decisions.
- Preserve APNs as source strings and retain the original source value.
- Keep raw agency files outside Git and limit access to approved project members.
- Use only the fields and retention period the agencies approve in writing.

## Deliverables after approval

- signed source/field decision record;
- source files and dictionaries stored outside Git;
- canonical mapping and validation report;
- synthetic test fixtures;
- repeatable but non-production pilot run;
- analyst review of a small, documented sample; and
- go, revise, or stop decision against the acceptance plan.

## Dependencies

Pilot implementation cannot begin until the Assessor and GIS questions in the [agency request package](../../research/california/sacramento/agency-requests.md) are answered. A public endpoint alone is not approval.

## Exit decision

Proceed beyond the pilot only if all hard guardrails pass and the source owners confirm permitted access, fields, frequency, retention, and redistribution. A technical success does not override an unresolved privacy or use restriction.
