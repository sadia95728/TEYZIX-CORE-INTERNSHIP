import sqlite3

# Create or connect to database file
conn = sqlite3.connect("churn_db.sqlite3")

cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS churn_predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_index INTEGER,
    churn_probability REAL,
    risk_level TEXT,
    recommendations TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database created successfully!")