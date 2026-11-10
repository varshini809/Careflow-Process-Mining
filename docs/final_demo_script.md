# CareFlow – Final Demo Script

Team Lead: Varshini
Format: live screen share of the Power BI dashboard (no PPT)
Time: about 5 minutes

## 1. Introduction (30 seconds)
- I am Varshini, team lead of CareFlow, a clinical pathway process mining project.
- Team: Mosharib (data), Chandana (SQL), Shubhangi (pandas analysis), Varshini (team lead and Power BI).

## 2. Problem and data (45 seconds)
- Goal: find the common patient paths, repeated steps (loop-backs) and long waits in a hospital.
- Dataset: 100 patients, 979 events, 30 days. Columns: Case_ID, Activity_Name, Date, Time, Department.
- Data checks: no empty values, no duplicates, time in order for each patient.

## 3. Dashboard walk-through (2 minutes)
1. Navigation bar on the left: each icon opens a bookmarked view.
2. Department filter at the top: it filters every visual.
3. Cards: Total Patients 100, Total Events 979, Avg Events per Patient 9.79, Avg Wait 19.48 minutes, Loop-back Patients 78.
4. Patients per Day: shows daily patient volume.
5. Events by Department: donut chart and table.
6. Avg Wait Time by Department: Laboratory and Radiology are the longest.
7. Events per Activity: Doctor is the busiest step.

## 4. Key findings (45 seconds)
- Doctor is the busiest step.
- Laboratory and Radiology have the longest waits.
- 78 of 100 patients had a loop-back.
- Recommendation: reduce waiting in Laboratory and Radiology, and check why patients return to the Doctor.

## 5. Team work and GitHub (30 seconds)
- Each member commits daily on their own branch. The team lead merges into main.
- Progress is tracked in the task sheet and the Work Distribution Document.

## 6. Closing (15 seconds)
- Future work: more data (patient type, priority, outcome), a patient path page, and wait-time prediction.
- Thank you. I am happy to answer questions.

## If I do not know an answer
- Say: "I am not sure. I will check and reply."
