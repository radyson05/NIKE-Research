# Lab 14 - Meridian Portfolio Baselines

## Inputs

| Sleeve | Expected return | Volatility |
|---|---:|---:|
| Treasury bills | 3.5% | 0.5% |
| Treasury 10-year note | 4.3% | 7.0% |
| Investment-grade bond fund | 5.0% | 6.0% |
| Global equity index fund | 8.0% | 16.0% |

Objective return: 6.5% (CPI estimate of 2.5% plus 4.0%). Reserve-eligible sleeves: Treasury bills and Treasury 10-year note.

## Known-answer check

| Portfolio | Weights: bills / 10-year / IG / equity | Return | Volatility | Reserve-eligible | Meets 6.5%? |
|---|---|---:|---:|---:|---|
| Benchmark | 0.0% / 0.0% / 40.0% / 60.0% | 6.80% | 10.46% | 0.0% | Yes |
| Equal weight | 25.0% / 25.0% / 25.0% / 25.0% | 5.20% | 5.21% | 50.0% | No |
| Inverse volatility | 84.3% / 6.0% / 7.0% / 2.6% | 3.77% | 1.05% | 90.3% | No |

All values match the Lab 14 known answers.

## Correlation sensitivity test

The investment-grade bond fund / global equity index fund correlation was temporarily changed from 0.25 to 0.50 in both symmetric correlation-table cells. After rerunning `python portfolio.py`, the benchmark volatility increased from 10.46% to **11.00%**, as expected. The original 0.25 correlation was restored in `portfolio.py`.

## Portfolio volatility logic

`build_covariance_matrix` calculates each covariance as:

`correlation[i][j] * volatility[i] * volatility[j]`

`portfolio_variance` calculates the weighted sum of every covariance pair:

`sum(weights[i] * covariance_matrix[i][j] * weights[j])`

`portfolio_volatility` takes the square root of that variance. Higher correlation between the IG bond fund and equity reduces their diversification benefit, increasing the benchmark's volatility.

## Run command

```powershell
python portfolio.py
```
