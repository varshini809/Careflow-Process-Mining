# CareFlow – Clinical Pathway Process Mining (Project Report Draft)

Team Lead: Varshini
Company: Infotact Solutions | Domain: Data Analytics
Team: Varshini, Mosharib, Chandana, Shubhangi
Duration: 5 Oct 2026 – 5 Nov 2026

## 1. Introduction
CareFlow is a process mining project on hospital patient journeys. Each patient moves through steps such as Registration, Triage, Doctor, Pathology, X-Ray, Pharmacy, Billing and Discharge. We study this event data to find the common patient paths, repeated steps (loop-backs) and long waiting times.

## 2. Objectives
- Understand the paths that patients follow in a hospital.
- Find where patients wait the longest.
- Find how many patients repeat a step.
- Show the results in a clear Power BI dashboard.

## 3. Tools used
Python (pandas), SQL, Power BI, Excel, GitHub.

## 4. Dataset
- File: careflow_100_patients_v3.csv (synthetic data, no real patient information).
- Columns: Case_ID, Activity_Name, Date, Time, Department.
- Size: 100 patients, 979 events, 30 days (October 2026).
- Data checks: no empty values, no duplicate rows, time in order for each patient.
- The dataset went through three versions: the first had time only with no date, the second had the same date for all rows, and the final version has dates spread over 30 days, a Department column and more path variety.

## 5. Method
1. Created the dataset and checked its quality.
2. Cleaned the data and wrote SQL queries (patients per activity, average time per activity, longest waits).
3. Analysed paths, wait times and loop-backs in pandas.
4. Built the Power BI dashboard with DAX measures, a Department slicer, bookmarks and navigation.

## 6. Dashboard
- Cards: Total Patients, Total Events, Avg Events per Patient, Avg Wait (minutes), Loop-back Patients.
- Charts: Patients per Day, Events by Department (donut and table), Avg Wait Time by Department, Events per Activity.
- Features: Department filter, left navigation bar with bookmarks, one green colour theme.

## 7. Key findings
- Doctor is the busiest step.
- Laboratory and Radiology have the longest average waits.
- 78 of 100 patients had a loop-back (a repeated step).
- SQL results: to be added by the SQL team member.
- Pandas analysis results (top paths, slowest activity): to be added by the analysis team member.

## 8. Team work and GitHub
- Work was divided by role: data (Mosharib), SQL (Chandana), pandas analysis (Shubhangi), team lead and Power BI (Varshini).
- Each member works on their own branch and commits daily. The team lead merges the branches into main.
- Progress was tracked in a task sheet and the Work Distribution Document.

## 9. Challenges
- The first dataset had no date and few patient paths, so it was improved in later versions.
- One team member was delayed, so the mentor was informed and a smaller task with a deadline was given.

## 10. Conclusion
The project shows how event data can reveal bottlenecks and repeated steps in a patient journey. The dashboard helps a reader see the busiest steps and the longest waits at a glance.

## 11. Future work
- Add more data such as patient type, priority and outcome.
- Add a page for individual patient paths.
- Predict waiting times by department.
