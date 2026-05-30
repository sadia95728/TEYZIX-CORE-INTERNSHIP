import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "logistic_model.pkl")
FEATURES_PATH = os.path.join(BASE_DIR, "models", "model_features.pkl")


def load_model():
    return joblib.load(MODEL_PATH)


def load_features():
    return joblib.load(FEATURES_PATH)


def predict_churn(model, X):
    return model.predict_proba(X)[:, 1]