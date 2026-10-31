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


## 18. Dataset Version 3 – Realistic Patient Pathways

### Overview

CareFlow Dataset V3 is an improved synthetic hospital patient event log designed for clinical pathway process mining.

This version introduces greater variation in patient journeys, additional loop-backs, realistic waiting times, emergency cases, and early departures.

The objective is to create a more diverse dataset for identifying hospital bottlenecks, analyzing patient flow, and discovering clinical pathways.

### Files

* `careflow_dataset_v3.py` – Python script used to generate the dataset.
* `careflow_100_patients_v3.csv` – Generated dataset containing 100 patient journeys.

### Dataset Structure

The dataset contains five columns:

| Column        | Description                                      |
| ------------- | ------------------------------------------------ |
| Case_ID       | Unique patient identifier                        |
| Activity_Name | Hospital activity performed                      |
| Date          | Date of the activity                             |
| Time          | Time of the activity                             |
| Department    | Hospital department associated with the activity |

### Dataset Statistics

| Metric                                   | Result |
| ---------------------------------------- | ------ |
| Total patients                           | 100    |
| Total event records                      | 979    |
| Unique patient pathways                  | 18     |
| Patients in the most common pathway      | 10     |
| Emergency patients                       | 6      |
| Early departures                         | 3      |
| Patients with repeat Doctor visits       | 78     |
| Patients with Triage loop-backs          | 18     |
| Patients with 60–120-minute report waits | 35     |
| Days covered                             | 30     |
| Minimum patients per day                 | 1      |
| Maximum patients per day                 | 6      |

### Improvements Introduced in V3

**1. Increased pathway diversity**

The dataset contains 18 different patient pathways, compared with 9 in the previous version.

Patients may follow different sequences depending on their simulated treatment requirements.

**2. Optional diagnostic procedures**

Some patients undergo Pathology tests without X-Ray examinations, while others undergo X-Ray examinations without Pathology tests.

Other patients undergo both procedures in different orders.

**3. Additional Doctor loop-backs**

Patients may return to the Doctor multiple times during their hospital visit.

Example:

Registration → Vitals → Triage → Doctor → Pathology → Pathology report → Doctor → X-Ray → X-Ray report → Doctor → Pharmacy → Discharge

**4. Realistic waiting times**

Additional waiting periods of 60–120 minutes have been introduced, particularly before diagnostic reports become available.

These delays help simulate hospital waiting times and potential bottlenecks.

**5. Emergency patient journeys**

Six simulated emergency patients follow pathways that prioritize access to the Doctor.

**6. Early departures**

Three patients leave the hospital before completing their planned treatment pathways.

**7. Variable daily patient volumes**

Patient arrivals are distributed across 30 days, with daily volumes ranging from 1 to 6 patients.

This introduces variation between relatively busy and quiet days.

### Data Validation

The Python script performs validation checks to ensure:

* Every patient has a unique Case_ID.
* Patient activities follow chronological order.
* All activities for a patient occur on the same date.
* Diagnostic reports occur after their corresponding tests.
* The dataset contains 100 patient journeys.

All reported validation checks passed.

### Running the Script

Open the project folder in VS Code and execute:

```bash
python careflow_dataset_v3.py
```

The script generates:

`careflow_100_patients_v3.csv`

### Applications

The improved dataset can be used for:

* Process discovery using PM4Py.
* Patient pathway analysis.
* Identifying repeated hospital activities.
* Detecting waiting-time bottlenecks.
* Comparing emergency and routine patient journeys.
* Analyzing daily patient volumes.
* Creating interactive dashboards using Power BI.

### Important Note

This dataset is synthetically generated for educational and analytical purposes. It does not contain actual patient records.

**Dataset V3 is the recommended version for further CareFlow analysis and process mining.**

## Week 3: Final Dataset Validation and Process Analysis

### Dataset Overview

The CareFlow project uses a synthetic hospital event log to simulate patient journeys across different hospital departments.

The dataset includes:

* **Total patients:** 100
* **Total events:** 979
* **Unique patient pathways:** 18
* **Date coverage:** 30 days
* **Dataset file:** `careflow_100_patients_v3.csv`

### Patient Pathway Variations

The dataset includes 18 distinct patient pathways representing different hospital scenarios.

These include:

* Routine patient consultations
* Patients requiring pathology tests
* Patients requiring X-ray examinations
* Patients requiring multiple diagnostic tests
* Emergency patient pathways
* Patients leaving before completing all activities
* Patients returning to previously visited departments

### Loop-Back Analysis

Loop-backs represent patients returning to an activity or department they have already visited.

The dataset includes repeated Doctor consultations and other activity revisits.

The analysis is implemented in `careflow_summary.py`.

### Long Intervals and Bottleneck Analysis

The dataset contains extended intervals between hospital activities, including intervals of 60 minutes or more.

The analysis covers:

* Average interval between consecutive activities
* Longest interval between activities
* Patients experiencing extended intervals
* Activity transitions with the highest average elapsed times
* Department-level interval analysis
* Long intervals grouped by destination department

These measurements help identify potential hospital process bottlenecks. Elapsed time between events does not necessarily represent waiting time alone.

### Data Quality Validation

The dataset is validated using `validate_careflow_v3.py`.

Validation checks include:

* Missing values
* Empty strings
* Duplicate records
* Chronological ordering of patient activities
* Minimum of 15 unique patient pathways
* Presence of loop-backs
* Presence of long intervals
* Required dataset columns
* Patient ID formatting
* Date consistency within patient journeys

The dataset passed the Week 3 validation and structure consistency checks.

### Running the Project

Generate the dataset:

`python careflow_dataset_v3.py`

Validate the dataset:

`python validate_careflow_v3.py`

Run the process analysis:

`python careflow_summary.py`

### Week 3 Outcome

The final dataset meets the Week 3 requirements for pathway diversity, loop-backs, extended activity intervals, and data quality.

Additional analysis helps identify potential delays and bottlenecks in simulated hospital workflows.
