-- SQLite cleaning script for careflow_100_patients_v3.csv.
DROP TABLE IF EXISTS patient_events_clean;
CREATE TABLE patient_events_clean AS
WITH normalized AS (
    SELECT TRIM(Case_ID) AS Case_ID,
           TRIM(Activity_Name) AS Activity_Name,
           TRIM(Date) AS Event_Date,
           TRIM(Time) AS Event_Time,
           TRIM(Department) AS Department,
           datetime(TRIM(Date) || ' ' || TRIM(Time)) AS Event_Timestamp
    FROM patient_events_raw
    WHERE NULLIF(TRIM(COALESCE(Case_ID, '')), '') IS NOT NULL
      AND NULLIF(TRIM(COALESCE(Activity_Name, '')), '') IS NOT NULL
      AND NULLIF(TRIM(COALESCE(Date, '')), '') IS NOT NULL
      AND NULLIF(TRIM(COALESCE(Time, '')), '') IS NOT NULL
      AND NULLIF(TRIM(COALESCE(Department, '')), '') IS NOT NULL
), deduplicated AS (
    SELECT DISTINCT Case_ID, Activity_Name, Event_Date, Event_Time,
                    Department, Event_Timestamp
    FROM normalized
    WHERE Event_Timestamp IS NOT NULL
)
SELECT Case_ID, Activity_Name, Event_Date, Event_Time, Department, Event_Timestamp
FROM deduplicated;
CREATE INDEX IF NOT EXISTS idx_patient_events_clean_case_time
    ON patient_events_clean (Case_ID, Event_Timestamp);
