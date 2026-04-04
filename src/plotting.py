import os
import pandas as pd
import matplotlib.pyplot as plt


def create_market_plot(data: pd.DataFrame, ticker: str):
    """
    Create a matplotlib figure showing close price, moving averages,
    and trend signals.
    """
    df = data.copy()

    fig, ax = plt.subplots(figsize=(14, 7))

    ax.plot(df.index, df["Close"], label="Close")
    ax.plot(df.index, df["MA20"], label="MA20")
    ax.plot(df.index, df["MA50"], label="MA50")

    uptrend = df[df["Trend"] == "Uptrend"]
    downtrend = df[df["Trend"] == "Downtrend"]

    ax.scatter(uptrend.index, uptrend["Close"], label="Uptrend Signal", marker="^", s=40)
    ax.scatter(downtrend.index, downtrend["Close"], label="Downtrend Signal", marker="v", s=40)

    ax.set_title(f"{ticker} Market Trend Analysis")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    ax.grid(True)

    fig.tight_layout()
    return fig


def save_market_plot(data: pd.DataFrame, ticker: str, output_path: str = "output/trend_chart.png") -> None:
    """
    Save the market analysis plot as a PNG file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    fig = create_market_plot(data, ticker)
    fig.savefig(output_path)
    plt.close(fig)