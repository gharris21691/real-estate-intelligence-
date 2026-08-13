# California automation access requests

This is the combined access tracker for Sacramento and the first California expansion candidates. A source remains disabled until its request is answered and the business, terms, privacy, and operations gates are approved.

## Combined priority tracker

| Priority | County and source | Official route | Current status | Next action | Decision |
| --- | --- | --- | --- | --- | --- |
| 1 | Sacramento secured assessment roll | `assessor@saccounty.gov`; [detailed checklist](../sacramento/agency-requests.md) | **Access obtained** on 2026-08-13 | Record the layout, effective date, update schedule, code definitions, and written use terms | Access gate complete; other gates pending |
| 2 | Sacramento Active GIS Parcel Base | `ASR-Mapping@saccounty.gov`; [detailed checklist](../sacramento/agency-requests.md) | Request sent; response pending | Obtain field-level and automated-use approval | Pending |
| 3 | San Bernardino ATC tax open data | [ATC Contact Us](https://www.sbcountyatc.gov/contact-us); (909) 387-8308 | [Ready to submit](san-bernardino-atc.md) | Submit the prepared request | Pending |
| 4 | Riverside Parcel Basic | [County Public Records Act Portal](https://riversidecountyca.nextrequest.com/requests/new), addressed to RCIT/GIS | [Ready to submit](riverside-gis.md) | Submit the prepared request | Pending |
| 5 | Yolo public parcels | `GIS@yolocounty.org`; fallback: `ITS.ServiceDesk@yolocounty.gov` | [Ready to send](yolo-gis.md) | Send the prepared request | Pending |
| 6 | Kern Assessor GIS data | Mark Larner, Mapping Section, `larner@kerncounty.com`, (661) 868-3378 | [Ready to send](kern-assessor-gis.md) | Send the prepared request | Pending |

Sacramento's item-level status stays in its [Assessor and GIS checklist](../sacramento/agency-requests.md). This combined table is the single high-level priority list.

Do not put credentials, access tokens, purchased files, or personal-record extracts in this repository. Save the agency's written response here only after removing signatures, phone numbers, and other unnecessary personal information.

## How to record a response

1. Enter the sent and response dates in the tracker.
2. Summarize the answer in the matching county file. Preserve a link or message identifier outside the repository if the original contains personal information.
3. Record every condition: permitted purpose, frequency, rate limits, retention, attribution, redistribution, cost, authentication, and revocation procedure.
4. Update `automation-source-registry.json` only after the written answer resolves the corresponding hold.
5. Keep `enabled` set to `false` until the full approval checklist is complete.

Official routes and source details verified 2026-08-13.
