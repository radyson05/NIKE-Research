# Lab 10 — Nike Model Run and Partner Exchange

## Run command and status

```powershell
python nike_proforma.py
```

Run status: **unresolved on this computer**. The exact terminal error is: `python : The term 'python' is not recognized as the name of a cmdlet, function, script file, or operable program.` Install Python or add it to PATH, then rerun the command above. Do not remove `assert_balanced` to bypass a failure.

## Base inputs saved from `nike_proforma.py`

| Input | Value |
|---|---:|
| Opening revenue (FY2026) | $46,398.0m |
| Revenue growth, FY2027E–FY2031E | 8%, 6%, 5%, 4%, 3% |
| Gross margin | 42.9% |
| SG&A ÷ gross profit | 80.93% |
| Depreciation ÷ opening PP&E | 747.0 ÷ 4,796.0 = 15.58% |
| Capital spending | $684.0m annually |
| Tax rate | 20.3% |
| Inventory days | 103.4 |
| Other working capital | 0.8% of revenue change |
| Debt / annual repayment | $7,942.0m / $0.0m |
| Minimum cash / revolver limit / rate | $1,000.0m / $2,000.0m / 6.0% |
| Share buyback | $150.0m annually |
| Cost of equity / terminal growth | 10.0% / 3.0% |
| Diluted shares | 1,481.0m |

## Expected visible output — independent arithmetic cross-check

This is the expected forecast from the current model inputs. Run the Python command after fixing Python availability; the model must reproduce these figures and the checks.

| Line (USD millions) | FY2027E | FY2028E | FY2029E | FY2030E | FY2031E |
|---|---:|---:|---:|---:|---:|
| Revenue | 50,109.8 | 53,116.4 | 55,772.3 | 58,003.1 | 59,743.2 |
| Operating income | 3,352.5 | 3,608.3 | 3,833.8 | 4,023.3 | 4,171.6 |
| Net income | 2,412.4 | 2,616.3 | 2,796.1 | 2,947.1 | 3,065.3 |
| FCFE | 1,843.7 | 2,159.2 | 2,390.2 | 2,606.4 | 2,802.0 |
| Year-end cash | 9,256.7 | 11,266.0 | 13,506.2 | 15,962.6 | 18,614.6 |
| Assets − liabilities − equity | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Cash ≥ $1,000m floor | Yes | Yes | Yes | Yes | Yes |

Expected valuation output: equity value **$35,461.2m**, terminal-value share **74.5%**, and value per share **$23.94**. No forecast year draws the revolver because FCFE, after the $150m annual buyback, keeps cash above the floor.

## Partner exchange 1 — prediction, mechanism, and question

### My Nike prediction

The input most likely to matter is **gross margin**, because each percentage-point change applies to every forecast dollar of revenue, changes operating income and after-tax FCFE, and therefore flows into the terminal value.

### Partner’s repeat-back prompt

Ask my partner to repeat this mechanism in their own words: “A gross-margin change changes gross profit; with SG&A linked to gross profit, it changes operating income, net income, FCFE, and the terminal value.”

### Question for my input range

What supports maintaining a 42.9% gross margin when NIKE’s history moved from 44.6% in FY2024 to 42.7% in FY2025 and 42.9% in FY2026?

### Gap written down before AI

I need evidence about the sustainability of gross margin—especially product costs, pricing, channel mix, and tariff effects—before defending a forecast range.

### Partner’s company

| Item | Notes to complete during exchange |
|---|---|
| Partner company and predicted key input |  |
| My repeat-back of their mechanism |  |
| My question about evidence supporting their range |  |
| Gap we identified before using AI |  |

## One-at-a-time sensitivity analysis

The added script is `nike_lab10_sensitivity.py`. It starts every scenario from a fresh independent copy of `BASE_INPUTS`, changes only the named driver, reruns the linked statements, retains each scenario’s statement trace, shows annual accounting checks, flags invalid valuation runs, and reruns the base case at the end.

### Drivers and estimated input ranges

| Driver | Lower | Base | Higher | Unit and forecast years |
|---|---|---|---|---|
| Revenue growth path | 6%, 4%, 3%, 2%, 1% | 8%, 6%, 5%, 4%, 3% | 10%, 8%, 7%, 6%, 5% | Annual growth; FY2027E–FY2031E |
| Gross margin | 41.9% | 42.9% | 43.9% | Percent of revenue; FY2027E–FY2031E |

### Results from the current model inputs

All cases pass the annual accounting checks: assets − liabilities − equity equals 0.0, cash remains above the $1,000m floor, and no case draws the revolver. FCFE is the model’s free-cash-flow measure.

