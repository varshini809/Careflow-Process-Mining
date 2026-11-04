# CareFlow — Final Data Summary

## Dataset Overview

The final CareFlow dataset (`careflow_100_patients_v3.csv`) contains synthetic hospital event logs generated using Python for clinical pathway process mining.

## Dataset Statistics

| Metric                               | Value |
| ------------------------------------ | ----- |
| Total rows (events)                  | 979   |
| Total patients                       | 100   |
| Total columns                        | 5     |
| Days covered                         | 30    |
| Unique patient pathways              | 18    |
| Emergency patients                   | 6     |
| Early departures                     | 3     |
| Patients with repeated Doctor visits | 78    |

## Dataset Columns

The dataset contains five columns: `Case_ID`, `Activity_Name`, `Date`, `Time`, and `Department`.

Each row represents one hospital activity performed during a patient's journey.

## Patient Pathways

The dataset includes 18 unique patient pathways, covering routine consultations, diagnostic testing, emergency cases, early departures, and repeated department visits.

Loop-backs and extended activity intervals were included to simulate variations in hospital workflows.

## Date Coverage

Patient journeys are distributed across 30 days, with between 1 and 6 patients per day.

## Data Quality

The final dataset passed the following validation checks:

* Missing values: 0
* Empty strings: 0
* Duplicate records: 0
* Chronological errors: 0
* Required columns: Present
* Patient pathway requirement (15+): Passed

## Conclusion

The final dataset contains 979 events from 100 patients across 30 days and 18 distinct patient pathways.

It is ready for process mining, patient journey analysis, and hospital workflow visualization.
