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

# 9. Detailed Loop-Back Analysis
print("\n8. DETAILED LOOP-BACK ANALYSIS")

# Count visits to each activity for every patient
activity_visits = (
    df.groupby(["Case_ID", "Activity_Name"])
    .size()
    .reset_index(name="Visit_Count")
)

# Identify activities visited more than once
repeated_activities = activity_visits[
    activity_visits["Visit_Count"] > 1
]

# Count patients with at least one repeated activity
patients_with_loopbacks = repeated_activities["Case_ID"].nunique()

print("Patients with at least one loop-back:", patients_with_loopbacks)

# Count patients revisiting each activity
loopback_counts = (
    repeated_activities.groupby("Activity_Name")["Case_ID"]
    .nunique()
    .sort_values(ascending=False)
)

print("\nLoop-backs by activity:")
print(loopback_counts.to_string())

# 10. Hospital Bottleneck Analysis
print("\n9. HOSPITAL BOTTLENECK ANALYSIS")

# Identify the previous activity for each patient
df["Previous_Activity"] = (
    df.groupby("Case_ID")["Activity_Name"].shift(1)
)

# Calculate elapsed time between consecutive activities
df["Transition_Minutes"] = (
    df.groupby("Case_ID")["Timestamp"]
    .diff()
    .dt.total_seconds() / 60
)

# Exclude the first event of each patient
transitions = df.dropna(
    subset=["Previous_Activity", "Transition_Minutes"]
).copy()

# Calculate average time for each activity transition
bottlenecks = (
    transitions.groupby(["Previous_Activity", "Activity_Name"])
    ["Transition_Minutes"]
    .agg(["mean", "count"])
    .reset_index()
)

# Sort by longest average transition time
bottlenecks = bottlenecks.sort_values(
    "mean", ascending=False
)

print("\nTop 5 longest average activity transitions:")

print(
    bottlenecks.head(5).to_string(
        index=False,
        formatters={"mean": "{:.2f}".format}
    )
)


# 11. Department-Level Delay Analysis
print("\n10. DEPARTMENT-LEVEL DELAY ANALYSIS")

# Calculate elapsed time before entering each department
df["Department_Interval_Minutes"] = (
    df.groupby("Case_ID")["Timestamp"]
    .diff()
    .dt.total_seconds() / 60
)

# Group intervals by destination department
department_delays = (
    df.groupby("Department")["Department_Interval_Minutes"]
    .agg(["mean", "max", "count"])
    .sort_values("mean", ascending=False)
)

print("\nAverage interval before each department:")
print(department_delays.round(2).to_string())

# Count long intervals by destination department
long_department_delays = df[
    df["Department_Interval_Minutes"] >= 60
]

long_delay_counts = (
    long_department_delays["Department"]
    .value_counts()
)

print("\nLong intervals (60+ minutes) by department:")
print(long_delay_counts.to_string())

# 12. Patient Pathway Frequency Analysis
print("\n11. PATIENT PATHWAY FREQUENCY ANALYSIS")

# Create a pathway for each patient
patient_pathways = (
    df.groupby("Case_ID", sort=False)["Activity_Name"]
    .apply(tuple)
)

# Count patients following each pathway
pathway_frequency = patient_pathways.value_counts()

total_patients = len(patient_pathways)

print("\nTotal unique pathways:", len(pathway_frequency))

print("\nTop 5 most common patient pathways:")

for rank, (pathway, count) in enumerate(
    pathway_frequency.head(5).items(), start=1
):
    percentage = (count / total_patients) * 100

    print(f"\nPathway {rank}:")
    print("Journey:", " -> ".join(pathway))
    print("Patients:", count)
    print(f"Percentage: {percentage:.2f}%")

    # 13. Emergency vs Routine Patient Journey Analysis
print("\n12. EMERGENCY VS ROUTINE PATIENT ANALYSIS")

# Ensure events are ordered chronologically
journey_df = df.sort_values(["Case_ID", "Timestamp"]).copy()

# Calculate patient-level journey statistics
patient_stats = (
    journey_df.groupby("Case_ID")
    .agg(
        Total_Activities=("Activity_Name", "count"),
        Start_Time=("Timestamp", "min"),
        End_Time=("Timestamp", "max")
    )
)

# Calculate journey duration in minutes
patient_stats["Duration_Minutes"] = (
    patient_stats["End_Time"] - patient_stats["Start_Time"]
).dt.total_seconds() / 60

# Identify emergency patients based on their pathway
# Emergency patients go directly to Doctor as their first activity
first_activities = (
    journey_df.groupby("Case_ID")["Activity_Name"].first()
)

