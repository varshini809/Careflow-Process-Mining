import pandas as pd

df = pd.read_csv("careflow_patients_data.csv")

# Ensure timestamps are interpreted as dates, then order each patient's activities
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df = df.sort_values(["Case ID", "Timestamp"])

# Build one activity sequence per patient
patient_paths = (
    df.groupby("Case ID")["Activity Name"]
      .agg(tuple)
)

# Count exact sequences and show the five most common
top_5_paths = patient_paths.value_counts().head(5)

print("Top 5 patient paths:")
for rank, (path, count) in enumerate(top_5_paths.items(), start=1):
    print(f"{rank}. {' → '.join(path)} — {count} patients")


#checking wait time and activitiesm8
import pandas as pd

df = pd.read_csv("careflow_patients_data.csv")

df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df = df.sort_values(["Case ID", "Timestamp"])

# Compare each activity's timestamp with the previous activity
df["Previous Activity"] = df.groupby("Case ID")["Activity Name"].shift(1)
df["Previous Timestamp"] = df.groupby("Case ID")["Timestamp"].shift(1)

df["Wait Time"] = df["Timestamp"] - df["Previous Timestamp"]
df["Wait Time (Hours)"] = df["Wait Time"].dt.total_seconds() / 3600

# The first activity in each patient's path has no preceding wait time
waits = df.dropna(subset=["Previous Timestamp"])

print(waits[[
    "Case ID", "Previous Activity", "Activity Name",
    "Previous Timestamp", "Timestamp", "Wait Time (Hours)"
]].head(20))

print("\nAverage wait time between activities:")
print(waits["Wait Time (Hours)"].mean())

print("\nAverage wait by activity transition:")
print(
    waits.groupby(["Previous Activity", "Activity Name"])["Wait Time (Hours)"]
         .mean()
         .sort_values(ascending=False)
         .head(10)
)