# Nike (NKE) Five-Year Valuation — Start

## Question

What are five years of Nike's statements worth, built from assumptions I can defend?

## Base-case inputs

| Input | Base case | Type |
|---|---:|---|
| Starting FCFF | $2,441.4m | Course case input |
| FCFF growth, FY2027E–FY2031E | 8%, 6%, 5%, 4%, 3% | Forecast judgment |
| WACC | 10.0% | Valuation judgment |
| Terminal growth | 3.0% | Long-run judgment |
| Cash | $9,027m | Course case input |
| Debt | $7,942m | Course case input |
| Diluted shares | 1,481.0m | Course case input |

## Initial result

The starter DCF projects FCFF from $2,636.7m in FY2027E to $3,143.6m in FY2031E. Using the listed assumptions, it produces an enterprise value of $39,669.5m, equity value of $40,754.5m, and an implied value of **$27.52 per share**. Terminal value is 72.4% of enterprise value, so the result is especially sensitive to WACC and terminal growth.

This is a starting valuation, not a price target. The next build should replace the high-level FCFF growth forecast with linked revenue, margin, tax, reinvestment, and working-capital schedules.

## Information sources

1. The course repository's [`Nike.md`](Nike.md) supplied the base-case FCFF, growth, WACC, terminal-growth, cash, debt, and diluted-share inputs. Its locators identify Nike's FY2026 Form 10-K for the factual items and label WACC, terminal growth, and forecast growth as estimates.
2. NIKE's [FY2026 Form 10-K filed with the SEC](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm) is the primary-company source for FY2026 reported context. It reports $46.398bn of revenue, 42.9% gross margin, $3.850bn EBIT, and $3.108bn net income for the year ended May 31, 2026.

## Assumptions to defend in discussion

- The 8% to 3% growth fade assumes an initial recovery followed by mature-company growth.
- A 10% WACC is a judgment about the required return; changing it materially changes terminal value.
- A 3% terminal-growth rate should not exceed a sustainable long-run nominal economic growth rate.

## Part 1: three-year history grid

All figures are USD millions. “SG&A” is NIKE's reported **total selling and administrative expense** (demand creation plus operating overhead), which is the closest filing label to the requested line.

| Line | FY2026 | FY2025 | FY2024 |
|---|---:|---:|---:|
| Revenue | 46,398 ([FY2026 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm)) | 46,309 ([FY2025 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm)) | 51,362 ([FY2024 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018724000044/nke-20240531.htm)) |
| Gross profit | 19,911 ([FY2026 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm)) | 19,790 ([FY2025 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm)) | 22,887 ([FY2024 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018724000044/nke-20240531.htm)) |
| SG&A | 16,114 ([FY2026 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm)) | 16,088 ([FY2025 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm)) | 16,576 ([FY2024 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018724000044/nke-20240531.htm)) |
| Net income | 3,108 ([FY2026 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm)) | 3,219 ([FY2025 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm)) | 5,700 ([FY2024 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018724000044/nke-20240531.htm)) |
| Inventory, ending | 7,501 ([FY2026 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm)) | 7,489 ([FY2025 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm)) | 7,519 ([FY2024 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018724000044/nke-20240531.htm)) |
| PP&E, net, ending | 4,796 ([FY2026 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm)) | 4,828 ([FY2025 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm)) | 5,000 ([FY2024 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018724000044/nke-20240531.htm)) |
| Shareholders’ equity, ending | 14,865 ([FY2026 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm)) | 13,213 ([FY2025 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm)) | 14,430 ([FY2024 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018724000044/nke-20240531.htm)) |

Manual spot checks completed against the primary filings: FY2026 revenue is $46,398m and FY2024 additions to PP&E (capex) are $812m. The filings’ audited statements corroborate the history grid.

## Opening balance sheet for the Nike statement model

FY2026 is the opening balance sheet for the forecast. Figures are USD millions and come from NIKE's FY2026 Form 10-K.

| Assets | FY2026 | Liabilities and shareholders’ equity | FY2026 |
|---|---:|---|---:|
| Cash and equivalents | 7,563 | Current portion of long-term debt | 2,000 |
| Short-term investments | 1,464 | Accounts payable | 3,600 |
| Accounts receivable, net | 5,931 | Current lease liabilities | 478 |
| Inventories | 7,501 | Accrued liabilities | 6,092 |
| Prepaid and other current assets | 2,144 | Income taxes payable | 377 |
| PP&E, net | 4,796 | Long-term debt | 5,942 |
| Operating lease ROU assets | 2,838 | Long-term lease liabilities | 2,613 |
| Identifiable intangibles | 259 | Deferred taxes and other liabilities | 2,443 |
| Goodwill | 240 | Shareholders’ equity | 14,865 |
| Deferred taxes and other assets | 5,674 |  |  |
| **Total assets** | **38,410** | **Total liabilities and equity** | **38,410** |

