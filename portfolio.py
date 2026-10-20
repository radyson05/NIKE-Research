"""Meridian portfolio baseline analysis - standard library only."""

from math import sqrt

# Editable inputs. Returns and volatilities are decimals (for example, 3.5% = 0.035).
SLEEVES = [
    {"name": "Treasury bills", "expected_return": 0.035, "volatility": 0.005},
    {"name": "Treasury 10-year note", "expected_return": 0.043, "volatility": 0.070},
    {"name": "Investment-grade bond fund", "expected_return": 0.050, "volatility": 0.060},
    {"name": "Global equity index fund", "expected_return": 0.080, "volatility": 0.160},
]

CORRELATIONS = [
    [1.00, 0.10, 0.05, 0.00],
    [0.10, 1.00, 0.80, -0.10],
    [0.05, 0.80, 1.00, 0.25],
    [0.00, -0.10, 0.25, 1.00],
]

OBJECTIVE_RETURN = 0.065
RESERVE_ELIGIBLE = {"Treasury bills", "Treasury 10-year note"}


def validate_correlation_table(correlations, sleeve_count):
    """Raise ValueError if a correlation matrix is not square, valid, and symmetric."""
    if len(correlations) != sleeve_count:
        raise ValueError("Correlation table must have one row for each sleeve.")
    for row_index, row in enumerate(correlations):
        if len(row) != sleeve_count:
            raise ValueError("Correlation table must be square.")
        for column_index, correlation in enumerate(row):
            if not -1.0 <= correlation <= 1.0:
                raise ValueError(
                    f"Correlation at row {row_index + 1}, column {column_index + 1} "
                    "must be between -1 and 1."
                )
            if correlation != correlations[column_index][row_index]:
                raise ValueError("Correlation table must be symmetric across its diagonal.")


def build_covariance_matrix(sleeves, correlations):
    """Return covariance[i][j] = correlation[i][j] * volatility[i] * volatility[j]."""
    return [
        [
            correlations[i][j] * sleeves[i]["volatility"] * sleeves[j]["volatility"]
            for j in range(len(sleeves))
        ]
        for i in range(len(sleeves))
    ]


def benchmark_weights():
    """Return 40% IG bonds and 60% global equity weights in sleeve order."""
    return [0.0, 0.0, 0.40, 0.60]


def equal_weight_weights(sleeve_count):
    """Return equal weights that sum to 100%."""
    return [1.0 / sleeve_count] * sleeve_count


def inverse_volatility_weights(sleeves):
    """Scale 1 / volatility weights to sum to 100%."""
    inverse_volatilities = []
    for sleeve in sleeves:
        if sleeve["volatility"] <= 0:
            raise ValueError("Each sleeve volatility must be greater than zero.")
        inverse_volatilities.append(1.0 / sleeve["volatility"])
    total = sum(inverse_volatilities)
    return [value / total for value in inverse_volatilities]


def expected_return(weights, sleeves):
    """Return the portfolio's weighted expected return."""
    return sum(weight * sleeve["expected_return"] for weight, sleeve in zip(weights, sleeves))


def portfolio_variance(weights, covariance_matrix):
    """Return w' * covariance * w."""
    return sum(
        weights[i] * covariance_matrix[i][j] * weights[j]
        for i in range(len(weights))
        for j in range(len(weights))
    )


def portfolio_volatility(weights, covariance_matrix):
    """Return the square root of portfolio variance."""
    variance = portfolio_variance(weights, covariance_matrix)
    if variance < 0:
        raise ValueError("Portfolio variance cannot be negative.")
    return sqrt(variance)


def reserve_eligible_weight(weights, sleeves, eligible_names):
    """Return the total weight in reserve-eligible sleeves."""
    return sum(
        weight for weight, sleeve in zip(weights, sleeves) if sleeve["name"] in eligible_names
    )


def meets_objective(portfolio_return, objective_return):
    """Return whether expected return meets or exceeds the objective."""
    return portfolio_return >= objective_return


def format_percent(value, decimals):
    """Format a decimal as a percentage."""
    return f"{value:.{decimals}%}"


def print_portfolio(name, weights, sleeves, covariance_matrix, objective_return):
    """Print one portfolio's weights, return, risk, reserve weight, and objective result."""
    portfolio_return = expected_return(weights, sleeves)
    volatility = portfolio_volatility(weights, covariance_matrix)
    reserve_weight = reserve_eligible_weight(weights, sleeves, RESERVE_ELIGIBLE)

    print(f"\n{name}")
    for sleeve, weight in zip(sleeves, weights):
        print(f"  {sleeve['name']}: {format_percent(weight, 1)}")
    print(f"  Expected return: {format_percent(portfolio_return, 2)}")
    print(f"  Volatility: {format_percent(volatility, 2)}")
    print(f"  Reserve-eligible weight: {format_percent(reserve_weight, 1)}")
    print(f"  Meets {format_percent(objective_return, 1)} objective: "
          f"{'Yes' if meets_objective(portfolio_return, objective_return) else 'No'}")


def main():
    validate_correlation_table(CORRELATIONS, len(SLEEVES))
    covariance_matrix = build_covariance_matrix(SLEEVES, CORRELATIONS)
    portfolios = [
        ("Benchmark", benchmark_weights()),
        ("Equal weight", equal_weight_weights(len(SLEEVES))),
        ("Inverse volatility", inverse_volatility_weights(SLEEVES)),
    ]
    print("MERIDIAN PORTFOLIO BASELINES")
    print(f"Objective return: {format_percent(OBJECTIVE_RETURN, 1)}")
    for name, weights in portfolios:
        print_portfolio(name, weights, SLEEVES, covariance_matrix, OBJECTIVE_RETURN)


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(f"Input error: {error}")
