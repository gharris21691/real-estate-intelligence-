# California Expansion Shortlist — August 2026

## Decision

After Sacramento, research **Kern, San Bernardino, Fresno, and Stanislaus** as the first statewide expansion wave. Research **Yolo and Placer** as a Sacramento-adjacent wave. Keep **Riverside** as the next Southern California companion county once San Bernardino's source path is understood.

This is a source-research priority, not an authorization to collect data. Each county must still pass the repository's source, legal, privacy, cost, and quality gates before any pilot or automation.

## Why “hot” is not one metric

For a wholesaling-oriented workflow, the hottest seller market is not automatically the best operating market. Fast sales and rising prices can support disposition, but higher inventory, longer marketing times, and price softness may create more motivated-seller conversations. The practical target is a balance of:

1. reachable acquisition prices;
2. enough transaction activity to support buyers and comparable sales;
3. signs of seller negotiation room;
4. official parcel, assessment, tax, and recorder access;
5. a repeatable county-level operating footprint.

The market screen below uses the California Association of Realtors' May 2026 existing single-family-home report. Monthly county figures can be volatile, especially in small counties, so this is a current screen rather than a long-term forecast.

## Market screen

| Priority | County | Example places | May 2026 median | Sales YoY | Inventory index | Median market time | Interpretation |
| ---: | --- | --- | ---: | ---: | ---: | ---: | --- |
| 1 | Kern | Bakersfield, Delano, Ridgecrest | $412,000 | +5.3% | 3.3 | 26 days | Best current balance of affordability, positive sales activity, and a documented county data path. |
| 2 | San Bernardino | San Bernardino, Fontana, Rialto, Victorville, Hesperia | $486,410 | -3.9% | 5.1 | 30 days | Not a “hot” seller market, but more inventory and unusually useful official data make it a strong motivated-seller research market. |
| 3 | Fresno | Fresno, Clovis, Sanger, Selma | $435,000 | +6.6% | 3.8 | 21 days | Affordable relative to the state, with positive sales growth and public parcel/zoning GIS. |
| 4 | Stanislaus | Modesto, Ceres, Turlock, Oakdale | $490,000 | +1.6% | 3.0 | 19.5 days | Affordable, steady, and supported by free parcel geometry plus defined paid assessment and sales products. |
| 5 | Yolo | Woodland, West Sacramento, Davis, Winters | $685,000 | +15.7% | 2.7 | 25.5 days | Strongest current sales momentum near Sacramento and a queryable parcel feature service, but higher prices and explicit recorder automation restrictions limit the initial use case. |
| 6 | Placer | Roseville, Rocklin, Lincoln, Auburn | $685,000 | +5.9% | 3.0 | 22 days | Strong adjacent market and easy operational extension from Sacramento; higher prices and incomplete bulk-source verification lower its first-wave priority. |
| 7 | Riverside | Riverside, Moreno Valley, Perris, Hemet, Indio | $640,000 | -2.2% | 3.9 | 37 days | Large Inland Empire opportunity with useful open parcel data; pair it with San Bernardino after source terms are verified. |
| Watch | San Joaquin | Stockton, Manteca, Lodi, Tracy | $550,000 | -20.7% | 4.5 | 27 days | Close to Sacramento and potentially motivated, but the sharp one-month sales decline and paid bulk products justify a watchlist rather than immediate expansion. |

