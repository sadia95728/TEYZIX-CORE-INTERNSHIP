import pandas as pd
import numpy as np

np.random.seed(42)

weeks = ["Week 1", "Week 2", "Week 3", "Week 4"]

data = []

for week in weeks:
    for i in range(5):
        churn_score = np.random.uniform(0.2, 0.9)

        if churn_score > 0.7:
            risk = "High"
        elif churn_score > 0.4:
            risk = "Medium"
        else:
            risk = "Low"

        data.append([week, i, churn_score, risk])

df = pd.DataFrame(data, columns=["Week", "Customer_ID", "Churn_Score", "Risk_Level"])

print(df)


df.to_csv("weekly_scoring_output.csv", index=False)

print("\nWeekly scoring simulation completed successfully!")

