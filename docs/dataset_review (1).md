# CareFlow – Dataset Review (Week 2)

Reviewed by: Varshini (Team Lead)
File reviewed: `careflow_100_patients_final.csv` (latest version shared by Mosharib)

## Dataset summary
| Item | Result |
|---|---|
| Rows | 1,162 |
| Patients (Case_ID) | 100 |
| Columns | Case_ID, Activity_Name, Date, Time, Department |
| Date range | 2026-10-01 to 2026-10-30 (30 days) |
| Empty values | 0 |
| Duplicate rows | 0 |
| Time order per patient | Correct for all patients |
| Different patient paths | 9 |

## Version history
1. **Version 1:** Timestamp had time only (no date), 6 different paths.
2. **Version 2:** Date and Department columns added, but all rows had the same date (2026-10-01).
3. **Version 3:** Dates spread over 30 days, one date per patient.

## Problems found
1. Only 9 different patient paths. 42 of 100 patients follow the exact same path.
2. Data is too regular. Few long waits and few unusual cases.
3. Column names changed between versions (Case ID, Activity Name, Timestamp → Case_ID, Activity_Name, Date, Time).

## Changes requested from Mosharib
1. Make 15 to 20 different paths (some skip X-Ray or Pathology, some in different order).
2. Add more loop-backs (for example Doctor > Pathology > Doctor > X-Ray > Doctor).
3. Add some long waits (60 to 120 minutes), mostly before reports.
4. Add a few emergency patients who go straight to Doctor, and a few who leave early.
5. Make some days busy and some quiet.
6. Keep the same columns, with no empty values.

## Team decision
- Everyone uses the same column names: Case_ID, Activity_Name, Date, Time, Department.
- Chandana and Shubhangi continue with the current file. Switch to the new file when it arrives.
- Power BI dashboard is built on the current file and the data is swapped later.
