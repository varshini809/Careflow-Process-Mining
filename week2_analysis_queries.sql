-- SQLite analysis queries. Run after week2_cleaning.sql.

-- 1. Distinct patients per activity.
SELECT Activity_Name, COUNT(DISTINCT Case_ID) AS Patients
FROM patient_events_clean
GROUP BY Activity_Name
ORDER BY Patients DESC, Activity_Name;

-- 2. Average wait after each activity until that patient's next event.
WITH sequenced AS (
    SELECT Case_ID, Activity_Name, Event_Timestamp,
           LEAD(Event_Timestamp) OVER (
               PARTITION BY Case_ID
               ORDER BY Event_Timestamp, Activity_Name, Department
           ) AS Next_Timestamp
    FROM patient_events_clean
), waits AS (
    SELECT Activity_Name,
           (julianday(Next_Timestamp) - julianday(Event_Timestamp)) * 1440.0 AS Wait_Minutes
    FROM sequenced
    WHERE Next_Timestamp IS NOT NULL
)
SELECT Activity_Name, ROUND(AVG(Wait_Minutes), 2) AS Average_Wait_Minutes
FROM waits
WHERE Wait_Minutes >= 0
GROUP BY Activity_Name
ORDER BY Average_Wait_Minutes DESC, Activity_Name;

-- 3. Five longest waits between consecutive events for the same patient.
WITH sequenced AS (
    SELECT Case_ID, Activity_Name AS From_Activity, Event_Timestamp AS From_Timestamp,
           LEAD(Activity_Name) OVER (
               PARTITION BY Case_ID
               ORDER BY Event_Timestamp, Activity_Name, Department
           ) AS To_Activity,
           LEAD(Event_Timestamp) OVER (
               PARTITION BY Case_ID
               ORDER BY Event_Timestamp, Activity_Name, Department
           ) AS To_Timestamp
    FROM patient_events_clean
), waits AS (
    SELECT Case_ID, From_Activity, From_Timestamp, To_Activity, To_Timestamp,
           (julianday(To_Timestamp) - julianday(From_Timestamp)) * 1440.0 AS Wait_Minutes
    FROM sequenced
    WHERE To_Timestamp IS NOT NULL
)
SELECT Case_ID, From_Activity, From_Timestamp, To_Activity, To_Timestamp,
       ROUND(Wait_Minutes, 2) AS Wait_Minutes
FROM waits
WHERE Wait_Minutes >= 0
ORDER BY Wait_Minutes DESC, Case_ID
LIMIT 5;
