# Model Evaluation Report - Telco Churn Prediction System

## 1. Objective
The objective of this phase was to evaluate multiple machine learning models for churn prediction and select the best-performing model based on evaluation metrics.

## 2. Models Trained

The following models were trained and evaluated:

- Logistic Regression  
- XGBoost Classifier  
- LightGBM Classifier  

## 3. Evaluation Metrics

Models were compared using:

- Accuracy  
- Precision  
- Recall  
- F1 Score  
- AUC-ROC  

## 4. Model Performance Comparison

| Model               | Accuracy | Precision | Recall | F1 Score | AUC |
|--------------------|----------|-----------|--------|----------|------|
| Logistic Regression | 0.8041   | 0.6551    | 0.5535 | 0.6000   | 0.8425 |
| XGBoost             | 0.7928   | 0.6258    | 0.5455 | 0.5829   | 0.8373 |
| LightGBM            | 0.7906   | 0.6254    | 0.5267 | 0.5718   | 0.8323 |

## 5. Final Model Selection

Although advanced models such as XGBoost and LightGBM were used, **Logistic Regression performed best in terms of AUC-ROC (0.8425)**, indicating:

- Strong class separability  
- Better generalization on unseen data  
- More stable performance compared to complex models  

## 6. Conclusion

Logistic Regression was selected as the final model for deployment due to its superior AUC score and balanced performance across evaluation metrics.