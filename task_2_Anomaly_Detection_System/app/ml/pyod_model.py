import pandas as pd
from pyod.models.knn import KNN


def detect_anomalies_pyod(df: pd.DataFrame, contamination: float = 0.01):

    model = KNN(contamination=contamination)

    model.fit(df[["value"]])

    
    df["anomaly"] = model.predict(df[["value"]])


    df["anomaly_score"] = model.decision_scores_

    return df