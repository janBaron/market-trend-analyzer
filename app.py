from src.data_loader import load_market_data
from src.indicators import add_indicators
from src.trend_logic import classify_trend


def main():
    ticker = "AAPL"

    data = load_market_data(ticker=ticker, period="1y", interval="1d")
    data = add_indicators(data)
    data = classify_trend(data)

    print(f"\nLoaded data for {ticker}")
    print("\nLast rows with trend classification:")
    print(data[["Close", "MA20", "MA50", "Momentum_10", "Volatility_20", "Trend"]].tail(15))

    print("\nTrend distribution:")
    print(data["Trend"].value_counts())


if __name__ == "__main__":
    main()