Model reconciliation: the DCF’s $9,027m “cash” input equals $7,563m cash and equivalents plus $1,464m short-term investments. Total debt is $7,942m ($2,000m current plus $5,942m long-term). For a three-statement build, cash and short-term investments should remain separate unless the model explicitly treats short-term investments as excess cash.

## Ratios and growth history

| Ratio / line | FY2026 | FY2025 | FY2024 | Calculation or filing field |
|---|---:|---:|---:|---|
| Gross margin | 42.9% | 42.7% | 44.6% | Gross profit ÷ revenue |
| SG&A ÷ gross profit | 80.9% | 81.3% | 72.4% | Total selling and administrative expense ÷ gross profit |
| Inventory days | 103.4 | 103.1 | 96.4 | Ending inventory ÷ cost of sales × 365 |
| Depreciation ÷ PP&E | 15.6% | 16.1% | 15.9% | Depreciation and amortization ÷ ending PP&E |
| Capital spending, filing | 684 | 430 | 812 | “Additions to property, plant and equipment” in cash flows |
| Capital spending, data-provider field | unresolved | unresolved | unresolved | No data-provider export was provided; do not substitute a third-party value for the filing line. |
| Effective tax rate | 20.3% | 17.1% | 14.9% | Income tax expense ÷ income before income taxes |
| Reported revenue growth | 0.2% | (9.8%) | 0.3% | Current-year revenue ÷ prior-year revenue − 1 |
| Organic / same-store growth | None disclosed | None disclosed | None disclosed | NIKE’s consolidated 10-K does not disclose a companywide same-store or organic-sales metric. It discusses currency-neutral revenue instead; that is not the same measure. |

## Assumption set for the next statement build

| Value | Label | Reason |
|---|---|---|
| FY2026 revenue $46,398m | history | Latest audited operating base. |
| 42.9% gross margin | history | Latest reported margin; it is a transparent base before setting a forecast path. |
| 80.9% SG&A ÷ gross profit | history | Latest reported cost structure, using NIKE’s total selling and administrative expense. |
| 103.4 inventory days | history | Latest year-end inventory conversion implied by the filing. |
| 15.6% depreciation ÷ PP&E | history | Latest filing-based relationship, subject to refinement with a gross-PP&E schedule. |
| $684m capital spending | history | Latest cash-flow statement capex field. |
| 20.3% tax rate | history | Latest effective tax rate; it is a starting point, not a statutory-rate claim. |
| Floor plan: none | none | NIKE does not report an auto-dealer-style floor-plan financing line; do not invent one. |
| Revenue growth: 8%, 6%, 5%, 4%, 3% | judgment | A fading path reflects an initial recovery assumption followed by mature-company growth. |
| WACC: 10.0% | judgment | This is the course base case for the return demanded by capital providers; it needs sensitivity analysis. |
| Terminal growth: 3.0% | judgment | A conservative long-run nominal-growth assumption, below the 10% discount rate. |

NIKE reported positive net income in all three history years. There are therefore no historical “negative FCFE” years to flag in this start. 

## Final model check block and market comparison

`nike_proforma.py` is the completed five-year statement model. It projects FY2027E–FY2031E, prints all three statements, and calls `assert_balanced` annually before calculating valuation.

| Check | FY2027E | FY2028E | FY2029E | FY2030E | FY2031E |
|---|---:|---:|---:|---:|---:|
| Assets − liabilities − equity | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Year-end cash | 9,256.7 | 11,266.0 | 13,506.2 | 15,962.6 | 18,614.6 |
| Cash at or above $1,000m floor | Yes | Yes | Yes | Yes | Yes |
| Revolver draw | None | None | None | None | None |

No year draws the revolver because forecast FCFE, net of the $150m annual buyback, keeps cash above the $1,000m cash floor.

The model says **$23.94 per share**, while NKE traded at **$35.93 per share on September 24, 2026** (intraday), using the same 1,481.0m diluted-share count; the question is what stronger future cash flow, margins, or risk profile the market price is embedding. [Market-price source](https://ca.investing.com/equities/nike-historical-data)

## Complete source list

- Course case inputs: [Nike.md](Nike.md)
- NIKE, Inc. FY2026 Form 10-K (year ended May 31, 2026): [SEC filing](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm)
- NIKE, Inc. FY2025 Form 10-K (year ended May 31, 2025): [SEC filing](https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm)
- NIKE, Inc. FY2024 Form 10-K (year ended May 31, 2024): [SEC filing](https://www.sec.gov/Archives/edgar/data/320187/000032018724000044/nke-20240531.htm)
- NKE market price on September 24, 2026: [Investing.com historical-data page](https://ca.investing.com/equities/nike-historical-data)
