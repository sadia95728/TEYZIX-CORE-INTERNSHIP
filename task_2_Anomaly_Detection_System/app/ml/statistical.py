import pandas as pd
import numpy as np


def detect_anomalies_zscore(
    df: pd.DataFrame,
    threshold: int = 3
) -> pd.DataFrame:

    mean = df["value"].mean()
    std = df["value"].std()

    # calculate z-score
    df["z_score"] = (df["value"] - mean) / std

    # detect anomalies
    df["anomaly"] = df["z_score"].abs() > threshold

    return df