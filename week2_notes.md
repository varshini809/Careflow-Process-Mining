# CareFlow Week 2 — handoff notes

## What is included
- week2_careflow.sqlite: SQLite database with patient_events_raw and patient_events_clean.
- week2_cleaning.sql: removes null/blank fields and exact duplicate event rows; combines Date + Time into Event_Timestamp.
- week2_analysis_queries.sql: patient counts per activity, average wait after activity, and five longest consecutive-event waits.
- patient_events_clean.csv: cleaned export, sorted by patient and timestamp.
- week2_query_results.json: saved query output.

## Run / export
The database is already loaded with the supplied CSV. Run the cleaning script before the analysis queries if rebuilding. In SQLite CLI, export the cleaned table with:

    .headers on
    .mode csv
    .once patient_events_clean.csv
    SELECT Case_ID, Activity_Name, Event_Date AS Date, Event_Time AS Time, Department, Event_Timestamp
    FROM patient_events_clean
    ORDER BY Case_ID, Event_Timestamp, Activity_Name, Department;

## Data check and interpretation
Input: 979 rows, 100 patients. The supplied file has 0 rows with blank fields and 0 exact duplicate rows; the cleaned table contains 979 rows. Wait means elapsed minutes from an event to that patient’s next recorded event. Final events per patient have no next-event wait and are excluded; negative waits are excluded. Same-timestamp ties are ordered by activity name and department.

## Short commit note
Week 2: load and clean patient events, add activity and wait-time queries, and export cleaned CSV.