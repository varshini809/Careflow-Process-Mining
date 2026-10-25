import pandas as pd

df = pd.read_csv("careflow_100_patients_v3.csv")

# Check that it loaded and inspect its structure
print("First 5 rows:")
print(df.head())

print("\nRows and columns:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types and missing values:")
df.info()

import pandas as pd

df = pd.read_csv("careflow_100_patients_v3.csv")

# Combine Date and Time into one datetime column
df["DateTime"] = pd.to_datetime(
    df["Date"] + " " + df["Time"],
    format="%Y-%m-%d %H:%M"
)

# Sort each patient's activities by time
df = df.sort_values(["Case_ID", "DateTime"]).copy()

# Find the previous activity and its time for each patient
df["Previous_Activity"] = df.groupby("Case_ID")["Activity_Name"].shift(1)
df["Previous_DateTime"] = df.groupby("Case_ID")["DateTime"].shift(1)

# Calculate the wait time from the previous activity, in minutes
df["Wait_Minutes"] = (
    df["DateTime"] - df["Previous_DateTime"]
).dt.total_seconds() / 60

print(df[[
    "Case_ID",
    "Previous_Activity",
    "Activity_Name",
    "Wait_Minutes"
]].to_string(index=False))

# Summary of wait times (first activity per patient has no previous wait)
print("\nWait-time summary in minutes:")
print(df["Wait_Minutes"].describe())