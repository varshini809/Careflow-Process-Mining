import pandas as pd

df = pd.read_csv("careflow_patients_data.csv")

print(df.head(100))
print(df.columns)

import pandas as pd

df = pd.read_csv("careflow_patients_data.csv")

# Keep each patient's activities in timestamp order
df = df.sort_values(["Case ID", "Timestamp"])

# Build one activity sequence per patient
patient_paths = (
    df.groupby("Case ID")["Activity Name"]
      .agg(list)
)

# Count how many patients followed each exact sequence
path_counts = patient_paths.apply(
    lambda activities: " → ".join(activities)
).value_counts()

print("Patient paths and counts:")
print(path_counts)

# Count repeated activities within each patient's path
def count_loopbacks(activities):
    seen = set()
    loopbacks = 0

    for activity in activities:
        if activity in seen:
            loopbacks += 1
        else:
            seen.add(activity)

    return loopbacks

loopbacks_per_patient = patient_paths.apply(count_loopbacks)

print("\nLoop-backs per patient:")
print(loopbacks_per_patient)

print("\nTotal loop-backs:", loopbacks_per_patient.sum())