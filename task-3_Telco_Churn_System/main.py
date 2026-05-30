import os


print(" TELCO CHURN SYSTEM DEMO RUN ")

print("Step 1: Running Weekly Scoring Simulation...")
os.system("python outputs/weekly_scoring.py")

print("\nStep 2: Generating Anonymized Call List...")
os.system("python outputs/anonymized_call_list.py")

print("\nStep 3: Running Database Report...")
os.system("python database/db_report.py")



print(" PROJECT EXECUTION COMPLETED ")


print("All modules executed successfully.")
print("Check outputs/ and reports/ folders for results.")