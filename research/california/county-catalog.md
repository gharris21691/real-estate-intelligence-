# California County Source Catalog

This catalog is the statewide research index. `Not started` means the county has not yet been evaluated; it does not mean records are unavailable. Sacramento is the first research county. The August 2026 expansion screen is documented in [`expansion-shortlist-2026-08.md`](expansion-shortlist-2026-08.md), and machine-readable candidates are tracked in [`automation-source-registry.json`](automation-source-registry.json).

| County | FIPS | Planning tier | Research status | County research path |
| --- | ---: | --- | --- | --- |
| Alameda | 001 | Later | Not started | — |
| Alpine | 003 | Later | Not started | — |
| Amador | 005 | Later | Not started | — |
| Butte | 007 | Later | Not started | — |
| Calaveras | 009 | Later | Not started | — |
| Colusa | 011 | Later | Not started | — |
| Contra Costa | 013 | Next | Not started | — |
| Del Norte | 015 | Later | Not started | — |
| El Dorado | 017 | Next | Not started | — |
| Fresno | 019 | Wave 1 | Automation screen complete | `expansion-shortlist-2026-08.md`; `automation-source-registry.json` |
| Glenn | 021 | Later | Not started | — |
| Humboldt | 023 | Later | Not started | — |
| Imperial | 025 | Later | Not started | — |
| Inyo | 027 | Later | Not started | — |
| Kern | 029 | Wave 1 | Automation screen complete; terms hold | `expansion-shortlist-2026-08.md`; `automation-source-registry.json` |
| Kings | 031 | Later | Not started | — |
| Lake | 033 | Later | Not started | — |
| Lassen | 035 | Later | Not started | — |
| Los Angeles | 037 | Next | Not started | — |
| Madera | 039 | Later | Not started | — |
| Marin | 041 | Later | Not started | — |
| Mariposa | 043 | Later | Not started | — |
| Mendocino | 045 | Later | Not started | — |
| Merced | 047 | Later | Not started | — |
| Modoc | 049 | Later | Not started | — |
| Mono | 051 | Later | Not started | — |
| Monterey | 053 | Later | Not started | — |
| Napa | 055 | Later | Not started | — |
| Nevada | 057 | Later | Not started | — |
| Orange | 059 | Next | Not started | — |
| Placer | 061 | Adjacent | Initial screen complete | `expansion-shortlist-2026-08.md` |
| Plumas | 063 | Later | Not started | — |
| Riverside | 065 | Wave 1 automation | Automation screen complete; approval pending | `expansion-shortlist-2026-08.md`; `automation-source-registry.json` |
| Sacramento | 067 | Pilot | Source inventory verified | `sacramento/` |
| San Benito | 069 | Later | Not started | — |
| San Bernardino | 071 | Wave 1 automation | Automation screen complete; license hold | `expansion-shortlist-2026-08.md`; `automation-source-registry.json` |
| San Diego | 073 | Next | Not started | — |
| San Francisco | 075 | Next | Not started | — |
| San Joaquin | 077 | Watch | Market screen complete | `expansion-shortlist-2026-08.md` |
| San Luis Obispo | 079 | Later | Not started | — |
| San Mateo | 081 | Next | Not started | — |
| Santa Barbara | 083 | Later | Not started | — |
| Santa Clara | 085 | Next | Not started | — |
| Santa Cruz | 087 | Later | Not started | — |
| Shasta | 089 | Later | Not started | — |
| Sierra | 091 | Later | Not started | — |
| Siskiyou | 093 | Later | Not started | — |
| Solano | 095 | Next | Not started | — |
| Sonoma | 097 | Next | Not started | — |
| Stanislaus | 099 | Wave 2 automation | Automation screen complete; purchase required | `expansion-shortlist-2026-08.md`; `automation-source-registry.json` |
| Sutter | 101 | Later | Not started | — |
| Tehama | 103 | Later | Not started | — |
| Trinity | 105 | Later | Not started | — |
| Tulare | 107 | Later | Not started | — |
| Tuolumne | 109 | Later | Not started | — |
| Ventura | 111 | Next | Not started | — |
| Yolo | 113 | Wave 1 geometry | Automation screen complete; Recorder manual-only | `expansion-shortlist-2026-08.md`; `automation-source-registry.json` |
| Yuba | 115 | Later | Not started | — |

## County source coverage template

Each county should track these source families independently: Recorder/Clerk, Assessor, Tax Collector/Treasurer, Superior Court, GIS/Open Data, county Code Enforcement, and major incorporated-city code-enforcement sources when county coverage is insufficient.

## Prioritization criteria

Planning tiers are provisional. Re-rank counties using documented business relevance, source accessibility, legal and policy constraints, acquisition cost, freshness, identifier compatibility, data quality, and reuse of an already-approved acquisition pattern.

`Initial screen complete` is less mature than `Verified`: it means official sources were identified for expansion planning, but a county-specific source specification and operating review have not yet been completed.

`Automation screen complete` means a machine-readable or recurring file path has been identified and documented. It does not authorize collection; the source registry remains disabled until its outstanding gates are resolved.
