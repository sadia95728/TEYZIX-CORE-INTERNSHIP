# Feature Engineering Report - Telco Churn Prediction System

## 1. Introduction
Feature engineering was performed to transform raw telecom customer data into a machine-learning-ready format for churn prediction.

## 2. Data Cleaning
- Missing values handled using median (numerical) and mode (categorical).
- Duplicate records removed to ensure data integrity.
- Inconsistent entries corrected during preprocessing.

## 3. Encoding Categorical Features
Categorical variables were converted into numerical format using:
- Label Encoding
- One-Hot Encoding

Key encoded features:
- Gender
- Contract Type
- Payment Method
- Internet Service

## 4. Feature Scaling
Numerical features were standardized using StandardScaler:
- Monthly Charges
- Total Charges
- Tenure

This improved model stability and performance.

## 5. Feature Selection
- Removed irrelevant identifiers (Customer ID).
- Selected features based on correlation with churn target.
- Retained only high-impact predictive variables.

## 6. Final Feature Set
Final dataset includes:
- Customer demographics
- Subscription details
- Billing information
- Service usage attributes

## 7. Conclusion
Feature engineering significantly improved model learning capability and ensured high-quality input for churn prediction modeling.