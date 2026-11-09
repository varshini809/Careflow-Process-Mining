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

## Dashboard (Power BI)
- Cards: Total Patients, Total Events, Avg Events per Patient, Avg Wait (minutes), Loop-back Patients
- Visuals: Patients per Day, Events by Department, Avg Wait Time by Department, Events per Activity
- Features: Department filter, left navigation bar with bookmarks, green colour theme

## Key findings
- Doctor is the busiest step.
- Laboratory and Radiology have the longest average waits.
- 78 of 100 patients had a loop-back.

## Repository notes
- Each team member works and commits on their own branch. The team lead merges the branches into main.
- The docs folder has planning notes, the dataset review, dashboard notes, the project report draft and the demo script.

## How to open the dashboard
1. Install Power BI Desktop.
2. Open the .pbix file from this repository.
3. If asked, point the data source to careflow_100_patients_v3.csv.

## Team roles
- Mosharib: dataset (Python)
- Chandana: SQL database and cleaning
- Shubhangi: pandas analysis
- Varshini: team lead and Power BI dashboard
