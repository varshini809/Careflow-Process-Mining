# CareFlow – Final Review Questions and Answers (Preparation)

Team Lead: Varshini

## Project
- What is the project about? CareFlow analyses hospital patient journeys (Registration, Doctor, Lab, Pharmacy and more) to find where patients wait and where they repeat steps.
- What is process mining? It means using event data (patient ID, activity, time) to see how a process really runs.
- What is my role? Team lead: I plan tasks, check commits, hold meetings and build the Power BI dashboard.

## Data
- What does the dataset have? Case_ID, Activity_Name, Date, Time and Department. There are 100 patients and 979 events over 30 days.
- How was data quality checked? Empty values, duplicates and time order for each patient. There were none.
- What problems were found earlier? No date, the same date for all rows and too few paths. They were fixed in the later versions.
- What is a loop-back? A patient goes back to a step they already did, like seeing the Doctor again after Pathology.

## Power BI
- What is DAX? The formula language in Power BI for measures and columns.
- Measure vs column? A column is calculated for each row and stored. A measure is calculated when the report is used and changes with filters.
- How was Avg Wait calculated? A column stores the time gap between a patient's event and the previous event. The measure takes the average.
- How was Loop-back Patients calculated? A patient counts if they have more events than different activities.
- What is a slicer? A filter on the page. The Department slicer filters all visuals.
- What are bookmarks and navigation? Bookmarks save a view of the report. Each sidebar icon is linked to a bookmark or page.

## Findings
- Doctor is the busiest step.
- Laboratory and Radiology have the longest average waits.
- 78 of 100 patients had a loop-back.
- Recommendation: reduce waiting in Laboratory and Radiology and check why patients return to the Doctor.

## Team and GitHub
- How is the team managed? A task sheet, the Work Distribution Document, team meetings and nightly commit checks.
- How are commits handled? Each member commits daily to their own branch. The team lead merges the branches into main.
- What challenges were faced? Early dataset problems, and one team member was delayed, so the mentor was informed and a smaller task with a deadline was given.

## Future work
- Add patient type, priority and outcome.
- Add a page for individual patient paths.
- Predict waiting times by department.

## If I do not know an answer
- Say: "I am not sure. I will check and reply."
