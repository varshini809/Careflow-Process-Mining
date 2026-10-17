# CareFlow: Clinical Pathway Process Mining

## 1. Project Overview

CareFlow is a healthcare data analytics project focused on analyzing patient journeys through different hospital departments.

The project uses synthetic hospital event logs generated using Python to study patient movement, identify delays, detect loop-backs, and understand potential bottlenecks in hospital workflows.

The generated CSV dataset provides structured data for process mining, data analysis, and visualization.

### Project Objectives

* Generate synthetic patient event logs using Python.
* Simulate different hospital patient journeys.
* Introduce delays and loop-backs into patient pathways.
* Generate and export patient records into CSV format.
* Validate the generated dataset.
* Prepare the dataset for process mining and visualization.

---

## 2. Technologies Used

| Technology            | Purpose                                   |
| --------------------- | ----------------------------------------- |
| Python                | Patient event-log generation              |
| datetime              | Handling dates and timestamps             |
| timedelta             | Calculating time intervals                |
| random                | Simulating variations in patient journeys |
| csv                   | Creating and exporting CSV files          |
| VS Code               | Code development and execution            |
| Excel / Google Sheets | Viewing and inspecting CSV data           |

The CSV generator uses Python's standard library and does not require additional packages.

---

## 3. Project Structure

```text
CareFlow/
│
├── careflow_generator.py
├── careflow_generated_100_patients.csv
├── careflow_100_patients_cleaned.csv
├── careflow_validation_report.txt
└── README.md
```

### File Descriptions

**careflow_generator.py**

Python script that generates synthetic hospital patient journeys with timestamps, delays, and loop-backs.

**careflow_generated_100_patients.csv**

CSV dataset automatically created by the Python generator. It contains 100 patient journeys and 1,134 event records.

**careflow_100_patients_cleaned.csv**

Cleaned version of the original synthetic patient dataset, with standardized column names and full datetime values.

**careflow_validation_report.txt**

Report documenting dataset validation and quality checks.

**README.md**

Project documentation containing setup instructions, dataset information, and details of CSV generation.

---

## 4. Dataset Description

The dataset represents synthetic patient journeys through hospital departments.

Each row represents one recorded hospital activity.

### CSV Columns

| Column        | Description                             |
| ------------- | --------------------------------------- |
| Case_ID       | Unique identifier for a patient journey |
| Activity_Name | Name of the hospital activity           |
| Timestamp     | Date and time of the activity           |

### Example CSV Format

```csv
Case_ID,Activity_Name,Timestamp
P001,Registration,2026-10-01 10:00:00
P001,Vitals,2026-10-01 10:10:00
P001,Triage,2026-10-01 10:15:00
P001,Doctor,2026-10-01 10:25:00
P001,Pharmacy,2026-10-01 10:40:00
P001,Discharge,2026-10-01 10:50:00
```

The example above illustrates the CSV structure. The actual generated file contains additional activities and patient records.

---

## 5. Hospital Activities

The dataset contains the following activities:

1. Registration
2. Vitals
3. Triage
4. Doctor
5. Billing Counter
6. Pathology
7. X-Ray
8. X-Ray report
9. Pathology report
10. Pharmacy
11. Discharge

Different patients may follow different activity sequences.

---

## 6. Patient Journey Simulation

The generator uses six predefined hospital journey patterns.

### Example 1: Patient Journey with Pathology

Registration → Vitals → Triage → Doctor → Billing Counter → Pathology → Pathology report → Doctor → Pharmacy → Discharge

### Example 2: Patient Journey with X-Ray

Registration → Vitals → Triage → Doctor → Billing Counter → X-Ray → X-Ray report → Doctor → Pharmacy → Discharge

### Example 3: Patient Journey with Loop-Back

Registration → Vitals → Triage → Doctor → Billing Counter → Pathology → Pathology report → Triage → Doctor → Pharmacy → Discharge

### Loop-Back Explanation

A loop-back occurs when a patient returns to a previously visited stage.

For example, a patient may return to Triage after receiving a pathology report.

These repeated activities can be analyzed to understand hospital workflow variations.

---

## 7. Python Event-Log Generation

The project initially uses dictionaries and lists to represent individual patient journeys.

### Example

```python
patient_001 = {
    "patient_id": "P001",

    "activities": [
        "Registration",
        "Vitals",
        "Triage",
        "Doctor",
        "Pharmacy",
        "Discharge"
    ],

    "timestamps": [
        "10:00",
        "10:10",
        "10:15",
        "10:25",
        "10:40",
        "10:50"
    ]
}
```

