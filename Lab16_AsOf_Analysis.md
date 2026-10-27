# Lab 16 - As-Of Data Analysis

## Question

On the decision date, what information was actually knowable, and how much of the data visible later was not yet published?

Decision date: **31 March 2026**. A row is eligible for the as-of panel only if it was published on or before that date.

## Training data

| Row | Ticker | Month measured | Published on | Index |
|---:|---|---|---|---:|
| 1 | AAA | 2026-01 | 2026-02-10 | 101.0 |
| 2 | AAA | 2026-02 | 2026-03-10 | 104.0 |
| 3 | AAA | 2026-03 | 2026-04-10 | 109.0 |
| 4 | AAA | 2026-02 | 2026-03-25 | 103.0 |
| 5 | BBB | 2026-01 | 2026-02-10 | 98.0 |
| 6 | BBB | 2026-02 | 2026-03-10 | 97.0 |
| 7 | BBB | 2026-02 | 2026-03-10 | 97.0 |
| 8 | BBB | 2026-03 | 2026-04-10 | 92.0 |
| 9 | CCC | 2026-01 | 2026-02-10 | 110.0 |
| 10 | CCC | 2026-02 | 2026-04-05 | 112.0 |
| 11 |  | 2026-02 | 2026-03-10 | 99.0 |
| 12 | CCC | 2026-02 | 2026-03-10 | 111.0 |

## As-of filter rules

The script applies the following rules in order:

1. Quarantine a row with no ticker.
2. Remove an exact duplicate.
3. Remove a row published after the decision date.
4. When a ticker-month has multiple publications, retain the latest publication that was available by the decision date.

## Row funnel

| Funnel step | Rows removed |
|---|---|
| Quarantined: no ticker | 11 |
| Exact duplicate | 7 |
| Published after 31 March 2026 | 3, 8, 10 |
| Older vintage replaced by a revision | 2 |

## As-of panel

| Row | Ticker | Month measured | Published on | Index |
|---:|---|---|---|---:|
| 1 | AAA | 2026-01 | 2026-02-10 | 101.0 |
| 4 | AAA | 2026-02 | 2026-03-25 | 103.0 |
| 5 | BBB | 2026-01 | 2026-02-10 | 98.0 |
| 6 | BBB | 2026-02 | 2026-03-10 | 97.0 |
| 9 | CCC | 2026-01 | 2026-02-10 | 110.0 |
| 12 | CCC | 2026-02 | 2026-03-10 | 111.0 |

## Signals

The signal is the percentage change from the previous measured month to the latest measured month available in each panel.

| Ticker | As-of signal | Naive signal using later publications |
|---|---:|---:|
| AAA | +1.98% (February) | +5.83% (March) |
| BBB | -1.02% (February) | -5.15% (March) |
| CCC | +0.91% (February) | +1.82% (February, revised) |

## Interpretation

On 31 March 2026, March data for AAA and BBB had not been published, and the later CCC February revision had not been published. A naive analysis using every later publication therefore uses information that was unavailable on the decision date. The difference between the as-of and naive columns is the look-ahead information that would have distorted a real-time decision.

The AAA revision illustrates why rule 4 matters. February's first publication was 104.0 (row 2), but the latest knowable February publication was 103.0 (row 4). Keeping row 2 would incorrectly produce a +2.97% as-of signal instead of +1.98%.

## Implementation

The standard-library implementation is in [asof.py](asof.py). It contains reusable functions for each filter, the as-of panel, the naive comparison panel, and signal calculation.

Run it from the repository folder:

```powershell
python asof.py
```

## Later-decision-date check

When the decision date is temporarily changed to 15 April 2026, all training rows have been published. The as-of signal values then equal the naive signal values ticker by ticker. The saved file uses the original 31 March 2026 decision date.

## AI use disclosure

I used AI and Codex to help format the analysis and organize the standard-library Python implementation. I reviewed the row filters, calculations, and output against the provided known answers.
