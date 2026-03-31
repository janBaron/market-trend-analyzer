# 📈 Market Trend Analyzer

A lightweight Python project for analyzing financial market data using simple quantitative methods.
The tool retrieves historical price data via an API, computes key indicators, classifies market regimes, and visualizes results.

---

## 🚀 Project Motivation

This project was built to explore how basic quantitative indicators can be used to structure and analyze financial time series data.

The goal is **not** to develop a profitable trading system, but to demonstrate:

* data acquisition via APIs
* data preprocessing and transformation
* indicator engineering
* simple rule-based market classification
* visualization and reporting

---

## ⚙️ Features

* 📊 **Market Data Retrieval**

  * Fetches historical price data using `yfinance`

* 🧮 **Indicator Calculation**

  * Moving Averages (MA20, MA50)
  * Momentum (10-day)
  * Daily Returns
  * Rolling Volatility (20-day)

* 📉 **Market Regime Classification**

  * Uptrend
  * Downtrend
  * Neutral

* 📈 **Visualization**

  * Price series with moving averages
  * Trend signals highlighted

* 📄 **Reporting**

  * Trend distribution
  * Average returns per regime
  * Simple strategy vs. buy & hold comparison

---

## 🧠 Methodology

The project applies simple quantitative rules to identify basic market regimes:

* **Uptrend**

  * Price > MA20
  * MA20 > MA50
  * Positive momentum

* **Downtrend**

  * Price < MA20
  * MA20 < MA50
  * Negative momentum

* **Neutral**

  * All other cases

These rules are intentionally simple and interpretable.

---

## 📊 Example Output

The tool generates:

* A chart showing price, moving averages, and trend signals
* A summary report with statistics and performance comparison

Example files:

```
output/
├── trend_chart.png
└── summary.txt
```

---

## ⚠️ Disclaimer

This project is for educational and demonstration purposes only.

* No transaction costs are considered
* No out-of-sample validation
* No risk management
* Not suitable for real trading decisions

The focus is on **data processing and analysis**, not financial performance.

---

## 🛠️ Tech Stack

* Python
* pandas
* numpy
* matplotlib
* yfinance

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/market-trend-analyzer.git
cd market-trend-analyzer
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

---

## 📌 Project Structure

```
market-trend-analyzer/
│
├── app.py
├── config.py
├── README.md
├── requirements.txt
│
├── data/
├── output/
│
└── src/
    ├── data_loader.py
    ├── indicators.py
    ├── trend_logic.py
    ├── plotting.py
    └── reporting.py
```

---

## 💡 Key Takeaways

This project demonstrates:

* structured handling of financial time series data
* implementation of basic quantitative indicators
* transformation of raw data into interpretable signals
* clear separation of concerns in code design

---

## 👤 About Me

I am a Business Informatics student with a strong interest in data-driven systems, quantitative analysis, and software engineering.

This project reflects my approach to combining:

* technical implementation
* analytical thinking
* structured problem solving

---

## 📬 Contact

Feel free to reach out or connect via GitHub.
