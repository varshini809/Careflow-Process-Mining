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


# A loop-back occurs when a patient repeats an activity
df["Is_Loopback"] = (
    df.groupby("Case_ID")["Activity_Name"]
      .transform(lambda activities: activities.duplicated(keep="first"))
)

loopbacks = df[df["Is_Loopback"]]

print("\nLoop-back events:")
print(
    loopbacks[["Case_ID", "Activity_Name", "DateTime"]]
    .to_string(index=False)
)
print(f"\nTotal loop-back events: {len(loopbacks)}")

# Find the activity with the longest average wait before it starts
activity_waits = (
    df.dropna(subset=["Wait_Minutes"])
      .groupby("Activity_Name")["Wait_Minutes"]
      .agg(["mean", "median", "count"])
      .sort_values("mean", ascending=False)
)

print("\nWait-time summary by activity (minutes):")
print(activity_waits)

if not activity_waits.empty:
    slowest = activity_waits.index[0]
    print(
        f"\nSlowest activity by average preceding wait: {slowest} "
        f"({activity_waits.iloc[0]['mean']:.1f} minutes average)"
    )