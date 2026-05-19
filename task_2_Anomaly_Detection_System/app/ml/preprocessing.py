import pandas as pd
from sklearn.preprocessing import StandardScaler


def set_timestamp_index(df: pd.DataFrame) -> pd.DataFrame:
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp"])
    df = df.set_index("timestamp")
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df["value"] = df["value"].fillna(df["value"].mean())
    return df


def scale_values(df: pd.DataFrame) -> pd.DataFrame:
    scaler = StandardScaler()
    df["value"] = scaler.fit_transform(df[["value"]])
    return df


def preprocess(df: pd.DataFrame, scale: bool = False) -> pd.DataFrame:
    df = set_timestamp_index(df)
    df = handle_missing_values(df)

    if scale:
        df = scale_values(df)

    return df