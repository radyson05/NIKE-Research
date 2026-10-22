"""Download five completed years of Yahoo Finance monthly adjusted-close prices.

This uses a course-practice fund universe. Run with:
    python download_lab15_prices.py
"""

import csv
import json
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen


# Fund universe selected for the four roles in the Lab 15 instructions.
FUNDS = {
    "BIL": ("SPDR Bloomberg 1-3 Month T-Bill ETF", "Cash and reserve"),
    "IEF": ("iShares 7-10 Year Treasury Bond ETF", "Government bonds"),
    "LQD": ("iShares iBoxx $ Investment Grade Corporate Bond ETF", "Fixed income"),
    "VT": ("Vanguard Total World Stock ETF", "Equity"),
}

# Five full calendar years of completed monthly observations: Oct. 2021-Sept. 2026.
START_DATE = date(2021, 10, 1)
END_DATE_EXCLUSIVE = date(2026, 10, 1)
PRICES_FILE = Path("prices.csv")
SOURCES_FILE = Path("prices_sources.md")


def unix_timestamp(value):
    """Return the UTC Unix timestamp for a date."""
    return int(datetime(value.year, value.month, value.day, tzinfo=timezone.utc).timestamp())


def download_monthly_adjusted_close(ticker):
    """Return a {YYYY-MM-DD: adjusted_close} mapping from Yahoo Finance."""
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
        f"?period1={unix_timestamp(START_DATE)}"
        f"&period2={unix_timestamp(END_DATE_EXCLUSIVE)}&interval=1mo"
        "&events=history&includeAdjustedClose=true"
    )
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=30) as response:
        payload = json.load(response)
    result = payload["chart"]["result"][0]
    timestamps = result["timestamp"]
    adjusted = result["indicators"]["adjclose"][0]["adjclose"]
    prices = {}
    for timestamp, value in zip(timestamps, adjusted):
        if value is not None:
            month = datetime.fromtimestamp(timestamp, tz=timezone.utc).date().replace(day=1)
            prices[month.isoformat()] = value
    return prices, url


def write_prices_csv(series_by_ticker):
    """Write oldest-first dates and one adjusted-close column per ticker."""
    common_dates = sorted(set.intersection(*(set(series) for series in series_by_ticker.values())))
    if len(common_dates) != 60:
        raise ValueError(f"Expected 60 completed monthly observations; received {len(common_dates)}.")
    with PRICES_FILE.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(["Date", *FUNDS])
        for month in common_dates:
            writer.writerow([month, *(f"{series_by_ticker[ticker][month]:.6f}" for ticker in FUNDS)])
    return common_dates


def write_sources_markdown(urls, months):
    """Write the required ticker, fund, role, source, and download-date record."""
    download_date = date.today().isoformat()
    lines = [
        "# Lab 15 Price Sources",
        "",
        "This is a course-practice fund universe, not investment advice.",
        "Returns calculated from these prices are historical estimates, not forecasts.",
        "",
        "| Ticker | Fund name | Role | Source | Download date | Price period |",
        "|---|---|---|---|---|---|",
    ]
    for ticker, (fund_name, role) in FUNDS.items():
        source = f"[Yahoo Finance monthly historical data]({urls[ticker]})"
        lines.append(
            f"| {ticker} | {fund_name} | {role} | {source} | {download_date} | "
            f"{months[0]} through {months[-1]} |"
        )
    SOURCES_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    series_by_ticker, urls = {}, {}
    for ticker in FUNDS:
        prices, url = download_monthly_adjusted_close(ticker)
        series_by_ticker[ticker] = prices
        urls[ticker] = url
    months = write_prices_csv(series_by_ticker)
    write_sources_markdown(urls, months)
    print(f"Wrote {PRICES_FILE} with {len(months)} monthly observations.")
    print(f"Wrote {SOURCES_FILE}.")


if __name__ == "__main__":
    main()
