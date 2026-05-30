import shap
import pandas as pd


def create_explainer(model, X_sample):
    """
    Creates SHAP explainer for Logistic Regression or linear models
    """
    explainer = shap.LinearExplainer(model, X_sample, feature_perturbation="interventional")
    return explainer


def get_shap_values(explainer, X):
    """
    Returns SHAP values for dataset
    """
    shap_values = explainer.shap_values(X)
    return shap_values


def get_top_features(shap_values_row, feature_names, top_n=3):
    """
    Extract top contributing features for a single customer
    """

    importance = list(zip(feature_names, shap_values_row))

    # sort by absolute impact
    importance.sort(key=lambda x: abs(x[1]), reverse=True)

    top_features = []

    for feature, value in importance[:top_n]:
        if value > 0:
            direction = "increases churn risk"
        else:
            direction = "reduces churn risk"

        top_features.append({
            "feature": feature,
            "impact": direction,
            "value": float(value)
        })

    return top_features