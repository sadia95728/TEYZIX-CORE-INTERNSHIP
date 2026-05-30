import sqlite3

conn = sqlite3.connect("churn_db.sqlite3")
cur = conn.cursor()

sample_data = [
    (1, 0.82, "High", "Offer discount"),
    (2, 0.65, "Medium", "Send email campaign"),
    (3, 0.30, "Low", "No action"),
    (4, 0.91, "High", "Call customer support"),
    (5, 0.40, "Medium", "Engagement offer")
]

cur.executemany("""
INSERT INTO churn_predictions 
(customer_index, churn_probability, risk_level, recommendations)
VALUES (?, ?, ?, ?)
""", sample_data)

conn.commit()
conn.close()

print("Dummy data inserted successfully!")