"""Lab 16 as-of data filter - standard library only."""

from collections import defaultdict
from datetime import date, datetime


# Editable training inputs.
DECISION_DATE = date(2026, 3, 31)
ROWS = [
    {"row": 1, "ticker": "AAA", "month": "2026-01", "published": "2026-02-10", "index": 101.0},
    {"row": 2, "ticker": "AAA", "month": "2026-02", "published": "2026-03-10", "index": 104.0},
    {"row": 3, "ticker": "AAA", "month": "2026-03", "published": "2026-04-10", "index": 109.0},
    {"row": 4, "ticker": "AAA", "month": "2026-02", "published": "2026-03-25", "index": 103.0},
    {"row": 5, "ticker": "BBB", "month": "2026-01", "published": "2026-02-10", "index": 98.0},
    {"row": 6, "ticker": "BBB", "month": "2026-02", "published": "2026-03-10", "index": 97.0},
    {"row": 7, "ticker": "BBB", "month": "2026-02", "published": "2026-03-10", "index": 97.0},
    {"row": 8, "ticker": "BBB", "month": "2026-03", "published": "2026-04-10", "index": 92.0},
    {"row": 9, "ticker": "CCC", "month": "2026-01", "published": "2026-02-10", "index": 110.0},
    {"row": 10, "ticker": "CCC", "month": "2026-02", "published": "2026-04-05", "index": 112.0},
    {"row": 11, "ticker": "", "month": "2026-02", "published": "2026-03-10", "index": 99.0},
    {"row": 12, "ticker": "CCC", "month": "2026-02", "published": "2026-03-10", "index": 111.0},
]


def publication_date(row):
    """Convert a row's publication text to a date."""
    return date.fromisoformat(row["published"])


def remove_missing_ticker(rows):
    """Rule 1: quarantine rows without a ticker."""
    removed = [row for row in rows if not row["ticker"]]
    kept = [row for row in rows if row["ticker"]]
    return kept, removed


def duplicate_key(row):
    """Return the fields that define an exact duplicate, excluding row number."""
    return row["ticker"], row["month"], row["published"], row["index"]


def remove_exact_duplicates(rows):
    """Rule 2: retain the first row and remove later exact duplicates."""
    seen, kept, removed = set(), [], []
    for row in rows:
        key = duplicate_key(row)
        if key in seen:
            removed.append(row)
        else:
            seen.add(key)
            kept.append(row)
    return kept, removed


def remove_after_decision_date(rows, decision_date):
    """Rule 3: remove rows that were not published by the decision date."""
    removed = [row for row in rows if publication_date(row) > decision_date]
    kept = [row for row in rows if publication_date(row) <= decision_date]
    return kept, removed


def keep_latest_revision(rows):
    """Rule 4: keep the latest publication for each ticker and measured month."""
    latest_by_series = {}
    for row in rows:
        key = row["ticker"], row["month"]
        if key not in latest_by_series or publication_date(row) > publication_date(latest_by_series[key]):
            latest_by_series[key] = row
    kept = [row for row in rows if latest_by_series[row["ticker"], row["month"]]["row"] == row["row"]]
    removed = [row for row in rows if row not in kept]
    return kept, removed


def asof_filter(rows, decision_date):
    """Apply the four as-of rules in the required order and return the row funnel."""
    remaining, missing_ticker = remove_missing_ticker(rows)
    remaining, duplicates = remove_exact_duplicates(remaining)
    remaining, after_date = remove_after_decision_date(remaining, decision_date)
    panel, older_revision = keep_latest_revision(remaining)
    funnel = [
        ("Quarantined: no ticker", missing_ticker),
        ("Exact duplicate", duplicates),
        (f"Published after {decision_date:%d %B}", after_date),
        ("Older vintage replaced by a revision", older_revision),
    ]
    return panel, funnel


def naive_panel(rows):
    """Keep latest publications regardless of decision date, after basic data cleaning."""
    remaining, _ = remove_missing_ticker(rows)
    remaining, _ = remove_exact_duplicates(remaining)
    publication_counts = defaultdict(int)
    for row in remaining:
        publication_counts[row["ticker"], row["month"]] += 1
    revised_months = {key for key, count in publication_counts.items() if count > 1}
    panel, _ = keep_latest_revision(remaining)
    return panel, revised_months


def month_name(month):
    """Convert YYYY-MM to a readable month name."""
    return datetime.strptime(month, "%Y-%m").strftime("%B")


def signals(panel, revised_months=None):
    """Return each ticker's latest month-over-month index signal."""
    rows_by_ticker = defaultdict(list)
    for row in panel:
        rows_by_ticker[row["ticker"]].append(row)
    output = {}
    for ticker, ticker_rows in rows_by_ticker.items():
        ordered = sorted(ticker_rows, key=lambda row: row["month"])
        if len(ordered) < 2:
            continue
        previous, latest = ordered[-2], ordered[-1]
        change = (latest["index"] / previous["index"] - 1.0) * 100
        output[ticker] = {
            "change": change,
            "month": latest["month"],
            "revised": (ticker, latest["month"]) in (revised_months or set()),
        }
    return output


def row_numbers(rows):
    """Return comma-separated row numbers for output."""
    return ", ".join(str(row["row"]) for row in rows) or "None"


def print_funnel(funnel):
    """Print the removals from each as-of filtering rule."""
    print("ROW FUNNEL")
    print(f"{'Funnel step':<40}{'Rows removed'}")
    for label, removed in funnel:
        print(f"{label:<40}{row_numbers(removed)}")


def print_panel(panel):
    """Print the rows that were knowable on the decision date."""
    print("\nAS-OF PANEL")
    print(f"{'Row':<6}{'Ticker':<8}{'Month measured':<18}{'Published on':<15}{'Index':>8}")
    for row in panel:
        print(f"{row['row']:<6}{row['ticker']:<8}{row['month']:<18}{row['published']:<15}{row['index']:>8.1f}")


def print_signals(asof_signals, naive_signals):
    """Print as-of and naive signals side by side."""
    print("\nSIGNALS")
    print(f"{'Ticker':<8}{'As-of signal':<28}{'Naive signal'}")
    for ticker in sorted(asof_signals):
        asof = asof_signals[ticker]
        naive = naive_signals[ticker]
        asof_text = f"{asof['change']:+.2f}% ({month_name(asof['month'])})"
        naive_month = month_name(naive["month"])
        if naive["revised"]:
            naive_month += ", revised"
        naive_text = f"{naive['change']:+.2f}% ({naive_month})"
        print(f"{ticker:<8}{asof_text:<28}{naive_text}")


def main():
    panel, funnel = asof_filter(ROWS, DECISION_DATE)
    all_dates_panel, revised_months = naive_panel(ROWS)
    print_funnel(funnel)
    print_panel(panel)
    print_signals(signals(panel), signals(all_dates_panel, revised_months))


if __name__ == "__main__":
    main()
