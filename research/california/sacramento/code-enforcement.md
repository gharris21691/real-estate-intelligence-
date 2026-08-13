# Code Enforcement

- Research status: `Verified for manual research`
- Automation status: `Deferred — public bulk/API access not documented`
- Verified: 2026-08-12
- Owning agency: Sacramento County Community Development, Code Enforcement Division

## Official sources

- [Code Enforcement Division](https://development.saccounty.gov/us/en/code-enforcement.html)
- [Report a Violation and process](https://development.saccounty.gov/us/en/code-enforcement/report-a-violation.html)
- [Code Enforcement contacts](https://development.saccounty.gov/us/en/code-enforcement/contact-us.html)
- [Code Enforcement fees](https://development.saccounty.gov/us/en/code-enforcement/fees.html)
- [County public-records portal](https://saccounty.nextrequest.com/)
- [Cities within the County](https://www.saccounty.gov/us/en/cities-within-the-county.html)

## Verified access profile

| Field | Finding |
| --- | --- |
| Record scope | Housing, zoning, and vehicle-abatement enforcement; described stages include notices, inspections, violations, fees, administrative actions, citations, and possible court action. |
| Geographic scope | Unincorporated Sacramento County only. The County does not enforce city ordinances inside the seven incorporated cities. |
| Access method | Official page links to Accela Citizen Access for case search. Support and fee workflows use case number/property address; NextRequest handles records requests. |
| Authentication | Public search requirements were not documented on the landing page. Online payment requires an account. |
| Identifiers | Code Enforcement case number and property address. |
| Complaint privacy | Complainant name, address, and contact information are kept confidential and described as exempt from disclosure. |
| Process timing | Guidance says zoning inspections generally occur in 3–4 weeks, housing in 5–6 weeks, and vehicle abatement in about 2 weeks. These are process estimates, not refresh guarantees. |
| Formats | Browser case search and request-produced records. No published bulk export or API was identified. |

## Jurisdiction coverage

| Jurisdiction | Responsible source | Status |
| --- | --- | --- |
| Unincorporated Sacramento County | County Code Enforcement / Accela | Verified; manual access only |
| Citrus Heights | City Code Enforcement | Not researched |
| Elk Grove | City Code Enforcement | Not researched |
| Folsom | City Code Enforcement | Not researched |
| Galt | City Code Compliance | Not researched |
| Isleton | City government | Not researched |
| Rancho Cordova | City Code Enforcement | Not researched |
| Sacramento | City Code Compliance | Not researched |

## Risks and limitations

- A complaint or advisory letter does not establish a verified violation.
- Open, alleged, corrected, appealed, and closed outcomes must remain distinct.
- Complainant information must never be sought or stored.
- County records do not provide incorporated-city coverage.
- The Accela page did not expose automation terms, rate limits, or bulk access during review.

## Evidence log

| Checked | Official page/document | Claim supported |
| --- | --- | --- |
| 2026-08-12 | [Code Enforcement](https://development.saccounty.gov/us/en/code-enforcement.html) | Scope, unincorporated boundary, case-search link, and enforcement tools |
| 2026-08-12 | [Report a Violation](https://development.saccounty.gov/us/en/code-enforcement/report-a-violation.html) | Confidential complainant data, identifiers, stages, and timing |
| 2026-08-12 | [Contacts](https://development.saccounty.gov/us/en/code-enforcement/contact-us.html) | Separate city enforcement authorities |
| 2026-08-12 | [Cities](https://www.saccounty.gov/us/en/cities-within-the-county.html) | Seven incorporated cities |
| 2026-08-12 | [NextRequest](https://saccounty.nextrequest.com/) | Public-record request route |

## Recommendation and next action

Use the case portal manually to document visible fields and status meanings without collecting complainant data. Ask whether an approved export or API exists and request its dictionary, geography, cadence, status semantics, terms, and privacy guidance. Research incorporated cities only after the unincorporated pilot scope is decided.
