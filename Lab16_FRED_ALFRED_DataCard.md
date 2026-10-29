# Lab 16 — FRED/ALFRED As-Of Data Card

## Purpose

This app separates the date an observation measures from the date it was available. FRED provides the current series; ALFRED provides the series vintage available on the selected **As known on** date. The comparison prevents using revisions or later publications in an earlier decision.

Run the app with:

```powershell
.\.venv\Scripts\python.exe -m streamlit run asof_app.py
```

## Known-answer check

With **As known on = 5 October 2026**, the app should show the following last values known then:

| Series | Last date known | Value |
|---|---|---:|
| BAA | September 2026 | 6.47 |
| FEDFUNDS | September 2026 | 3.75 |
| DGS10 | 2 October 2026 | 5.28 |
| MORTGAGE30US | 1 October 2026 | 7.28 |

**PAYEMS probe:** Add `PAYEMS` and set **As known on** to 15 January 2025. The last known observation should be December 2024 at **159,536** (thousands). Today's December 2024 value should be lower and the same-date revised count should be well above zero. That difference is revision history, not a trading signal.

## Data cards

**Download date:** 29 October 2026. Current observations come from [FRED](https://fred.stlouisfed.org/); vintage observations come from [ALFRED](https://alfred.stlouisfed.org/). The app requests one current CSV and one vintage CSV per selected series.

| ID | What it measures | Units / frequency | Typical availability | Revisions |
|---|---|---|---|---|
| [BAA](https://fred.stlouisfed.org/series/BAA) | Moody's seasoned Baa corporate-bond yield (long maturities). | Percent; monthly; not seasonally adjusted. | September 2026 was posted 1 October 2026, so the monthly observation was available just after month-end. | Yes in principle: FRED warns its data can be revised; the app measures actual changes. |
| [FEDFUNDS](https://fred.stlouisfed.org/series/FEDFUNDS) | Effective rate on overnight federal-funds transactions. | Percent; monthly average of daily figures; not seasonally adjusted. | September 2026 was posted 1 October 2026. | Yes in principle; the app counts changed values on identical dates. |
| [DGS10](https://fred.stlouisfed.org/series/DGS10) | 10-year U.S. Treasury constant-maturity yield. | Percent; daily; not seasonally adjusted. | Normally available with roughly a one-business-day lag. | Yes in principle, but typically few changes; verify with the app's same-date count. |
| [MORTGAGE30US](https://fred.stlouisfed.org/series/MORTGAGE30US) | Average U.S. 30-year fixed mortgage rate from Freddie Mac's survey. | Percent; weekly, ending Thursday; not seasonally adjusted. | Generally released on the Thursday of the week measured. | Yes in principle; compare with its ALFRED vintage. |
| [PAYEMS](https://fred.stlouisfed.org/series/PAYEMS) | Total nonfarm payroll employment. | Thousands of persons; monthly; seasonally adjusted. | Normally released on the first Friday after the measured month. | Yes; benchmark and other revisions can change history. The 15 January 2025 probe demonstrates this. |

## Three values checked on the FRED pages

On the download date, the current FRED pages displayed:

| Series | Latest displayed observation | Value |
|---|---|---:|
| BAA | September 2026 | 6.47% |
| FEDFUNDS | September 2026 | 3.75% |
| DGS10 | 27 October 2026 | 4.99% |

## Interpretation

Daily market-rate series such as DGS10 should have little publication lag and generally few revisions compared with a monthly economic series such as PAYEMS. A row that is absent from an earlier vintage was not known at that time; it must not be used for an as-of decision.

Built with AI help, as a learning demonstration, not investment advice.
