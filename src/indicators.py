import pandas as pd


def add_indicators(data: pd.DataFrame) -> pd.DataFrame:
    """
    Add technical indicators to the market data.
    """
    df = data.copy()

    # Moving averages
    df["MA20"] = df["Close"].rolling(window=20).mean()
    df["MA50"] = df["Close"].rolling(window=50).mean()

    # Momentum over 10 days
    df["Momentum_10"] = df["Close"] - df["Close"].shift(10)

    # Daily returns
    df["Daily_Return"] = df["Close"].pct_change()

    # Rolling volatility over 20 days
    df["Volatility_20"] = df["Daily_Return"].rolling(window=20).std()

    return df