import pandas as pd

# Load the CareFlow V3 dataset
df = pd.read_csv("careflow_100_patients_v3.csv")

# 1. Check missing values
print("Missing values:")
print(df.isnull().sum())

# 2. Check duplicate records
print("\nDuplicate records:", df.duplicated().sum())

# 3. Check timestamp order
df["Timestamp"] = pd.to_datetime(
    df["Date"].astype(str) + " " + df["Time"].astype(str)
)

invalid_cases = []

for case_id, group in df.groupby("Case_ID", sort=False):
    if not group["Timestamp"].is_monotonic_increasing:
        invalid_cases.append(case_id)

print("\nPatients with incorrect time order:", len(invalid_cases))
print("Patient IDs:", invalid_cases)

# 4. Check total patients and events
print("\nTotal patients:", df["Case_ID"].nunique())
print("Total events:", len(df))