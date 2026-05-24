# Week 1 — Day 2 Report

## Project

ICU Early Warning Prediction System

## Day 2 Objective

The objective of Day 2 was to preprocess the ICU dataset and create the first machine-learning-ready patient-level feature table.

## Work Completed

- Reviewed medical meaning of ICU variables
- Grouped features into vital signs, laboratory values, demographics, and target label
- Analyzed missing values
- Combined multiple patient files into one dataframe
- Applied forward fill per patient
- Applied median imputation for remaining missing values
- Created patient-level aggregated features
- Exported processed dataset to `data/processed/day2_patient_level_features.csv`

## Medical Understanding

Vital signs such as heart rate, oxygen saturation, temperature, blood pressure, MAP, and respiratory rate are important indicators of patient deterioration.

Laboratory values provide additional information about infection, inflammation, organ dysfunction, metabolism, coagulation, and respiratory status.

Missing values are expected in ICU data because measurements are taken at different frequencies depending on clinical need.

## Preprocessing Method

A baseline preprocessing strategy was used:

1. Sort records by patient and ICU length of stay
2. Forward fill missing values within each patient
3. Fill remaining missing values using the median
4. Aggregate hourly records into patient-level features

## Output File

`data/processed/day2_patient_level_features.csv`

## Challenges

- ICU data contains many missing values
- Sepsis labels are highly imbalanced
- Lab values are not recorded as frequently as vital signs
- Time-series data must be handled carefully to avoid data leakage

## Conclusion

Day 2 successfully transformed raw ICU data into a structured patient-level dataset suitable for initial machine learning experiments.

## Next Step

Week 1 Day 3 will focus on building a baseline machine learning model for sepsis or early warning prediction.