Source: [California Association of Realtors, May 2026 County Sales, Price, Inventory, and Market Time](https://www.car.org/aboutus/mediacenter/newsreleases/2026releases/may2026sales), verified 2026-08-12.

## Official-record feasibility

### Kern County — first research target

- The Assessor publishes a live property search, parcel-map search, property-tax portal, and official-record index from its [property and records hub](https://www.kerncounty.com/services/property-land-and-taxes).
- Its [GIS data documentation](https://www.kerncounty.com/government/departments/assessor-recorder/property/mapping-gis/gis-data) describes parcel geometry, tax-roll tables, ownership/assessee names, use codes, assessed values, and parcel history. A complete edition is currently listed at $220; ordering and reuse terms require confirmation.
- The public mapping stack exposes an ArcGIS REST parcel service, while the bulk dataset is a paid snapshot. These should be evaluated as separate sources.
- The [official-record search](https://www.kerncounty.com/government/departments/assessor-recorder/records/search-for-recorded-documents-or-maps) supports grantor/grantee, document number, date, class, and recorded-map searches. Online APN searching was removed in December 2024.

**Research conclusion:** strongest balanced candidate. Verify the public REST service's allowed use, bulk-product license, current edition cadence, recorder interface restrictions, and whether tax-delinquency data is available in a reusable format.

### San Bernardino County — strongest bulk-data candidate

- The Assessor's [property-information page](https://arc.sbcounty.gov/property-information/) publishes annual secured-roll files, property-characteristic files, owner-transfer dates, and monthly owner files, alongside parcel maps and an interactive property application.
- The Auditor-Controller/Treasurer/Tax Collector operates an [open-data portal](https://opendata.sbcountyatc.gov/) with property-tax categories and developer/API access.
- The Recorder provides an [online official-record index](https://arc.sbcounty.gov/official-records/) from 1925 to the present. It is an index only; document images are not freely viewable online, though copies can be ordered.

**Research conclusion:** best official bulk-data posture in the shortlist, but current market conditions are softer. Treat that as a lead-generation hypothesis to test, not proof of distress.

### Fresno County — strong market, partial source path

- Fresno County states that its [GIS program](https://www.fresnocountyca.gov/Departments/Public-Works-and-Planning/divisions-of-public-works-and-planning/cds) provides parcel numbers, street addresses, zoning, and flood-zone information.
- Parcel ownership must be obtained from the Assessor rather than the GIS program.
- Recorder index availability, bulk assessment products, tax-delinquency access, and automation terms still need a full official-source review.

**Research conclusion:** strong market candidate, but source feasibility is only partially screened. Complete the Recorder, Assessor, and Tax Collector worksheets before ranking it above San Bernardino.

### Stanislaus County — clear paid/free split

- The Assessor's [assessment-data page](https://www.stancounty.com/assessor/AssessorDataSubscriptions.shtm) identifies free APN-based inquiry and downloadable GIS parcel shapes.
- Paid products include a $220 annual secured roll with monthly parcel/owner updates and a $350 cumulative-sales product with monthly updates; the page also documents higher-cost property-characteristic products.
- The Clerk-Recorder provides an [online RecorderWorks index](https://crweb.stancounty.com/RecorderWorksInternet/?ln=en).

**Research conclusion:** operationally promising because the source packages and costs are explicit. Verify resale/use restrictions, registration eligibility, field layouts, and whether the cumulative-sales product is needed for the first pilot.

### Yolo County — adjacent, useful GIS, restricted recorder automation

- Yolo exposes a queryable [public parcel feature layer](https://gis.yolocounty.gov/ext/rest/services/Public/Parcels_Public/FeatureServer/0) supporting JSON and GeoJSON queries.
- The Assessor says the roll and ownership data are available mainly at public terminals or by limited phone inquiry; [property characteristics](https://assessor.yolocounty.gov/191/Whats-Available) are fee-based.
- The [official-record index](https://ace.yolocounty.gov/222/Official-Records-Search) expressly prohibits automated, scripted, unattended, robotic, mining, or scraping access.

**Research conclusion:** good for parcel geography and manual validation, not an automated recorder-index pilot. Do not automate the recorder portal.

### Placer County — adjacent market, incomplete source verification

- The Assessor publishes a GIS-based parcel index and parcel-map workflow, documented in its [Assessor Index Map guide](https://www.placer.ca.gov/DocumentCenter/View/83331).
- The Clerk-Recorder offers official-record copies, but the current index, bulk availability, reuse terms, and machine-readable access have not yet been verified.

**Research conclusion:** prioritize after the first four counties unless geographic adjacency is more important than data maturity.

### Riverside County — Inland Empire companion

- Riverside County's [GIS Open Data portal](https://gis2.rivco.org/) lists countywide parcel products, including attributed and basic parcel data and Assessor tables.
- The Assessor-County Clerk-Recorder has published paid property-data products, including sales and recorder-index products, but current pricing, delivery, licensing, and field coverage require direct verification.

**Research conclusion:** research alongside San Bernardino to create an Inland Empire cluster, but do not assume the open GIS products include ownership or recorder events.

## Recommended next sequence

1. Create a full Kern County source-research folder using the Sacramento template.
2. In parallel only after that template is stable, create San Bernardino's source inventory, beginning with its published bulk files and tax open-data API.
3. Screen Fresno's Assessor, Recorder, and Tax Collector products to close the largest evidence gaps.
4. Price and license the Stanislaus secured-roll and cumulative-sales products.
5. Use Yolo and Placer for an adjacency track; keep Yolo's recorder index manual-only.
6. Add Riverside after San Bernardino so identifiers and workflows can be compared across the Inland Empire.

## Caveats

- These county figures describe completed market transactions, not off-market wholesaling outcomes or seller motivation.
- Positive sales growth can improve buyer liquidity but may reduce seller leverage; softer markets can create opportunities but increase disposition risk.
- City-level code enforcement, permits, utilities, and liens are often separate from county systems. Example cities identify operating clusters, not verified city source coverage.
- Public visibility does not grant permission for bulk collection, automation, resale, or commercial use.
- The market screen should be refreshed with at least three to six months of county data before committing budget.

Verified 2026-08-12.
