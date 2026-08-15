# Sacramento Assessor land-use code references

- Status: `Received and reviewed`
- Received: 2026-08-13
- Storage: External encrypted/project data drive; originals are not stored in Git
- Record content: Reference definitions only; no parcel-level or personal records observed

## Files

| File | Description | Verification |
| --- | --- | --- |
| `36-11_B_Land Use Code Tables (JG-2023r) (SH-2023) (ES)(2).pdf` | Sacramento County Assessor Operations Manual, section 36-11B, 20 pages, effective April 2023 | SHA-256 `d5c13077e6fbb8eee12e5c4eb8c47c6e511487b8d8cd82ad1df5084b89672e6e` |
| `36-11_CX_Land Use Code Quick Reference.xlsx` | Quick-reference workbook with one populated worksheet (`Sheet1`, range `A1:H101`) and two blank worksheets | SHA-256 `43e3cec4fcd252f01142730cf031b0837019526ea284270bb81b9edd82f1dbeb` |

## Coverage

The manual documents six-position land-use codes and examples across these categories:

- residential;
- retail/commercial;
- office;
- personal care and health;
- church and welfare;
- recreational;
- industrial;
- agricultural;
- vacant;
- miscellaneous; and
- public and utilities.

The quick-reference workbook summarizes general and specific code patterns and subordinate values. It also marks the `Wxxxxx` public-and-utilities family as retired. The full manual should be treated as the primary interpretation reference because subordinate letters and digits have position-specific meanings that cannot always be read as independent code-description pairs.

## Remaining questions

- Confirm that the April 2023 manual is the current version applicable to the delivered secured roll.
- Identify the exact secured-roll column containing the land-use code and confirm its width and padding rules.
- Obtain separate definitions for parcel-status fields; these files cover land use, not parcel status.
- Preserve codes as strings so leading zeroes, positional characters, and placeholder patterns are not changed.

Reviewed 2026-08-13.
