# 🧠 Telco Customer Churn Prediction System

## 📌 Project Overview

This project is a complete end-to-end Machine Learning based Telco Customer Churn Prediction System developed to identify customers who are likely to leave telecom services. The system integrates data preprocessing, feature engineering, machine learning modeling, explainable AI (SHAP), weekly scoring simulation, database integration, and business impact analysis into a unified pipeline.

The project demonstrates a production-style churn prediction workflow with automation, reporting, and explainability.
# 🎯 Objectives

* Predict customer churn probability using machine learning
* Compare multiple ML models for best performance
* Explain predictions using SHAP explainability
* Simulate weekly churn monitoring
* Store churn insights in a database
* Generate business-oriented analytics reports
* Demonstrate a reproducible ML pipeline

# ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* LightGBM
* SHAP
* SQLite
* Streamlit
* Joblib
* Matplotlib

# 🏗️ Project Pipeline

1. Data Cleaning & Preprocessing
2. Feature Engineering
3. Model Training & Evaluation
4. SHAP Explainability Analysis
5. Weekly Scoring Simulation
6. Customer Segmentation & Recommendations
7. Database Integration
8. Business Impact Reporting
9. Dashboard Visualization
# 📂 Project Structure

```bash
task-3_TC-INT-20260430-142_SadiaSalamat/

├── dashboard/
│   └── app.py
│
├── database/
│   ├── churn_db.py
│   ├── churn_db.sqlite3
│   ├── database_data.py
│   └── db_report.py
│
├── dataset/
│   └── raw dataset
│
├── models/
│   ├── lightgbm_model.pkl
│   ├── logistic_model.pkl
│   ├── model_feature.pkl
│   └── xgboost_model.pkl
│
├── notebook/
│   ├── comparison_model.ipynb
│   ├── data_cleaning.ipynb
│   ├── feature_engineering.ipynb
│   ├── model.train.ipynb
│   ├── pipeline_test.ipynb
│   └── shap_analysis.ipynb
│
├── outputs/
│   ├── anonymized_call_list.csv
│   ├── anonymized_call_list.py
│   ├── weekly_scoring_output.csv
│   └── weekly_scoring.py
│
├── reports/
│   ├── business_impact.md
│   ├── feature_engineering_report.md
│   ├── model_evaluation_report.md
│   └── shap_report.md
│
├── screenshot/
│   ├── png1
│   ├── png2
│   └── png3
│
├── src/
│   ├── __init__.py
│   ├── pipeline.py
│   ├── predict.py
│   ├── recommendation.py
│   ├── segmentation.py
│   ├── shap_explainer.py
│   └── utils.py
│
├── main.py
├── requirement.txt
└── Readme.md
```

# 🤖 Machine Learning Models Used

| Model               | Accuracy | Precision | Recall | F1 Score | AUC    |
| ------------------- | -------- | --------- | ------ | -------- | ------ |
| Logistic Regression | 0.8041   | 0.6551    | 0.5535 | 0.6000   | 0.8425 |
| XGBoost             | 0.7928   | 0.6258    | 0.5455 | 0.5829   | 0.8373 |
| LightGBM            | 0.7906   | 0.6254    | 0.5267 | 0.5718   | 0.5718 |

### Final Selected Model:

**Logistic Regression** was selected as the final deployment model due to its superior AUC-ROC score and strong generalization capability.

# 📈 SHAP Explainability

SHAP (SHapley Additive exPlanations) was used to:

* Explain global feature importance
* Interpret individual customer churn predictions
* Identify major churn-driving features

Key churn drivers identified:

* Tenure
* TotalCharges
* PhoneService_Yes

# 🗄️ Database Integration

SQLite database was integrated to:

* Store churn predictions
* Maintain customer risk records
* Generate analytics reports

# 📊 Weekly Scoring Simulation

The system simulates churn predictions across multiple weeks to monitor customer risk changes over time.

Generated Outputs:

* weekly_scoring_output.csv
* anonymized_call_list.csv

# 💼 Business Impact Analysis

Estimated Business Value:

* 10% churn reduction target
* Estimated revenue saved: **$60,000 per 1000 customers**

Benefits:

* Early churn identification
* Improved customer retention
* Better marketing targeting
* Revenue optimization

---

# ▶️ How to Run the Project

## Install Requirements

```bash
pip install -r requirement.txt
```
## Run Complete Pipeline

```bash
python main.py
```

# Dashboard & Screenshots

Project screenshots and dashboard outputs are available in the `screenshot/` folder.
# 👩‍💻 Author

## Sadia Salamat

BS Computer Science Student
Minahj University Lahore
Passionate about Machine Learning, AI, Deep learning, and Deployment.
# 📌 Conclusion

This project demonstrates a complete industry-style churn prediction system integrating machine learning, explainable AI, database systems, business analytics, and automation into a single reproducible pipeline.
