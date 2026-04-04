import streamlit as st

from src.data_loader import load_market_data
from src.indicators import add_indicators
from src.trend_logic import classify_trend
from src.plotting import create_market_plot


st.set_page_config(page_title="Market Trend Analyzer", layout="wide")

st.title("📈 Market Trend Analyzer")
st.caption(
    "A lightweight Python application for retrieving historical market data, "
    "computing simple quantitative indicators, and classifying basic market regimes."
)

st.info(
    "This project is intended for educational and analytical purposes only. "
    "It is not a trading bot and does not provide investment advice."
)

with st.sidebar:
    st.header("Analysis Settings")
    ticker = st.text_input("Ticker Symbol", value="AAPL").upper()
    period = st.selectbox("Time Period", ["6mo", "1y", "2y", "5y"], index=1)
    run_analysis = st.button("Run Analysis")

if run_analysis:
    try:
        data = load_market_data(ticker=ticker, period=period, interval="1d")
        data = add_indicators(data)
        data = classify_trend(data)

        clean_data = data.dropna()

        if clean_data.empty:
            st.warning("Not enough data available to compute indicators.")
        else:
            latest_row = clean_data.iloc[-1]
            current_trend = latest_row["Trend"]
            latest_close = latest_row["Close"]
            latest_ma20 = latest_row["MA20"]
            latest_ma50 = latest_row["MA50"]
            latest_momentum = latest_row["Momentum_10"]
            latest_volatility = latest_row["Volatility_20"]
            latest_date = clean_data.index[-1].strftime("%Y-%m-%d")

            st.success(f"Analysis completed for {ticker}")

            if current_trend == "Uptrend":
                st.markdown(f"### Current Regime: ✅ **{current_trend}**")
            elif current_trend == "Downtrend":
                st.markdown(f"### Current Regime: ⚠️ **{current_trend}**")
            else:
                st.markdown(f"### Current Regime: ➖ **{current_trend}**")

            st.caption(f"Latest analyzed trading day: {latest_date}")

            tab1, tab2, tab3 = st.tabs(["Overview", "Data", "Methodology"])

            with tab1:
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

                st.subheader("Price and Trend Visualization")
                fig = create_market_plot(data, ticker)
                st.pyplot(fig)

                st.subheader("Trend Distribution")
                trend_counts = data["Trend"].value_counts()
                st.dataframe(trend_counts.rename_axis("Trend").reset_index(name="Count"), use_container_width=True)

            with tab2:
                st.subheader("Recent Analyzed Data")
                display_columns = ["Close", "MA20", "MA50", "Momentum_10", "Volatility_20", "Trend"]
                st.dataframe(data[display_columns].tail(20), use_container_width=True)

            with tab3:
                st.subheader("Methodology")
                st.markdown(
                    """
                    This tool applies simple quantitative indicators to historical market data:

                    - **MA20**: short-term moving average
                    - **MA50**: medium-term moving average
                    - **Momentum (10d)**: price change over 10 trading days
                    - **Volatility (20d)**: rolling standard deviation of daily returns

                    **Trend classification rules**
                    - **Uptrend**: Close > MA20, MA20 > MA50, Momentum > 0
                    - **Downtrend**: Close < MA20, MA20 < MA50, Momentum < 0
                    - **Neutral**: all other cases

                    The purpose of this project is to demonstrate structured financial data analysis,
                    indicator engineering, and interpretable rule-based classification.
                    """
                )

    except Exception as e:
        st.error(f"Error during analysis: {e}")

else:
    st.write("Use the sidebar to select a ticker and run the analysis.")