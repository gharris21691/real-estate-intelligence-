# GIS and Open Data

- Research status: `Verified`
- Pilot status: `Candidate — field-level approval required`
- Verified: 2026-08-12
- Owning agency: Sacramento County GIS / Assessor source data

## Official sources

- [County ArcGIS REST directory](https://mapservices.gis.saccounty.gov/arcgis/rest/services)
- [PARCELS MapServer](https://mapservices.gis.saccounty.gov/arcgis/rest/services/PARCELS/MapServer)
- [Active GIS Parcel Base](https://mapservices.gis.saccounty.gov/arcgis/rest/services/PARCELS/MapServer/8)
- [ASSESSOR MapServer](https://mapservices.gis.saccounty.gov/arcgis/rest/services/ASSESSOR/MapServer)
- [Parcel Viewer disclaimer](https://assessor.saccounty.gov/us/en/maps-property-data-and-records/data-disclaimer-and-instructions-parcel-viewer.html)

## Verified access profile

| Field | Finding |
| --- | --- |
| Service | The REST directory exposes a `PARCELS` MapServer with active, transitional, obsolete, multilevel, and all-parcel layers. |
| Candidate layer | `Active GIS Parcel Base` (layer 8) is a polygon feature layer. |
| Access method | ArcGIS REST queries over HTTPS; the layer advertises pagination, statistics, ordering, and distinct values. |
| Authentication | Layer metadata and query endpoints were publicly readable without a token during verification. |
| Query formats | JSON, GeoJSON, and PBF. |
| Service limit | `maxRecordCount` is 2,000 per response; pagination is supported. |
| Spatial reference | WKID 102642 / 2226, feet. |
| Identifiers | `PARCEL_NUMBER` (length 14), `APN_DASH`, `APN10`, `PRCL_KEY`, status/type, and geometry. |
| Additional schema | Published fields include situs, jurisdiction, land use, lot size, document references, dates, owner/name, and mailing fields. |
| Cadence | Date fields and a Return Updates operation exist, but no authoritative refresh commitment was found. |
| Fitness | Parcel maps are for assessment purposes, may not match legal descriptions, and are provided as-is. |

## Privacy and governance conflict

The Assessor says owner information is not available through Parcel Viewer because of privacy concerns, while the public REST schema advertises owner and mailing fields. Do not retrieve or store those fields until the County confirms that they are intentionally public for this use and provides field-level terms. Technical availability is not approval.

## Risks and limitations

- No license, redistribution grant, uptime commitment, or refresh SLA was published on the service page.
- ArcGIS metadata says `Can Modify Layer: true`; this project must never attempt writes to a source system.
- Active, all, obsolete, and transitional parcels have different semantics.
- Parcel geometry is an assessment reference, not a legal survey.

## Evidence log

| Checked | Official page/document | Claim supported |
| --- | --- | --- |
| 2026-08-12 | [REST Directory](https://mapservices.gis.saccounty.gov/arcgis/rest/services) | Official catalog and PARCELS/ASSESSOR services |
| 2026-08-12 | [PARCELS MapServer](https://mapservices.gis.saccounty.gov/arcgis/rest/services/PARCELS/MapServer) | Layer families, service limit, formats, and spatial reference |
| 2026-08-12 | [Active Parcel Layer](https://mapservices.gis.saccounty.gov/arcgis/rest/services/PARCELS/MapServer/8) | Query capabilities and field schema |
| 2026-08-12 | [Parcel Disclaimer](https://assessor.saccounty.gov/us/en/maps-property-data-and-records/data-disclaimer-and-instructions-parcel-viewer.html) | As-is status and boundary limitation |

## Recommendation and next action

Treat geometry plus a minimal APN/status field set as a leading technical pilot candidate. Ask GIS and the Assessor to confirm automated access, approved fields, cadence, license, redistribution, and whether file delivery is preferred. Exclude owner and mailing fields unless explicitly approved.
