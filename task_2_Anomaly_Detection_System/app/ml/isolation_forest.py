import pandas as pd

from sklearn.ensemble import IsolationForest


def detect_anomalies_isolation_forest(
    df: pd.DataFrame,
    contamination: float = 0.01
) -> pd.DataFrame:

    # create model
    model = IsolationForest(
        contamination=contamination,
        random_state=42
    )

    df["anomaly_score"] = model.fit_predict(df[["value"]])

    df["anomaly"] = df["anomaly_score"] == -1

    return df