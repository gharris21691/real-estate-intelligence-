# Tax Collector / Treasurer

- Research status: `Verified for manual lookup`
- Automation status: `Deferred — bulk access and terms unknown`
- Verified: 2026-08-12
- Owning agency: Sacramento County Department of Finance, Tax Collection and Licensing Division

## Official sources

- [Tax Collection and Business Licensing](https://finance.saccounty.gov/us/en/tax.html)
- [Property-tax FAQs](https://finance.saccounty.gov/us/en/tax/faqs.html)
- [Tax dates and bill information](https://finance.saccounty.gov/Tax/Pages/BillInfo.aspx)
- [Tax-sale information](https://finance.saccounty.gov/us/en/tax/tax/tax-sales.html)

## Verified access profile

| Field | Finding |
| --- | --- |
| Record scope | e-PropTax provides the most recent secured annual bill and direct levies, bills issued or due in the most recent fiscal year, prior-year delinquent secured amounts, and relevant supplemental, escaped, additional, and corrected real-property bills. |
| Exclusions | Prior-year delinquent unsecured real-property taxes and unsecured personal-property bills are not available in e-PropTax. |
| Access method | Public parcel lookup through e-PropTax; tax-sale information is published separately. |
| Search key | A 14-digit Assessor parcel number is required. |
| Fields described | Amounts, due dates, direct levies, tax rates, paid/unpaid detail, delinquent secured amounts, and printable payment stubs. |
| Historical depth | Current/recent bills plus prior-year delinquent secured amounts; complete historical depth is not published. |
| Cadence and lag | Annual secured bills issue by October; the prior bill remains until the new bill is issued. Payment posting may lag several business days. |
| Cost | Online lookup is presented without a fee. Staff-supplied copies incur a fee confirmed by the office. |
| Formats | Browser pages and printable stubs. No official data API or bulk export was identified. |

## Risks and limitations

- The portal is designed for parcel lookup and payment, not documented bulk acquisition.
- An unpaid state can lag payment processing and requires freshness/reconciliation rules.
- Supplemental, corrected, escaped, secured, and unsecured bills must remain distinct.
- A delinquency is not equivalent to a scheduled tax sale.

## Evidence log

| Checked | Official page/document | Claim supported |
| --- | --- | --- |
| 2026-08-12 | [Tax FAQs](https://finance.saccounty.gov/us/en/tax/faqs.html) | APN requirement, coverage, exclusions, annual transition, copies, and posting lag |
| 2026-08-12 | [Tax Division](https://finance.saccounty.gov/us/en/tax.html) | Owning division, e-PropTax, and tax-sale link |
| 2026-08-12 | [Tax Sales](https://finance.saccounty.gov/us/en/tax/tax/tax-sales.html) | Separate auction information and terms materials |

## Recommendation and next action

Use e-PropTax only for manual validation until the Tax Collector confirms whether a bulk status file or approved service exists. Request fields, history, refresh and correction behavior, cost, permitted uses, and rate limits. Do not automate the payment portal.
