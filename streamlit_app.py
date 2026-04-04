import streamlit as st

from src.data_loader import load_market_data
from src.indicators import add_indicators
from src.trend_logic import classify_trend


st.set_page_config(page_title="Market Trend Analyzer", layout="wide")

st.title("📈 Market Trend Analyzer")
st.write(
    "A lightweight financial market analysis tool for retrieving historical price data, "
    "computing simple quantitative indicators, and classifying basic market regimes."
)

st.info(
    "This tool is for educational and analytical purposes only. "
    "It does not provide investment advice or promise financial returns."
)

ticker = st.text_input("Enter ticker symbol", value="AAPL").upper()
period = st.selectbox("Select time period", ["6mo", "1y", "2y", "5y"], index=1)

if st.button("Run analysis"):
    try:
        data = load_market_data(ticker=ticker, period=period, interval="1d")
        data = add_indicators(data)
        data = classify_trend(data)

        latest_row = data.dropna().iloc[-1]
        current_trend = latest_row["Trend"]
        latest_close = latest_row["Close"]
        latest_ma20 = latest_row["MA20"]
        latest_ma50 = latest_row["MA50"]
        latest_momentum = latest_row["Momentum_10"]
        latest_volatility = latest_row["Volatility_20"]

        st.success(f"Analysis completed for {ticker}")

        st.subheader("Current Market Snapshot")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Latest Close", f"{latest_close:.2f}")
            st.metric("MA20", f"{latest_ma20:.2f}")

        with col2:
            st.metric("MA50", f"{latest_ma50:.2f}")
            st.metric("Momentum (10d)", f"{latest_momentum:.2f}")

        with col3:
            st.metric("Volatility (20d)", f"{latest_volatility:.4f}")
            st.metric("Detected Trend", current_trend)

        st.subheader("Trend Distribution")
        trend_counts = data["Trend"].value_counts()
        st.dataframe(trend_counts.rename_axis("Trend").reset_index(name="Count"))

        st.subheader("Recent Analyzed Data")
        display_columns = ["Close", "MA20", "MA50", "Momentum_10", "Volatility_20", "Trend"]
        st.dataframe(data[display_columns].tail(15))

    except Exception as e:
        st.error(f"Error during analysis: {e}")