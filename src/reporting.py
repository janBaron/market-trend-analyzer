import pandas as pd
import os


def generate_report(data: pd.DataFrame, ticker: str, output_path: str = "output/summary.txt") -> None:
    """
    Generate a simple text report with trend statistics.
    """
    df = data.copy()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Trend distribution
    trend_counts = df["Trend"].value_counts()

    # Average returns per trend
    avg_returns = df.groupby("Trend")["Daily_Return"].mean()

    # Basic strategy: invested only during Uptrend
    df["Strategy_Return"] = df["Daily_Return"] * (df["Trend"] == "Uptrend")

    cumulative_strategy = (1 + df["Strategy_Return"].fillna(0)).cumprod()
    cumulative_buy_hold = (1 + df["Daily_Return"].fillna(0)).cumprod()

    strategy_performance = cumulative_strategy.iloc[-1]
    buy_hold_performance = cumulative_buy_hold.iloc[-1]

    with open(output_path, "w") as f:
        f.write(f"Market Trend Analysis Report for {ticker}\n")
        f.write("=" * 50 + "\n\n")

        f.write("Trend Distribution:\n")
        f.write(trend_counts.to_string())
        f.write("\n\n")

        f.write("Average Daily Returns by Trend:\n")
        f.write(avg_returns.to_string())
        f.write("\n\n")

        f.write("Performance Comparison:\n")
        f.write(f"Strategy (Uptrend only): {strategy_performance:.4f}\n")
        f.write(f"Buy & Hold: {buy_hold_performance:.4f}\n\n")

        f.write("Disclaimer:\n")
        f.write("This analysis is simplified and does not account for transaction costs, slippage, or out-of-sample validation.\n")