Each patient record contains:

* A unique patient identifier.
* A list of hospital activities.
* A corresponding list of timestamps.

A Python function can process these records and display the event logs.

The full generator extends this approach by automatically creating patient journeys and exporting them into a CSV file.

---

## 8. Timestamp Generation

The generator uses Python's `datetime` and `timedelta` modules to create timestamps.

### Example

```python
from datetime import datetime, timedelta

start_time = datetime.strptime("10:00", "%H:%M")

next_time = start_time + timedelta(minutes=10)

print(next_time)
```

The `timedelta` function is used to add time intervals between consecutive hospital activities.

Random time intervals introduce variation into patient journeys.

Some Triage-to-next-event intervals are intentionally longer to simulate potential delays.

All dates in the generated dataset are synthetic.

---

## 9. CSV File Creation

The Python generator exports patient event logs into CSV format using the built-in `csv` module.

### CSV Generation Process

1. Define hospital journey patterns.
2. Generate unique patient IDs.
3. Assign a journey pattern to each patient.
4. Generate an initial timestamp.
5. Calculate timestamps for subsequent activities.
6. Store each activity as an event record.
7. Write the generated records into a CSV file.

### CSV Writing Example

```python
import csv

with open("careflow.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Case_ID",
        "Activity_Name",
        "Timestamp"
    ])

    writer.writerow([
        "P001",
        "Registration",
        "2026-10-01 10:00:00"
    ])
```

The actual generator automatically writes all patient event records into:

`careflow_generated_100_patients.csv`

The CSV file can be opened using Excel, Google Sheets, or Python.

---

## 10. How to Run the Project

### Step 1: Install Python

Ensure Python 3 is installed.

### Step 2: Open the Project Folder

Open the CareFlow project folder in VS Code.

### Step 3: Open the Terminal

Select:

Terminal → New Terminal

### Step 4: Execute the Script

```bash
python careflow_generator.py
```

### Step 5: Expected Output

```text
Saved 1134 events from 100 patients to careflow_generated_100_patients.csv
```

### Step 6: Verify the CSV

After execution, the CSV file will be created in the same directory as the Python script.

Open the file to inspect the generated patient records.

**Note:** Running the generator again overwrites the generated CSV with a reproducible dataset using the script's fixed random seed.

---

## 11. Dataset Statistics

| Parameter                       | Value               |
| ------------------------------- | ------------------- |
| Total patients                  | 100                 |
| Total event records             | 1,134               |
| Total columns                   | 3                   |
| Unique patient journey patterns | 6                   |
| Dataset type                    | Synthetic           |
| File format                     | CSV                 |
| Timestamp format                | YYYY-MM-DD HH:MM:SS |

Each patient journey begins with Registration and ends with Discharge.

The dataset includes multiple hospital pathways, repeated activities, and simulated delays.

---

## 12. Data Validation

The original cleaned dataset was checked for:

* Unique patient IDs.
* Missing values.
* Duplicate records.
* Chronological timestamp ordering.
* Valid activity names.
* Repeated activities and loop-backs.
* Correct starting and ending activities.

### Validation Results for the Cleaned Dataset

| Validation Check                | Result |
| ------------------------------- | ------ |
| Unique patients                 | 100    |
| Total events                    | 1,134  |
| Missing values                  | 0      |
| Exact duplicate rows            | 0      |
| Chronological violations        | 0      |
| Patients with Triage loop-backs | 16     |
| Distinct journey patterns       | 6      |

These results describe the cleaned original dataset. The separately generated CSV has the same number of patients, events, and journey patterns, but individual timestamps and patient assignments may differ.

---

## 13. Applications in Process Mining

### Process Discovery

Identify the sequence of activities followed by patients.

### Bottleneck Analysis

Analyze longer intervals between consecutive hospital activities.

### Loop-Back Analysis

Identify repeated activities within patient journeys.

### Performance Analysis

Calculate the duration of individual patient journeys and compare different pathways.

### Process Visualization

Visualize hospital workflows using process-mining tools and dashboards.

The dataset can support further analysis using Python, PM4Py, and Power BI.

---

## 14. Limitations

* The dataset contains synthetic patient records.
* No real patient information is included.
* Patient pathways are based on predefined patterns.
* Waiting times are simulated.
* The generator uses six journey patterns.
* Long event intervals do not necessarily represent confirmed waiting time.
* The dataset does not include medical diagnoses or treatment outcomes.

