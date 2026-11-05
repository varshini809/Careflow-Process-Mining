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

import pandas as pd

df = pd.read_csv("careflow_patients_data.csv")
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df = df.sort_values(["Case ID", "Timestamp"])

# Build each patient's ordered activity path
patient_paths = df.groupby("Case ID")["Activity Name"].agg(list)

# Count each activity occurrence after its first occurrence as a loop-back
def count_loopbacks(activities):
    seen = set()
    loopbacks = 0

    for activity in activities:
        if activity in seen:
            loopbacks += 1
        else:
            seen.add(activity)

    return loopbacks

loopbacks = patient_paths.apply(count_loopbacks)

print("Loop-backs per patient:")
print(loopbacks)

print("\nTotal loop-backs:", loopbacks.sum())
print("Patients with at least one loop-back:", (loopbacks > 0).sum())

# Calculate the time between each patient's consecutive activities
df["Previous Activity"] = df.groupby("Case ID")["Activity Name"].shift(1)
df["Previous Timestamp"] = df.groupby("Case ID")["Timestamp"].shift(1)
df["Wait Time (Hours)"] = (
    (df["Timestamp"] - df["Previous Timestamp"]).dt.total_seconds() / 3600
)

waits = df.dropna(subset=["Previous Timestamp"])

# Rank activity transitions by average wait
slowest_transitions = (
    waits.groupby(["Previous Activity", "Activity Name"])["Wait Time (Hours)"]
         .agg(["mean", "median", "count"])
         .sort_values("mean", ascending=False)
         .head(10)
)

print("\nTransitions with the longest average wait:")
print(slowest_transitions)

