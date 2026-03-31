from src.data_loader import load_market_data


def main():
    ticker = "AAPL"
    data = load_market_data(ticker=ticker, period="1y", interval="1d")

    print(f"\nLoaded data for {ticker}")
    print("\nFirst rows:")
    print(data.head())

    print("\nLast rows:")
    print(data.tail())

    print("\nColumns:")
    print(data.columns.tolist())

    print(f"\nShape: {data.shape}")


if __name__ == "__main__":
    main()