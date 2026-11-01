# CareFlow: Week 3 Final Validation Report

## 1. Objective

The objective of Week 3 was to finalize the synthetic hospital event-log dataset, ensure at least 15 unique patient pathways, include realistic loop-backs and long activity intervals, and verify data quality.

## 2. Dataset Overview

The final dataset contains:

* Total patients: 100
* Total events: 979
* Unique patient pathways: 18
* Date coverage: 30 days
* Dataset file: `careflow_100_patients_v3.csv`

The dataset contains the following columns:

* `Case_ID`
* `Activity_Name`
* `Date`
* `Time`
* `Department`

## 3. Patient Pathway Diversity

The dataset contains 18 distinct patient pathways, exceeding the minimum requirement of 15.

Patient journeys include routine consultations, diagnostic testing, emergency cases, early departures, and repeated department visits.

## 4. Loop-Back Analysis

Loop-backs represent repeated visits to an activity within the same patient journey.

The dataset includes repeated Doctor consultations and other department revisits.

The `careflow_summary.py` script identifies patients with repeated activities and summarizes loop-backs by activity.

## 5. Long Intervals and Bottleneck Analysis

The dataset includes extended intervals between consecutive patient activities, including intervals of 60 minutes or more.

The analysis script calculates:

* Average interval between activities
* Maximum interval between activities
* Number of patients experiencing extended intervals
* Activity transitions with the highest average elapsed times
* Department-level interval statistics
* Long intervals grouped by destination department

These results help identify potential hospital workflow bottlenecks.

**Note:** Elapsed time between activities is not necessarily equivalent to waiting time.

## 6. Data Quality Validation

The `validate_careflow_v3.py` script checks:

* Missing values
* Empty strings
* Duplicate records
* Chronological ordering
* Unique patient pathways
* Presence of loop-backs
* Presence of extended intervals
* Required columns
* Patient ID formatting
* Date consistency within patient journeys

### Validation Results

| Validation Check           | Result |
| -------------------------- | ------ |
| Minimum 15 unique pathways | PASS   |
| Loop-backs present         | PASS   |
| Long intervals present     | PASS   |
| Missing values             | 0      |
| Empty strings              | 0      |
| Duplicate records          | 0      |
| Chronological errors       | 0      |
| Required columns           | PASS   |
| Patient ID format          | PASS   |
| Patient date consistency   | PASS   |

## 7. Files Used

* `careflow_100_patients_v3.csv` — Final dataset
* `careflow_dataset_v3.py` — Dataset generation
* `validate_careflow_v3.py` — Data quality validation
* `careflow_summary.py` — Patient pathway and bottleneck analysis
* `README.md` — Project documentation

## 8. Week 3 Outcome

The final dataset satisfies the assigned Week 3 requirements for pathway diversity, loop-backs, extended activity intervals, and data quality.

The dataset and analysis scripts are ready for the next stage of process mining and visualization.
