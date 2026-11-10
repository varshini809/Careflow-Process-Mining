# CareFlow – Week 3 Plan

Team Lead: Varshini
Due date: 1 Nov 2026

## Tasks by member

### Mosharib (data)
- Final dataset with 15+ patient paths, more loop-backs and long waits
- No empty values, no duplicates, same column names
- Update README with column meanings and commit

### Chandana (SQL)
- Load the final CSV into the database
- Cleaning SQL: no duplicates, no nulls, time in order
- 3 queries: patients per activity, average time per activity, top 5 longest waits
- Export the cleaned table as CSV and commit the SQL files

### Shubhangi (pandas)
- Count unique paths and list the top 5
- Calculate wait time between activities
- Find loop-backs and the slowest activity
- Make 3 charts and write 5 lines of findings

### Varshini (lead + Power BI)
- Dashboard page 1: card, activity bar chart, line chart by Date, Department filter
- Add wait-time and loop-back visuals when the cleaned data is ready
- Update the task sheet, send daily progress reports, check commits every night

## Team rules
- One real commit every day on your own branch (.md, .sql or .py file)
- Update your status in the task sheet
- Send a short update in the group every night
- Common columns: Case_ID, Activity_Name, Date, Time, Department