---

## 15. Future Improvements

* Generate larger datasets.
* Introduce additional hospital journey patterns.
* Add more detailed delay scenarios.
* Calculate average time intervals between activities.
* Analyze department-level bottlenecks.
* Perform process discovery using PM4Py.
* Build interactive dashboards using Power BI.
* Compare actual event sequences against expected hospital workflows.

---

## 16. Conclusion

CareFlow demonstrates how Python can be used to generate synthetic hospital event logs for healthcare process analysis.

The project includes a Python event-log generator and a CSV dataset containing 100 patient journeys and 1,134 event records.

The dataset includes different hospital pathways, simulated delays, and loop-backs.

These event logs provide a foundation for further process mining, bottleneck analysis, and hospital workflow visualization.


---

## 17. Dataset Version 2 – Enhanced Patient Event Logs

### Overview

The CareFlow dataset was enhanced to improve its suitability for
clinical pathway process mining and hospital workflow analysis.

The updated dataset contains 100 synthetic patient journeys with
additional loop-backs, simulated delays, and department information.

### Updated Dataset Statistics

| Parameter | Value |
|---|---|
| Total Patients | 100 |
| Total Event Records | 1,162 |
| Total Columns | 5 |
| Patients with Triage Loop-backs | 30 |
| Patients Affected by Additional Delays | 40 |
| Additional Delays Introduced | 91 |
| Missing Values | 0 |
| Chronological Errors | 0 |
| Dataset Type | Synthetic |

### Updated Dataset Columns

| Column | Description |
|---|---|
| Case_ID | Unique identifier for each patient journey |
| Activity_Name | Hospital activity performed |
| Date | Date of the recorded activity |
| Time | Time of the recorded activity |
| Department | Hospital department responsible for the activity |

### Example Dataset

| Case_ID | Activity_Name | Date | Time | Department |
|---|---|---|---|---|
| P001 | Registration | 2026-10-01 | 08:20 | Reception |
| P001 | Vitals | 2026-10-01 | 08:53 | Nursing |
| P001 | Triage | 2026-10-01 | 09:25 | Emergency |
| P001 | Doctor | 2026-10-01 | 09:49 | Consultation |
| P001 | Billing Counter | 2026-10-01 | 10:06 | Billing |

### Additional Loop-backs

The original dataset contained 16 patients with repeated Triage visits.

Version 2 introduces additional Triage and Doctor events for
14 patients.

This increases the total number of patients with Triage loop-backs
to 30.

These loop-backs simulate patients returning to an earlier
hospital stage for reassessment.

### Additional Delays

Additional waiting periods were introduced to simulate
potential hospital bottlenecks.

The simulation includes delays associated with:

- Triage to Doctor
- Pathology to Pathology Report
- X-Ray to X-Ray Report

A total of 91 additional delays were introduced,
affecting 40 patients.

### Data Validation

The updated dataset was validated using Python and Pandas.

Validation included:

- Checking missing values.
- Confirming 100 unique patient journeys.
- Checking chronological event ordering.
- Verifying the total number of event records.
- Identifying repeated Triage activities.

Final validation confirmed:

- 0 missing values.
- 0 chronological ordering errors.
- 100 unique patients.
- 1,162 event records.

### Python Script

File: `careflow_dataset_v2.py`

The script uses Python and Pandas to:

1. Load the original cleaned CSV dataset.
2. Separate Date and Time information.
3. Assign hospital departments.
4. Introduce additional loop-backs.
5. Simulate additional delays.
6. Validate patient event sequences.
7. Export the updated dataset.

### How to Run Version 2

Install Pandas:

```bash
python -m pip install pandas
```

Run the script:

```bash
python careflow_dataset_v2.py
```

The script generates:

`careflow_100_patients_final.csv`

### Final Output

The updated CSV contains five columns:

`Case_ID, Activity_Name, Date, Time, Department`

The dataset can be used for:

- Process discovery.
- Patient journey analysis.
- Loop-back identification.
- Hospital bottleneck analysis.
- Department-level performance analysis.
- Process visualization using PM4Py and Power BI.

For process-mining applications requiring a complete timestamp,
the Date and Time columns can be combined during preprocessing.

### Important Note

All patient records, timestamps, delays, and hospital pathways
are synthetic and intended for educational and analytical purposes.