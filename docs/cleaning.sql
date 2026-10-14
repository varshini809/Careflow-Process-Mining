
DROP TABLE IF EXISTS patient_events_clean;

CREATE TABLE patient_events_clean AS
SELECT DISTINCT
    TRIM("Case ID") AS Case_ID,
    TRIM("Activity Name") AS Activity,
    TRIM("Timestamp") AS Timestamp
FROM patients_events
WHERE TRIM(COALESCE("Case ID", '')) <> ''
  AND TRIM(COALESCE("Activity Name", '')) <> ''
  AND TRIM(COALESCE("Timestamp", '')) <> '';
