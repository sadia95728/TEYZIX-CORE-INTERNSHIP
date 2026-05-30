import sqlite3

conn = sqlite3.connect("churn_db.sqlite3")
cur = conn.cursor()

# Total records
cur.execute("SELECT COUNT(*) FROM churn_predictions")
total = cur.fetchone()[0]

# High risk customers
cur.execute("SELECT COUNT(*) FROM churn_predictions WHERE risk_level='High'")
high = cur.fetchone()[0]

# Medium risk customers
cur.execute("SELECT COUNT(*) FROM churn_predictions WHERE risk_level='Medium'")
medium = cur.fetchone()[0]

# Low risk customers
cur.execute("SELECT COUNT(*) FROM churn_predictions WHERE risk_level='Low'")
low = cur.fetchone()[0]

# Average churn probability
cur.execute("SELECT AVG(churn_probability) FROM churn_predictions")
avg_prob = cur.fetchone()[0]

print("\n===== CHURN DATABASE FINAL REPORT =====")
print("Total Predictions:", total)
print("High Risk Customers:", high)
print("Medium Risk Customers:", medium)
print("Low Risk Customers:", low)
print("Average Churn Probability:", round(avg_prob, 4))

conn.close()