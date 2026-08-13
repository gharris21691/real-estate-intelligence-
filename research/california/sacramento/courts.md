# Superior Court

- Research status: `Verified for manual research`
- Automation status: `Deferred — no documented bulk/API route`
- Identity resolution status: `Not approved`
- Verified: 2026-08-12
- Owning agency: Superior Court of California, County of Sacramento

## Official sources

- [Public Portal information](https://www.saccourt.ca.gov/indexes/new-portal-info.aspx)
- [Civil Records](https://www.saccourt.ca.gov/divisions/civil/civil-records)
- [Unlawful Detainer and Small Claims Records](https://www.saccourt.ca.gov/divisions/unlawful-detainer-landlord-tenant/unlawful-detainer-and-small-claims-records)
- [Public Case Access](https://services.saccourt.ca.gov/PublicCaseAccess/)

## Verified access profile

| Field | Finding |
| --- | --- |
| Record scope | Public portal access includes permitted civil case information and public documents. Public Case Access describes participants, events, and documents where applicable. |
| Civil depth | Civil cases and documents filed after November 13, 2007 are online; older civil files are physical/off-site. |
| Small Claims / UD depth | Small Claims initiated after 1999 and Unlawful Detainer cases initiated after 2005 are described as available. |
| UD restriction | Unlawful Detainer cases are masked and require at least one plaintiff, one defendant, and the premises address, including unit when applicable. |
| Access method | Account-based public portal; courthouse kiosks and records requests supplement online access. |
| Authentication | A public-user account requires email, phone number, and personal information. |
| Search inputs | Official materials describe name, case-number, and filing-date searches. |
| Cost | Online search and document-download fees were discontinued. Certified or staff-produced copies may incur search and per-page fees. |
| Restrictions | Confidential, sealed, and party-only documents are excluded. No official bulk feed, API, automation permission, or rate limits were identified. |

## Risks and limitations

- Names and addresses do not prove a case participant owns or controls a parcel.
- Unlawful Detainer masking is an access control and must not be circumvented.
- Court records include sensitive allegations and incomplete procedural states.
- Coverage and portal behavior changed during the recent case-system migration.
- Court data should not drive automated outreach or person-level scoring without separate review.

## Evidence log

| Checked | Official page/document | Claim supported |
| --- | --- | --- |
| 2026-08-12 | [New Portal](https://www.saccourt.ca.gov/indexes/new-portal-info.aspx) | Account requirement, civil boundary, public documents, and exclusions |
| 2026-08-12 | [Civil Records](https://www.saccourt.ca.gov/divisions/civil/civil-records) | Digital/physical boundary and copy channels |
| 2026-08-12 | [UD and Small Claims Records](https://www.saccourt.ca.gov/divisions/unlawful-detainer-landlord-tenant/unlawful-detainer-and-small-claims-records) | Historical coverage and masked UD requirements |
| 2026-08-12 | [Public Case Access](https://services.saccourt.ca.gov/PublicCaseAccess/) | Search keys, case information, and discontinued online fees |

## Recommendation and next action

Keep access manual and case-specific. Ask whether a licensed bulk service or approved research route exists and what California Rule of Court 2.506 constraints apply. Do not build party-to-parcel resolution or automated monitoring during the pilot.
