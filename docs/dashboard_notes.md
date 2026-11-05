# CareFlow – Power BI Dashboard Notes

Team Lead: Varshini
Date: 5 Nov 2026
Data: careflow_100_patients_v3.csv (Case_ID, Activity_Name, Date, Time, Department)

## What the dashboard shows
- Cards: Total Patients (100), Total Events (979), Avg Events per Patient (9.79), Avg Wait in minutes (19.48), Loop-back Patients (78).
- Patients per Day: column chart by Date.
- Events by Department: donut chart and a table with events and patients per department.
- Avg Wait Time by Department: bar chart that shows where patients wait the longest.
- Events per Activity: bar chart that shows the busiest steps.

## Features used
- Department slicer (dropdown) that filters every visual.
- Left navigation bar with icons. Each icon is linked to a bookmark or page.
- Bookmarks to save different views of the report.
- DAX measures: Total Patients, Total Events, Avg Events per Patient, Avg Wait, Loop-back Patients.
- A Wait Minutes column calculated from the time gap between a patient's events.
- One green colour theme (#419869 and its shades) for a clean, consistent look.

## Key findings
- Doctor is the busiest step.
- Laboratory and Radiology have the longest average waits.
- 78 of 100 patients had a loop-back (a repeated step).

## Still to improve
- Rename the title to CareFlow – Clinical Pathway Dashboard.
- Clean the donut labels (percent only) and fix the table colours.
- Use real dates on the Patients per Day axis.
- Add a Key Findings text box.
