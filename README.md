# CareFlow – Clinical Pathway Process Mining

Infotact Solutions internship project | Domain: Data Analytics
Team Lead: Varshini | Team: Mosharib, Chandana, Shubhangi

## About the project
CareFlow studies hospital patient journeys using event data. Each patient moves through steps like Registration, Triage, Doctor, Pathology, X-Ray, Pharmacy, Billing and Discharge. We find the common paths, repeated steps (loop-backs) and long waiting times, and show them in a Power BI dashboard.

## Dataset
- File: careflow_100_patients_v3.csv (synthetic data, no real patient information)
- Columns: Case_ID, Activity_Name, Date, Time, Department
- Size: 100 patients, 979 events, 30 days
- Checks: no empty values, no duplicate rows, time in order for each patient

## Tools
Python (pandas), SQL, Power BI, Excel, GitHub

# CareFlow — Week 2 Analysis

This week’s work loads the patient activity dataset, checks its structure, calculates wait times between consecutive activities, and identifies loop-backs and activities with longer waits.

## Dataset

The analysis uses `careflow_100_patients_v3.csv`, which contains 979 event records across 100 patient cases.

Columns:

- `Case_ID` — patient case identifier
- `Activity_Name` — recorded activity
- `Date` and `Time` — when the activity occurred
- `Department` — department associated with the activity

## Analysis

The script `week 2.py`:

- Loads the CSV with pandas and checks its rows, columns, and data types.
- Combines `Date` and `Time` into a timestamp.
- Orders activities by case and timestamp.
- Calculates the wait in minutes between consecutive activities for each case.
- Identifies loop-backs when a case repeats an activity later in its path.
- Summarizes average wait time by activity.

The first activity in each case has no preceding activity, so it is excluded from wait-time calculations.

## Charts

The charts are saved in `docs/charts/`:

- **Activity event counts:** `activity_frequency.svg`
- **Average wait by activity:** `average_wait_by_activity.svg`
- **Loop-back events by activity:** `loopbacks_by_activity.svg`

![Activity event count by activity](docs/charts/activity_frequency.svg)

![Average wait in minutes by activity](docs/charts/average_wait_by_activity.svg)

![Loop-back event count by activity](docs/charts/loopbacks_by_activity.svg)

## Findings

1. The dataset contains **979 event records** across **100 patients**, with **12 activity types** and **10 departments**.
2. There are **879 wait intervals**; the average wait is **19.5 minutes** and the median is **14 minutes**.
3. **Doctor** is the most frequently recorded activity, with **191 events**.
4. **Pathology report** has the longest average preceding wait at **59.7 minutes**, followed by **X-Ray report** at **56.5 minutes**.
5. There are **111 loop-back events** across **78 patients**; **Doctor** accounts for **93** of them.

## week 3:

## Objective
Visualize patient journey patterns, waiting times, and repeated activities in the CareFlow dataset.
Work Completed
- Created a bar chart of the five most common patient activity paths.
- Created a chart comparing average wait times between consecutive activities.
- Created a histogram of loop-backs per patient.
- Reviewed the charts and summarized the main findings below.
