import pandas as pd
import numpy as np

np.random.seed(42)

data = []

for i in range(1, 11):
    data.append([
        f"CUST_{1000+i}",
        np.random.randint(1, 15),   # call duration in minutes
        np.random.randint(0, 5),    # complaints
        np.random.choice(["Resolved", "Pending", "Escalated"]),
        np.random.choice(["High", "Medium", "Low"])
    ])

df = pd.DataFrame(data, columns=[
    "Customer_ID",
    "Call_Duration",
    "Complaints",
    "Call_Status",
    "Churn_Risk"
])

print(df)

df.to_csv("anonymized_call_list.csv", index=False)

print("\nAnonymized call list generated successfully!")



#output...

