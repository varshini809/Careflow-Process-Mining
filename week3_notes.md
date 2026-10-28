# CareFlow Week 3 — handoff notes

## Deliverables
- week3_careflow.sqlite: database loaded from careflow_100_patients_v3.csv, with raw and cleaned tables.
- week3_cleaning.sql: removes blank/null values and exact duplicate rows; combines Date and Time into Event_Timestamp.
- week3_analysis_queries.sql: patients per activity, average time until next event by activity, and top five longest waits.
- week3_patient_events_clean.csv: cleaned table exported in patient and timestamp order.
- week3_query_results.json: results from the three queries.

## Data summary
The supplied CSV contains 979 rows for 100 patients. It has no blank fields or exact duplicate rows, so all 979 rows are retained. Wait time is interpreted as the interval from an event to that patient’s next event; each patient’s final event is excluded because it has no subsequent event.

## Commit note
Week 3: load final patient events, clean and analyze activity waits, export cleaned CSV.

The files are prepared in the outputs folder. The current workspace is not a Git repository, so these files still need to be added and committed from your project branch.