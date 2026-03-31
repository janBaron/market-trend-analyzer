from src.data_loader import load_market_data
from src.indicators import add_indicators


def main():
    ticker = "AAPL"

    data = load_market_data(ticker=ticker, period="1y", interval="1d")
    data_with_indicators = add_indicators(data)

    print(f"\nLoaded data for {ticker}")
    print("\nFirst rows with indicators:")
    print(data_with_indicators.head(25))

    print("\nColumns:")
    print(data_with_indicators.columns.tolist())

    print(f"\nShape: {data_with_indicators.shape}")


if __name__ == "__main__":
    main()