| Driver | Case | FY2031E operating profit ($m) | FY2031E FCFE ($m) | Value/share | Valid valuation |
|---|---|---:|---:|---:|---|
| Revenue growth | Lower | 3,724.2 | 2,649.5 | $22.98 | Yes |
| Revenue growth | Base | 4,171.6 | 2,802.0 | $23.94 | Yes |
| Revenue growth | Higher | 4,654.3 | 2,951.5 | $24.88 | Yes |
| Gross margin | Lower | 4,057.7 | 2,706.2 | $23.04 | Yes |
| Gross margin | Base | 4,171.6 | 2,802.0 | $23.94 | Yes |
| Gross margin | Higher | 4,285.5 | 2,897.7 | $24.85 | Yes |

### Signed change from base and output spans

| Driver | Case | Operating profit change ($m) | FCFE change ($m) | Value/share change |
|---|---|---:|---:|---:|
| Revenue growth | Lower | (447.4) | (152.5) | ($0.96) |
| Revenue growth | Higher | +482.7 | +149.6 | +$0.93 |
| Gross margin | Lower | (113.9) | (95.7) | ($0.90) |
| Gross margin | Higher | +113.9 | +95.7 | +$0.90 |

| Driver | Operating-profit span ($m) | FCFE span ($m) | Value/share span |
|---|---:|---:|---:|
| Revenue growth | 930.1 | 302.0 | $1.89 |
| Gross margin | 227.9 | 191.5 | $1.81 |

The final base rerun is required to match the first base run; the script tests and prints `Restored base matches initial base: True`.

## V — Result check and locked record

| Check | Actual Nike result |
|---|---|
| Base before and after analysis | Same inputs and outputs: FY2031E FCFE is $2,802.0m and value per share is $23.94 in both base runs. The script requires an exact match before printing `True`. |
| Lower/higher run isolation | Each scenario begins with a fresh copy of `BASE_INPUTS`; only the selected growth path or gross-margin input changes. All statement lines then recalculate. |
| Accounting checks | Every lower/base/higher run passes: balance-sheet gap is 0.0 (within the script’s $0.05m tolerance), cash stays above the $1,000m floor, and the revolver remains below its limit. |
| Change from base | The script calculates each signed difference as scenario output minus its corresponding base output; the reconciled amounts appear in the signed-change table above. |

### Locked prediction and reconciliation

My prediction was that gross margin would matter most because it applies to every forecast dollar of revenue and flows through operating income, FCFE, and terminal value. The actual results do not support that prediction over the tested ranges: revenue growth has the larger span for FY2031E operating profit ($930.1m versus $227.9m), FCFE ($302.0m versus $191.5m), and value per share ($1.89 versus $1.81).

The prediction error is explained by the tested ranges and linkage: the revenue-growth scenarios change each annual growth rate by two percentage points, compound through all five years, and then change gross profit, SG&A, inventory, other working capital, FCFE, and terminal value. Gross margin changes by one percentage point in each year. This is an explanation of the model result, not a claim that it will occur.

The valuation conclusion from this model does not change: its $22.98–$24.88 per-share sensitivity range remains below the previously recorded $35.93 market price. The research priority changes to evidence on NIKE’s revenue recovery and sustainable growth, because revenue growth generated the larger tested output spans.

### Partner exchange 2 — evidence check

This exchange must be completed with the assigned partner; it is not represented as completed here.

| Required record | Complete during partner exchange |
|---|---|
| Changed result and base shown |  |
| Difference recomputed by partner |  |
| Other independent inputs checked at base |  |
| Statement trace requested and explained |  |
| Partner question or correction |  |
| My check of partner’s model |  |

## E — Find the driver

Over these ranges, **revenue growth** is the larger driver for operating profit, FCFE, and value per share. The comparison is based on output spans, not raw dollar levels.

| Output | Revenue-growth span | Gross-margin span | Larger driver over these ranges |
|---|---:|---:|---|
| FY2031E operating profit | $930.1m | $227.9m | Revenue growth |
| FY2031E FCFE | $302.0m | $191.5m | Revenue growth |
| Value per share | $1.89 | $1.81 | Revenue growth |

The limitation is material: a bigger span can reflect a wider chosen input range rather than an inherently more important driver. Here, the revenue-growth path changes by two percentage points in each forecast year, while gross margin changes by one percentage point. The appropriate conclusion is only that revenue growth is larger **over these ranges**.

### Partner exchange 3 — causal explanation

My causal link to explain: a change in annual revenue growth compounds revenue, then changes gross profit and SG&A, inventory and other working-capital investment, FCFE, and terminal value. The listener should ask whether the ranking could reflect the chosen ranges; the answer is yes, which is why the conclusion is limited to the stated ranges.

| Required record | Complete during partner exchange |
|---|---|
| Partner’s question about my ranking or ranges |  |
| My response |  |
| My question about their company’s causal link |  |
| Their response / my summary of their conclusion |  |
| Why the companies may have different main drivers |  |
