# CareFlow - Dataset Summary and Analysis
# Analyzes patient journeys from the V3 dataset

import pandas as pd

# 1. Load the dataset
df = pd.read_csv("careflow_100_patients_v3.csv")

# Combine Date and Time into one timestamp
df["Timestamp"] = pd.to_datetime(
    df["Date"].astype(str) + " " + df["Time"].astype(str)
)

# Sort events chronologically for each patient
df = df.sort_values(["Case_ID", "Timestamp"])

print("=" * 50)
print("CAREFLOW V3 - DATASET SUMMARY")
print("=" * 50)

# 2. Total patients and events
total_patients = df["Case_ID"].nunique()
total_events = len(df)

print("\n1. DATASET OVERVIEW")
print("Total patients:", total_patients)
print("Total events:", total_events)

# 3. Unique patient pathways
patient_paths = df.groupby("Case_ID")["Activity_Name"].apply(tuple)

unique_paths = patient_paths.nunique()

print("\n2. PATIENT PATHWAYS")
print("Unique patient pathways:", unique_paths)

# 4. Most frequently visited departments
print("\n3. DEPARTMENT ACTIVITY COUNTS")

department_counts = df["Department"].value_counts()

print(department_counts.to_string())

# 5. Average patient journey duration
print("\n4. PATIENT JOURNEY DURATION")

patient_duration = df.groupby("Case_ID")["Timestamp"].agg(
    ["min", "max"]
)

patient_duration["Duration_Minutes"] = (
    patient_duration["max"] - patient_duration["min"]
).dt.total_seconds() / 60

average_duration = patient_duration["Duration_Minutes"].mean()

print(f"Average patient journey duration: {average_duration:.2f} minutes")
print(
    f"Longest patient journey: "
    f"{patient_duration['Duration_Minutes'].max():.2f} minutes"
)

# 6. Patients with repeated Doctor visits
print("\n5. REPEATED DOCTOR VISITS")

doctor_visits = (
    df[df["Activity_Name"] == "Doctor"]
    .groupby("Case_ID")
    .size()
)

repeat_doctor_patients = (doctor_visits > 1).sum()

print("Patients with repeated Doctor visits:", repeat_doctor_patients)

# 7. Daily patient counts
print("\n6. DAILY PATIENT COUNTS")

daily_patients = df.groupby("Date")["Case_ID"].nunique()

print("Days covered:", len(daily_patients))
print("Minimum patients per day:", daily_patients.min())
print("Maximum patients per day:", daily_patients.max())

# 8. Waiting Time Analysis
print("\n7. WAITING TIME ANALYSIS")

# Calculate time difference between consecutive activities
# for each patient
df["Wait_Minutes"] = (
    df.groupby("Case_ID")["Timestamp"]
    .diff()
    .dt.total_seconds() / 60
)

# Remove the first activity of each patient
# because it has no previous activity
waiting_times = df["Wait_Minutes"].dropna()

# Calculate waiting time statistics
average_wait = waiting_times.mean()
longest_wait = waiting_times.max()

# Count patients experiencing long waits
patients_wait_60 = df.loc[
    df["Wait_Minutes"] >= 60, "Case_ID"
].nunique()

patients_wait_120 = df.loc[
    df["Wait_Minutes"] >= 120, "Case_ID"
].nunique()

print(f"Average interval between activities: {average_wait:.2f} minutes")
print(f"Longest interval between activities: {longest_wait:.2f} minutes")

print("Patients with intervals >= 60 minutes:", patients_wait_60)
print("Patients with intervals >= 120 minutes:", patients_wait_120)

print("\n" + "=" * 50)
print("CAREFLOW DATASET ANALYSIS COMPLETED")
print("=" * 50)