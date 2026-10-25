# CareFlow – Week 2 Dataset Validation Report

## 1. Project Overview

CareFlow is a clinical pathway process-mining project designed
to analyze simulated patient journeys, identify delays,
and study hospital workflow patterns.

## 2. Week 2 Objectives

- Add Date and Department columns.
- Distribute patient records across 30 days.
- Generate at least 15 unique patient pathways.
- Introduce loop-backs and realistic waiting times.
- Validate missing values, duplicates, and chronological order.
- Update project documentation.

## 3. Dataset Overview

Dataset: careflow_100_patients_v3.csv

- Total patients: 100
- Total events: 979
- Unique patient pathways: 18
- Days covered: 30
- Minimum patients per day: 1
- Maximum patients per day: 6

## 4. Dataset Columns

- Case_ID: Unique identifier for each patient.
- Activity_Name: Hospital activity performed.
- Date: Date of the activity.
- Time: Time of the activity.
- Department: Hospital department associated with the activity.

## 5. Data Validation

Validation script: validate_careflow_v3.py

Validation results:

- Duplicate records: 0
- Patients with incorrect time order: 0
- Total patients verified: 100
- Total events verified: 979

The validation script also checks for missing values.

## 6. Dataset Analysis

Analysis script: careflow_summary.py

The analysis covers:

- Total patients and events.
- Unique patient pathways.
- Department activity frequencies.
- Average patient journey duration.
- Repeated Doctor visits.
- Daily patient volumes.

## 7. Conclusion

The CareFlow V3 dataset meets the main Week 2 requirements
and provides a foundation for further process-mining analysis.

The dataset is synthetically generated for educational
and analytical purposes. It does not contain real patient records.