import yfinance as yf
import pandas as pd


def load_market_data(ticker: str, period: str = "1y", interval: str = "1d") -> pd.DataFrame:
    """
    Load and prepare historical market data for a given ticker symbol.
    """
    data = yf.download(ticker, period=period, interval=interval, auto_adjust=False)

    if data.empty:
        raise ValueError(f"No data found for ticker '{ticker}'.")

    data = data.copy()

    # Flatten MultiIndex columns if needed
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    # Keep only relevant columns
    required_columns = ["Open", "High", "Low", "Close", "Volume"]
    data = data[required_columns]

    # Remove missing values
    data = data.dropna()

    return data