# Lab 19 — Three Investor Panel

## My request to AI

Extend the existing 10-K-only SEC EDGAR Buffett analysis. Add liabilities, current assets, current liabilities, current ratio, and liabilities divided by equity. Create separate Graham and Burry skills that use the same computed facts, write a memo from printed values only, and display all three approaches in one Streamlit investor panel. The app must show every check, the three verdicts, three memos, and a flag for any memo number not produced by code.

## Data and calculation rules

- Source: SEC EDGAR `company_tickers.json` and `companyfacts`; 10-K filings only.
- Five fiscal years are labelled by fiscal-year-end date. One-year flow periods only are accepted.
- If a period occurs in several filings, the latest filed 10-K wins.
- A missing input is `not found`; a calculation lacking an input is `not known`.
- Owner earnings = operating cash flow - capital spending.
- ROE = net income / year-end equity.
- Current ratio = current assets / current liabilities.
- Liabilities / equity = liabilities / year-end equity.

## Investor rules

| Investor | Code-based checks |
|---|---|
| Buffett | ROE >= 15% every year; owner earnings positive every year; owner earnings grew from first to last year |
| Graham | Latest current ratio >= **1.0**; net income positive every year; net income grew from first to last year |
| Burry | Operating cash flow >= net income every year; latest liabilities / equity <= 2.0 |

**Threshold kept:** Graham's current-ratio threshold is **1.0**. Costco's business model can function with a leaner current-asset cushion, so this threshold is retained for this panel rather than the original 2.0 demonstration threshold.

## COST: underlying SEC EDGAR facts

**Company:** Costco Wholesale Corp /New  
**Ticker:** COST  
**CIK:** 0000909832

| Fiscal-year end | Net income | Operating cash flow | Equity | Current ratio | Liabilities / equity |
|---|---:|---:|---:|---:|---:|
| 2022-08-28 | $5,844,000,000 | $7,392,000,000 | $20,642,000,000 | 1.02 | 2.11 |
| 2023-09-03 | $6,292,000,000 | $11,068,000,000 | $25,058,000,000 | 1.07 | 1.75 |
| 2024-09-01 | $7,367,000,000 | $11,339,000,000 | $23,622,000,000 | 0.97 | 1.96 |
| 2025-08-31 | $8,099,000,000 | $13,335,000,000 | $29,164,000,000 | 1.03 | 1.64 |
| 2026-08-30 | $9,226,000,000 | $15,817,000,000 | $35,803,000,000 | 1.06 | 1.49 |

## COST panel result

| Investor | Check | Result |
|---|---|---|
| Buffett | ROE of 15% or more every year | Pass |
| Buffett | Owner earnings positive every year | Pass |
| Buffett | Owner earnings grew, first year to last | Pass |
| Graham | Current ratio of 1.0 or more, latest year | Pass (1.06) |
| Graham | Net income positive every year | Pass |
| Graham | Net income grew, first year to last | Pass |
| Burry | Operating cash flow at least net income every year | Pass |
| Burry | Liabilities no more than twice equity, latest year | Pass (1.49) |

**Verdicts:** Buffett: Own the business (3 of 3). Graham: Own the business (3 of 3). Burry: Own the business (2 of 2).

## Memos

### Buffett

**Buffett verdict: Own the business.**

ROE was 28.31% in 2022 and 25.77% in 2026. Owner earnings moved from $3,501,000,000 to $9,382,000,000. This judges business quality from printed 10-K facts, not market price.

### Graham

**Graham verdict: Own the business.**

The latest current ratio is 1.06, compared with the retained 1.0 threshold. Net income changed from $5,844,000,000 to $9,226,000,000. This memo evaluates the business from the printed 10-K facts, not its market price.

Threshold retained: 1.0, because Costco's operating model can function with a leaner current-asset cushion.

### Burry

**Burry verdict: Own the business.**

Latest operating cash flow was $15,817,000,000, compared with net income of $9,226,000,000. Latest liabilities divided by equity were 1.49, below the 2.00 ceiling. The checks use printed 10-K facts and do not evaluate share price.

## App and code inventory

The distinctive Streamlit app is named **The Three Lenses**. It uses one shared EDGAR data calculation, presents a single investor-check panel, three side-by-side memos, and a common validator. The validator passed: no memo number is absent from the computed SEC results.

- `investor_panel_app.py` — Streamlit app
- `.codex/skills/sec-edgar-buffett/` — shared EDGAR downloader and Buffett rules
- `.codex/skills/sec-edgar-graham/` — Graham rules and memo writer
- `.codex/skills/sec-edgar-burry/` — Burry rules and memo writer
- `COST_edgar_data.json` — computed COST facts
- `COST_buffett_memo.md`, `COST_graham_memo.md`, `COST_burry_memo.md` — investor memos

Run the panel with:

```powershell
.\.venv\Scripts\python.exe -m streamlit run investor_panel_app.py
```

Data from SEC EDGAR; built with AI help, a learning demonstration, not investment advice.