patient_stats["Patient_Type"] = first_activities.apply(
    lambda activity: "Emergency"
    if activity == "Doctor"
    else "Routine"
)

# Compare patient groups
comparison = (
    patient_stats.groupby("Patient_Type")
    .agg(
        Patients=("Total_Activities", "count"),
        Avg_Activities=("Total_Activities", "mean"),
        Avg_Duration_Minutes=("Duration_Minutes", "mean"),
        Max_Duration_Minutes=("Duration_Minutes", "max")
    )
)

print("\nEmergency vs Routine Comparison:")
print(comparison.round(2).to_string())

# 14. Patient Journey Duration Distribution Analysis

print("\n13. PATIENT JOURNEY DURATION DISTRIBUTION")

# Combine Date and Time columns into a datetime
duration_df = df.copy()

duration_df["Journey_Timestamp"] = pd.to_datetime(
    duration_df["Date"].astype(str) + " " +
    duration_df["Time"].astype(str)
)

# Calculate the start and end time for each patient
patient_durations = (
    duration_df.groupby("Case_ID")["Journey_Timestamp"]
    .agg(["min", "max"])
)

# Calculate total journey duration in minutes
patient_durations["Duration_Minutes"] = (
    patient_durations["max"] - patient_durations["min"]
).dt.total_seconds() / 60

# Display overall journey duration statistics
print("\nPatient Journey Duration Statistics:")

print(
    f"Shortest Journey: "
    f"{patient_durations['Duration_Minutes'].min():.2f} minutes"
)

print(
    f"Longest Journey: "
    f"{patient_durations['Duration_Minutes'].max():.2f} minutes"
)

print(
    f"Average Journey: "
    f"{patient_durations['Duration_Minutes'].mean():.2f} minutes"
)

print(
    f"Median Journey: "
    f"{patient_durations['Duration_Minutes'].median():.2f} minutes"
)

# Group patients into journey duration categories
duration_bins = [0, 60, 120, 180, 240, float("inf")]

duration_labels = [
    "0-60 minutes",
    "61-120 minutes",
    "121-180 minutes",
    "181-240 minutes",
    "More than 240 minutes"
]

patient_durations["Duration_Category"] = pd.cut(
    patient_durations["Duration_Minutes"],
    bins=duration_bins,
    labels=duration_labels,
    include_lowest=True
)

# Count patients in each category
duration_distribution = (
    patient_durations["Duration_Category"]
    .value_counts()
    .sort_index()
)

print("\nPatient Journey Duration Distribution:")
print(duration_distribution.to_string())

print(
    f"\nTotal Patients Analyzed: "
    f"{len(patient_durations)}"
)

# 15. Department Transition Frequency Analysis

print("\n14. DEPARTMENT TRANSITION FREQUENCY ANALYSIS")

# Create a copy of the dataset
transition_df = df.copy()

# Combine Date and Time for chronological ordering
transition_df["Transition_Timestamp"] = pd.to_datetime(
    transition_df["Date"].astype(str) + " " +
    transition_df["Time"].astype(str)
)

# Sort activities by patient and timestamp
transition_df = transition_df.sort_values(
    ["Case_ID", "Transition_Timestamp"]
)

# Identify the next department visited by each patient
transition_df["Next_Department"] = (
    transition_df.groupby("Case_ID")["Department"].shift(-1)
)

# Exclude the final activity of each patient
transitions = transition_df.dropna(
    subset=["Next_Department"]
).copy()

# Count total and unique transitions
transition_counts = (
    transitions.groupby(["Department", "Next_Department"])
    .agg(
        Frequency=("Case_ID", "count"),
        Unique_Patients=("Case_ID", "nunique")
    )
    .sort_values("Frequency", ascending=False)
)

print(f"\nTotal Department Transitions: {len(transitions)}")

print(
    f"Unique Department Transitions: "
    f"{len(transition_counts)}"
)

print("\nTop 10 Most Frequent Department Transitions:")
print(transition_counts.head(10).to_string())

# Identify consecutive visits to the same department
same_department = transitions[
    transitions["Department"] == transitions["Next_Department"]
]

print(
    f"\nConsecutive Same-Department Transitions: "
    f"{len(same_department)}"
)

# Identify patients who revisit a department later in their journey
department_revisits = (
    transition_df.groupby("Case_ID")["Department"]
    .apply(lambda departments: departments.duplicated().any())
)

print(
    f"Patients Revisiting a Department: "
    f"{department_revisits.sum()}"
)

print("\nDepartment Transition Analysis Completed.")
print("\n" + "=" * 50)
print("CAREFLOW DATASET ANALYSIS COMPLETED")
print("=" * 50)