import pandas as pd
import numpy as np


def classify_trend(data: pd.DataFrame) -> pd.DataFrame:
    """
    Classify market regime into Uptrend, Downtrend, or Neutral.
    """
    df = data.copy()

    uptrend_condition = (
        (df["Close"] > df["MA20"]) &
        (df["MA20"] > df["MA50"]) &
        (df["Momentum_10"] > 0)
    )

    downtrend_condition = (
        (df["Close"] < df["MA20"]) &
        (df["MA20"] < df["MA50"]) &
        (df["Momentum_10"] < 0)
    )

    df["Trend"] = np.select(
        [uptrend_condition, downtrend_condition],
        ["Uptrend", "Downtrend"],
        default="Neutral"
    )

    return df