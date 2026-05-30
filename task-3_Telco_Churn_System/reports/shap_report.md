# SHAP Explainability Report - Churn Prediction System

## 1. Objective
The purpose of this report is to explain the predictions of the churn model using SHAP (SHapley Additive exPlanations). SHAP helps in understanding how each feature contributes to individual predictions.

## 2. Global Model Interpretation (Summary Plot)

A SHAP summary plot was used to understand the overall impact of features on churn prediction.

Key insights:
- Tenure is one of the strongest predictors of churn behavior.
- TotalCharges significantly influences customer retention behavior.
- Service-related features such as PhoneService also impact churn probability.

## 3. Local Explanation (Individual Customer Analysis)

A single customer (customer_index = 0) was analyzed using SHAP waterfall plot.

### Python Code Used:
```python
customer_index = 0

shap.plots.waterfall(
    shap.Explanation(
        values=shap_values[customer_index],
        base_values=explainer.expected_value,
        data=X.iloc[customer_index],
        feature_names=X.columns
    )
)
