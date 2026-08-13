# California automation access requests

This folder tracks written permission and access requests for the first automated-data candidates. A source remains disabled until its request is answered and the business, terms, privacy, and operations gates are approved.

## Wave 1 request tracker

| Order | County and source | Official route | Status | Sent | Response | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | San Bernardino ATC tax open data | [ATC Contact Us](https://www.sbcountyatc.gov/contact-us); (909) 387-8308 | Ready to submit | — | — | Pending |
| 2 | Riverside Parcel Basic | [County Public Records Act Portal](https://riversidecountyca.nextrequest.com/requests/new), addressed to RCIT/GIS | Ready to submit | — | — | Pending |
| 3 | Yolo public parcels | `GIS@yolocounty.org`; fallback: `ITS.ServiceDesk@yolocounty.gov` | Ready to send | — | — | Pending |
| 4 | Kern Assessor GIS data | Mark Larner, Mapping Section, `larner@kerncounty.com`, (661) 868-3378 | Ready to send | — | — | Pending |

Do not put credentials, access tokens, purchased files, or personal-record extracts in this repository. Save the agency's written response here only after removing signatures, phone numbers, and other unnecessary personal information.

## How to record a response

1. Enter the sent and response dates in the tracker.
2. Summarize the answer in the matching county file. Preserve a link or message identifier outside the repository if the original contains personal information.
3. Record every condition: permitted purpose, frequency, rate limits, retention, attribution, redistribution, cost, authentication, and revocation procedure.
4. Update `automation-source-registry.json` only after the written answer resolves the corresponding hold.
5. Keep `enabled` set to `false` until the full approval checklist is complete.

Official routes and source details verified 2026-08-13.
