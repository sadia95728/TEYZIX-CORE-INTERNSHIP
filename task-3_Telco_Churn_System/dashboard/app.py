import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

from src.pipeline import run_batch_scoring
from src.shap_explainer import create_explainer, get_shap_values, get_top_features


st.set_page_config(page_title="Telco Churn Dashboard", layout="wide")

st.title("Telco Customer Churn Analytics Dashboard")
st.subheader("Machine Learning Churn Prediction System")

st.write(
    "This dashboard provides churn analytics, customer risk segmentation, "
    "model insights, and retention recommendations."
)

st.divider()


st.header("Model Performance Comparison")

metrics_df = pd.DataFrame({
    "Model": ["Logistic Regression", "XGBoost", "LightGBM"],
    "Accuracy": [0.804116, 0.792761, 0.790632],
    "Precision": [0.655063, 0.625767, 0.625397],
    "Recall": [0.553476, 0.545455, 0.526738],
    "F1 Score": [0.600000, 0.582857, 0.571843],
    "AUC": [0.842463, 0.837327, 0.832252]
})

st.dataframe(metrics_df)

fig = px.bar(
    metrics_df,
    x="Model",
    y="Accuracy",
    color="Model",
    text="Accuracy",
    title="Model Accuracy Comparison"
)

fig.update_traces(texttemplate='%{text:.3f}', textposition='outside')
st.plotly_chart(fig, use_container_width=True)

st.divider()



st.header("Customer Risk Segmentation & Drilldown")

raw_data = pd.read_csv("dataset/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# pipeline input copy
model_input = raw_data.copy()

# pipeline execution

results, X_processed = run_batch_scoring(model_input)

risk_counts = results["risk_level"].value_counts().reset_index()
risk_counts.columns = ["Risk", "Count"]

fig2 = px.pie(
    risk_counts,
    names="Risk",
    values="Count",
    title="Churn Risk Distribution"
)

st.plotly_chart(fig2, use_container_width=True)


customer_id = st.selectbox("Select Customer Index", results.index)

st.subheader("Customer Prediction")
st.write(results.loc[customer_id])

st.subheader("Recommended Actions")
st.write(results.loc[customer_id, "recommendations"])

st.subheader("Why this customer is at risk (SHAP Explanation)")

explainer = get_explainer()

# IMPORTANT: use processed features from pipeline
X_sample = X_processed.copy()

shap_values = explainer.shap_values(X_sample)

row = shap_values[customer_id]

importance = pd.DataFrame({
    "feature": X_sample.columns,
    "impact": row
})

importance["abs_impact"] = importance["impact"].abs()
importance = importance.sort_values("abs_impact", ascending=False)

st.write("Top 3 churn drivers:")

for i in range(3):
    feature = importance.iloc[i]["feature"]
    impact = importance.iloc[i]["impact"]

    direction = "increases churn risk" if impact > 0 else "reduces churn risk"

    st.write(f"• {feature} → {direction}")