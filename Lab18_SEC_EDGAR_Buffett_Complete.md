# Lab 18 — SEC EDGAR Buffett Skill: Complete Submission

## Question

Can an investor's philosophy become a skill an AI runs the same way every time, with numbers computed from the 10-K and judgment made by the model?

Yes, if the philosophy is converted into explicit, auditable rules. This submission separates repeatable code-based calculations from a short model-written business-quality judgment.

## My request to AI

Build a reusable skill called `sec-edgar-buffett` that analyzes a U.S. public company from SEC EDGAR 10-K facts only. Use the SEC ticker-to-CIK JSON and companyfacts API, do not use paid data or price data, and require a caller-supplied name-and-email User-Agent.

For the latest five fiscal years, calculate revenue, net income, operating cash flow, capital spending, equity, ROE, and owner earnings. Use annual flow periods only, select the latest filed 10-K when the same period appears more than once, and print `not found` rather than estimating a missing input. Calculate ROE as net income divided by year-end equity and owner earnings as operating cash flow minus capital spending. A missing, zero, or negative equity value makes ROE `not known`.

Check whether ROE was at least 15% every year, owner earnings were positive every year, and owner earnings grew from the first year to the last. A check with a missing input is `not known`. Create a short Buffett-style memo using only script-produced values and conclude **own the business**, **watch it**, or **pass**. The app must chart owner earnings and net income, show results and checks, show the memo, and flag memo numbers that the script did not print.

## Reusable skill

**Location:** `.codex/skills/sec-edgar-buffett/`

**When to use it:** A 10-K-only, filing-based business-quality analysis of a U.S. public company. It is not used for stock-price valuation.

### Rules implemented in the script

| Item | Rule |
|---|---|
| SEC sources | `https://www.sec.gov/files/company_tickers.json` and `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json` |
| Filings | 10-K only; latest five fiscal-year-end dates |
| Annual flows | A period from 330 to 380 days |
| Duplicate periods | Latest filed 10-K wins |
| Revenue tag | `RevenueFromContractWithCustomerExcludingAssessedTax`, then `Revenues` |
| Net-income tag | `NetIncomeLoss` |
| Operating-cash-flow tag | `NetCashProvidedByUsedInOperatingActivities` |
| Capital-spending tag | `PaymentsToAcquirePropertyPlantAndEquipment`, then `PaymentsToAcquireProductiveAssets` |
| Equity tag | `StockholdersEquity` |
| Owner earnings | Operating cash flow minus capital spending |
| ROE | Net income divided by year-end equity |
| Missing data | `not found`; no estimate is made |
| Missing/nonpositive equity | ROE is `not known` |

The script requires a real, caller-provided SEC User-Agent. It does not store the User-Agent in code, the data file, or this document.

## COST: SEC EDGAR result

**Company:** Costco Wholesale Corp /New  
**Ticker:** COST  
**CIK:** 0000909832  
**Source:** SEC EDGAR companyfacts, 10-K only

### XBRL tags used

| Metric | XBRL tag |
|---|---|
| Revenue | `RevenueFromContractWithCustomerExcludingAssessedTax` |
| Net income | `NetIncomeLoss` |
| Operating cash flow | `NetCashProvidedByUsedInOperatingActivities` |
| Capital spending | `PaymentsToAcquirePropertyPlantAndEquipment` |
| Equity | `StockholdersEquity` |

### Five fiscal years

| Fiscal-year end | Revenue | Net income | Operating cash flow | Capital spending | Equity | ROE | Owner earnings |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2022-08-28 | $226,954,000,000 | $5,844,000,000 | $7,392,000,000 | $3,891,000,000 | $20,642,000,000 | 28.31% | $3,501,000,000 |
| 2023-09-03 | $242,290,000,000 | $6,292,000,000 | $11,068,000,000 | $4,323,000,000 | $25,058,000,000 | 25.11% | $6,745,000,000 |
| 2024-09-01 | $254,453,000,000 | $7,367,000,000 | $11,339,000,000 | $4,710,000,000 | $23,622,000,000 | 31.19% | $6,629,000,000 |
| 2025-08-31 | $275,235,000,000 | $8,099,000,000 | $13,335,000,000 | $5,498,000,000 | $29,164,000,000 | 27.77% | $7,837,000,000 |
| 2026-08-30 | $303,154,000,000 | $9,226,000,000 | $15,817,000,000 | $6,435,000,000 | $35,803,000,000 | 25.77% | $9,382,000,000 |

### Buffett checks

| Check | Result |
|---|---|
| ROE at least 15% every year | Pass |
| Owner earnings positive every year | Pass |
| Owner earnings grew, first year to last | Pass |

## Costco Buffett-style memo

**Decision: Own the business.**

Costco passed all three business-quality checks. ROE remained above the 15% threshold in every reported fiscal year, including 28.31% in 2022 and 25.77% in 2026. Owner earnings were positive each year and increased from $3,501,000,000 in 2022 to $9,382,000,000 in 2026.

The business also showed stronger reported net income, rising from $5,844,000,000 in 2022 to $9,226,000,000 in 2026. Based only on these operating results, Costco demonstrates consistent profitability and growing owner earnings. This conclusion evaluates business quality, not the stock price.

## Streamlit app

The app is `buffett_app.py`. It imports the reusable skill script rather than copying the calculation logic. For a ticker, it:

- Downloads public 10-K facts from SEC EDGAR using a one-session User-Agent entered in the sidebar.
- Charts owner earnings and net income over the five fiscal years.
- Displays the computed table, selected XBRL tags, and three Buffett checks.
- Displays the ticker's markdown memo.
- Flags every numeric token in the memo that was not printed by the script.
- States: "Data from SEC EDGAR; built with AI help, a learning demonstration, not investment advice."

Run it with:

```powershell
.\.venv\Scripts\python.exe -m streamlit run buffett_app.py
```

## Included project files

The code and machine-readable output remain separate so the app can run, but all work is summarized in this document.

- [AI request](Lab18_Buffett_Skill_Request.md)
- [Skill instructions](../.codex/skills/sec-edgar-buffett/SKILL.md)
- [SEC EDGAR script](../.codex/skills/sec-edgar-buffett/scripts/sec_buffett.py)
- [Streamlit app](buffett_app.py)
- [COST computed data](COST_edgar_data.json)
- [COST memo](COST_buffett_memo.md)

Built with AI help, a learning demonstration, not investment advice.
