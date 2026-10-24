import pandas as pd

# Load the existing CareFlow dataset
df = pd.read_csv("careflow_100_patients_cleaned.csv")

# Display the first 10 rows
print(df.head(10))

# Display total patients and records
print("\nTotal Patients:", df["Case_ID"].nunique())
print("Total Records:", len(df))

# Display column names
print("\nColumns:", df.columns.tolist())
# Convert Timestamp into datetime format
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Create separate Date and Time columns
df["Date"] = df["Timestamp"].dt.strftime("%Y-%m-%d")
df["Time"] = df["Timestamp"].dt.strftime("%H:%M")

# Display the updated dataset
print("\nDataset with Date and Time:")
print(df.head(10))
# Assign departments based on hospital activities

department_mapping = {
    "Registration": "Reception",
    "Vitals": "Nursing",
    "Triage": "Emergency",
    "Doctor": "Consultation",
    "Billing Counter": "Billing",
    "Pathology": "Laboratory",
    "Pathology report": "Laboratory",
    "X-Ray": "Radiology",
    "X-Ray report": "Radiology",
    "Pharmacy": "Pharmacy",
    "Discharge": "Discharge"
}

# Create Department column
df["Department"] = df["Activity_Name"].map(department_mapping)

# Check whether any activities have missing departments
print("\nMissing Departments:", df["Department"].isna().sum())

# Display the updated dataset
print("\nDataset with Department:")
print(df.head(10).to_string(index=False))
# Remove the Timestamp column
df = df.drop(columns=["Timestamp"])

# Arrange columns in the required order
df = df[["Case_ID", "Activity_Name", "Date", "Time", "Department"]]

# Display updated dataset
print("\nFinal Dataset:")
print(df.head(10).to_string(index=False))
# Export the updated dataset to CSV
df.to_csv("careflow_100_patients_v2.csv", index=False)

print("\nCSV file created successfully!")
# Count how many times each patient visits Triage
triage_visits = df[df["Activity_Name"] == "Triage"]

triage_counts = triage_visits.groupby("Case_ID").size()

# Identify patients who visited Triage more than once
loopback_patients = triage_counts[triage_counts > 1]

print("\nPatients with Triage loop-backs:", len(loopback_patients))
print(loopback_patients.head(10))
# Combine Date and Time temporarily for calculations
df["Event_DateTime"] = pd.to_datetime(
    df["Date"] + " " + df["Time"]
)

# Display the first 5 records
print("\nDate and Time combined for calculations:")
print(df[["Case_ID", "Activity_Name", "Event_DateTime"]].head())
# Identify patients who already have Triage loop-backs
triage_counts = (
    df[df["Activity_Name"] == "Triage"]
    .groupby("Case_ID")
    .size()
)

existing_loopbacks = set(
    triage_counts[triage_counts > 1].index
)

# Find patients without existing Triage loop-backs
all_patients = sorted(df["Case_ID"].unique())

eligible_patients = [
    patient for patient in all_patients
    if patient not in existing_loopbacks
]

# Select 14 patients for additional loop-backs
selected_patients = eligible_patients[:14]

print("\nPatients selected for additional loop-backs:")
print(selected_patients)

print("\nExisting loop-back patients:", len(existing_loopbacks))
print("Additional patients selected:", len(selected_patients))
print("Expected total:", len(existing_loopbacks) + len(selected_patients))
from datetime import timedelta

# Store the updated patient journeys
updated_patients = []

for patient_id, patient_data in df.groupby("Case_ID", sort=False):

    patient_data = patient_data.copy()

    # Add loop-backs only to the 14 selected patients
    if patient_id in selected_patients:

        # Find the last Doctor visit
        doctor_rows = patient_data[
            patient_data["Activity_Name"] == "Doctor"
        ]

        if not doctor_rows.empty:

            last_doctor_index = doctor_rows.index[-1]

            # Find the position of that Doctor visit
            position = patient_data.index.get_loc(last_doctor_index)

            # Split the journey after the Doctor visit
            before = patient_data.iloc[:position + 1].copy()
            after = patient_data.iloc[position + 1:].copy()

            # Add 90 minutes to subsequent activities
            after["Event_DateTime"] += timedelta(minutes=90)

            # Create the additional loop-back events
            doctor_time = before["Event_DateTime"].iloc[-1]

            new_events = pd.DataFrame([
                {
                    "Case_ID": patient_id,
                    "Activity_Name": "Triage",
                    "Event_DateTime": doctor_time + timedelta(minutes=30),
                    "Department": "Emergency"
                },
                {
                    "Case_ID": patient_id,
                    "Activity_Name": "Doctor",
                    "Event_DateTime": doctor_time + timedelta(minutes=60),
                    "Department": "Consultation"
                }
            ])

            # Combine the updated journey
            patient_data = pd.concat(
                [before, new_events, after],
                ignore_index=True
            )

    updated_patients.append(patient_data)

