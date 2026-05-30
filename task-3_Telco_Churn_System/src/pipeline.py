import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "logistic_model.pkl")
FEATURES_PATH = os.path.join(BASE_DIR, "models", "model_features.pkl")

model = joblib.load(MODEL_PATH)
model_features = joblib.load(FEATURES_PATH)


def run_batch_scoring(X):
    X = pd.get_dummies(X)

    # ALIGN FEATURES (THIS IS THE FIX)
    X = X.reindex(columns=model_features, fill_value=0)

    churn_prob = model.predict_proba(X)[:, 1]

    predictions_df = X.copy()
    predictions_df["churn_probability"] = churn_prob

    predictions_df["risk_level"] = predictions_df["churn_probability"].apply(
        lambda x: "HIGH" if x > 0.7 else ("MEDIUM" if x > 0.4 else "LOW")
    )

    predictions_df["recommendations"] = predictions_df["risk_level"].apply(
        lambda x: "Immediate retention call" if x == "HIGH"
        else ("Send offer" if x == "MEDIUM" else "No action required")
    )

    return predictions_df, X