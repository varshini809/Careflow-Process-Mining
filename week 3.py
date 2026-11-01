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