# Combine all patient journeys
df = pd.concat(updated_patients, ignore_index=True)

# Recreate Date and Time from updated timestamps
df["Date"] = df["Event_DateTime"].dt.strftime("%Y-%m-%d")
df["Time"] = df["Event_DateTime"].dt.strftime("%H:%M")

# Count patients with Triage loop-backs
triage_counts = (
    df[df["Activity_Name"] == "Triage"]
    .groupby("Case_ID")
    .size()
)

loopback_patients = triage_counts[triage_counts > 1]

print("\nUpdated patient count:", df["Case_ID"].nunique())
print("Updated event records:", len(df))
print("Patients with Triage loop-backs:", len(loopback_patients))
# Check whether events are in chronological order

chronological_errors = []

for patient_id, patient_data in df.groupby("Case_ID", sort=False):

    timestamps = patient_data["Event_DateTime"]

    if not timestamps.is_monotonic_increasing:
        chronological_errors.append(patient_id)

print("\nChronological Validation Results:")
print("Total patients:", df["Case_ID"].nunique())
print("Patients with chronological errors:", len(chronological_errors))

if chronological_errors:
    print("Patients requiring correction:", chronological_errors)
else:
    print("All patient journeys are in chronological order!")
    import random
from datetime import timedelta

# Set seed so results remain consistent
random.seed(42)

# Define additional delays in minutes
delay_mapping = {
    ("Triage", "Doctor"): (60, 120),
    ("Pathology", "Pathology report"): (90, 150),
    ("X-Ray", "X-Ray report"): (45, 90)
}

delayed_patients = set()
delay_count = 0

updated_patients = []

for patient_id, patient_data in df.groupby("Case_ID", sort=False):

    patient_data = patient_data.copy().reset_index(drop=True)

    # Apply delays to selected patients
    if random.random() < 0.4:

        for i in range(len(patient_data) - 1):

            current_activity = patient_data.loc[i, "Activity_Name"]
            next_activity = patient_data.loc[i + 1, "Activity_Name"]

            transition = (current_activity, next_activity)

            if transition in delay_mapping:

                min_delay, max_delay = delay_mapping[transition]
                additional_delay = random.randint(min_delay, max_delay)

                # Shift the next event and all subsequent events
                patient_data.loc[
                    i + 1:, "Event_DateTime"
                ] += timedelta(minutes=additional_delay)

                delay_count += 1
                delayed_patients.add(patient_id)

    updated_patients.append(patient_data)

# Combine updated journeys
df = pd.concat(updated_patients, ignore_index=True)

# Update Date and Time after adding delays
df["Date"] = df["Event_DateTime"].dt.strftime("%Y-%m-%d")
df["Time"] = df["Event_DateTime"].dt.strftime("%H:%M")

print("\nDelay Simulation Results:")
print("Patients affected by additional delays:", len(delayed_patients))
print("Total delays introduced:", delay_count)
print("Total event records:", len(df))
# Final validation of the updated dataset

# Check missing values
print("\nMissing Values:")
print(df[["Case_ID", "Activity_Name", "Date", "Time", "Department"]].isnull().sum())

# Check chronological order after adding delays
chronological_errors = []

for patient_id, patient_data in df.groupby("Case_ID", sort=False):
    if not patient_data["Event_DateTime"].is_monotonic_increasing:
        chronological_errors.append(patient_id)

print("\nFinal Chronological Validation:")
print("Patients with chronological errors:", len(chronological_errors))

# Check patient and event counts
print("\nFinal Dataset Summary:")
print("Total Patients:", df["Case_ID"].nunique())
print("Total Records:", len(df))
print("Total Columns:", 5)
# Select the final five columns
final_df = df[
    ["Case_ID", "Activity_Name", "Date", "Time", "Department"]
].copy()

from datetime import datetime, timedelta

# Distribute 100 patients across 30 days
start_date = datetime(2026, 10, 1)

# Get unique patient IDs
patient_ids = final_df["Case_ID"].unique()

# Assign one date to each patient
patient_dates = {}

for i, patient_id in enumerate(patient_ids):
    day_offset = i % 30

    patient_date = start_date + timedelta(days=day_offset)

    patient_dates[patient_id] = patient_date.strftime("%Y-%m-%d")

# Apply the same date to every activity of each patient
final_df["Date"] = final_df["Case_ID"].map(patient_dates)

# Verify patients per day
print("\nPatients per day:")
print(final_df.groupby("Date")["Case_ID"].nunique())

# Verify each patient has only one date
multiple_dates = (
    final_df.groupby("Case_ID")["Date"].nunique() > 1
).sum()

print("\nPatients with multiple dates:", multiple_dates)

# Export the final dataset
final_df.to_csv(
    "careflow_100_patients_final.csv",
    index=False
)

print("\nFinal CSV exported successfully!")

print("Total Patients:", final_df["Case_ID"].nunique())
print("Total Records:", len(final_df))