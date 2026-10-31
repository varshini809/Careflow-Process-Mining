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
# 5. Validate unique patient pathways
print("\n5. PATIENT PATHWAY VALIDATION")

patient_paths = df.groupby("Case_ID")["Activity_Name"].apply(tuple)
unique_paths = patient_paths.nunique()

print("Unique patient pathways:", unique_paths)

if unique_paths >= 15:
    print("PASS: Dataset contains at least 15 unique pathways")
else:
    print("FAIL: Dataset contains fewer than 15 unique pathways")


# 6. Validate loop-backs
print("\n6. LOOP-BACK VALIDATION")

activity_counts = (
    df.groupby(["Case_ID", "Activity_Name"])
    .size()
    .reset_index(name="Visit_Count")
)

repeated_activities = activity_counts[
    activity_counts["Visit_Count"] > 1
]

loopback_patients = repeated_activities["Case_ID"].nunique()

print("Patients with loop-backs:", loopback_patients)

if loopback_patients > 0:
    print("PASS: Dataset contains loop-backs")
else:
    print("FAIL: No loop-backs found")


# 7. Validate long waiting intervals
print("\n7. LONG WAIT VALIDATION")

df["Wait_Minutes"] = (
    df.groupby("Case_ID")["Timestamp"]
    .diff()
    .dt.total_seconds() / 60
)

long_waits = df[df["Wait_Minutes"] >= 60]

print("Intervals of 60 minutes or more:", len(long_waits))

if len(long_waits) > 0:
    print("PASS: Dataset contains long waiting intervals")
else:
    print("FAIL: No long waiting intervals found")


# 8. Final Week 3 validation summary
print("\n8. WEEK 3 VALIDATION SUMMARY")

missing_values = df[
    ["Case_ID", "Activity_Name", "Date", "Time", "Department"]
].isnull().sum().sum()

empty_strings = (
    df[["Case_ID", "Activity_Name", "Date", "Time", "Department"]]
    .select_dtypes(include="object")
    .apply(lambda col: col.str.strip().eq("").sum())
    .sum()
)

duplicate_records = df[
    ["Case_ID", "Activity_Name", "Date", "Time", "Department"]
].duplicated().sum()

all_checks_passed = (
    unique_paths >= 15
    and loopback_patients > 0
    and len(long_waits) > 0
    and missing_values == 0
    and empty_strings == 0
    and duplicate_records == 0
    and len(invalid_cases) == 0
)

print("Missing values:", missing_values)
print("Empty strings:", empty_strings)
print("Duplicate records:", duplicate_records)
print("Chronological errors:", len(invalid_cases))

if all_checks_passed:
    print("\nSUCCESS: All Week 3 validation checks passed!")
else:
    print("\nWARNING: Some Week 3 validation checks failed!")

    # 9. Dataset Structure and Consistency Validation
print("\n9. DATASET STRUCTURE AND CONSISTENCY")

required_columns = [
    "Case_ID",
    "Activity_Name",
    "Date",
    "Time",
    "Department"
]

# Verify required columns
missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

print("Missing required columns:", missing_columns)

# Verify patient ID format
invalid_patient_ids = df[
    ~df["Case_ID"].astype(str).str.fullmatch(r"P\d{3}")
]

print("Invalid patient ID records:", len(invalid_patient_ids))

# Verify that every patient has a pathway
patient_event_counts = df.groupby("Case_ID").size()

print("Patients with no events:", (patient_event_counts == 0).sum())

# Check date consistency within each patient journey
patient_date_counts = df.groupby("Case_ID")["Date"].nunique()

inconsistent_dates = patient_date_counts[
    patient_date_counts > 1
]

print("Patients with multiple dates:", len(inconsistent_dates))

# Final structure validation
structure_valid = (
    len(missing_columns) == 0
    and len(invalid_patient_ids) == 0
    and len(inconsistent_dates) == 0
)

if structure_valid:
    print("\nPASS: Dataset structure and consistency verified!")
else:
    print("\nFAIL: Dataset structure or consistency issues detected!")