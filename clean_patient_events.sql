CREATE OR REPLACE TABLE
  `careflow-process-mining-511713.careflow_data.patient_events_clean` AS
SELECT DISTINCT *
FROM
  `careflow-process-mining-511713.careflow_data.patient_events`
ORDER BY
  SAFE.PARSE_TIME('%H:%M', string_field_2);
