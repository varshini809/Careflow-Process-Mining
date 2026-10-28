# CareFlow Project Progress

This README summarizes the work completed so far in the CareFlow process-mining project.

## Week 1: Load and explore the patient activity CSV

- Loaded the CareFlow patient activity CSV into Python with pandas.
- Checked the data by displaying rows and column names.
- Worked on building each patient’s activity path in timestamp order.
- Added logic to count patients following each distinct full activity path.
- Added logic to count loop-backs, defined as an activity repeated later in the same patient’s path.

The Week 1 CSV used these fields: `Case ID`, `Activity Name`, and `Timestamp`.

## Dataset Columns

- Case_ID: Unique patient case identifier.
- Activity_Name: Patient activity performed.
- Date: Date of the patient activity.
- Time: Time when the activity occurred.
- Department: Hospital department handling the activity.
