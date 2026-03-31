import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_market_analysis(data: pd.DataFrame, ticker: str, output_path: str = "output/trend_chart.png") -> None:
    """
    Plot closing price, moving averages, and highlight trend phases.
    """
    df = data.copy()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df["Close"], label="Close")
    plt.plot(df.index, df["MA20"], label="MA20")
    plt.plot(df.index, df["MA50"], label="MA50")

    uptrend = df[df["Trend"] == "Uptrend"]
    downtrend = df[df["Trend"] == "Downtrend"]

    plt.scatter(uptrend.index, uptrend["Close"], label="Uptrend Signal", marker="^", s=40)
    plt.scatter(downtrend.index, downtrend["Close"], label="Downtrend Signal", marker="v", s=40)

    plt.title(f"{ticker} Market Trend Analysis")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()