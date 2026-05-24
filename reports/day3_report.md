# Week 1 — Day 3 Report

## Project

ICU Early Warning Prediction System

## Day 3 Objective

The objective of Day 3 was to train the first baseline machine learning model using the processed patient-level dataset created on Day 2.

## Dataset Used

`data/processed/day2_patient_level_features.csv`

## Model Used

Logistic Regression was selected as the first baseline model because it is simple, interpretable, and suitable for binary classification.

## Work Completed

- Loaded the processed patient-level dataset
- Separated features and target variable
- Applied train-test split
- Applied feature scaling
- Trained a Logistic Regression model
- Evaluated the model using accuracy, precision, recall, F1-score, and ROC-AUC
- Generated a confusion matrix
- Generated a ROC curve
- Analyzed feature importance using model coefficients
- Saved model metrics and feature importance results

## Medical Understanding

In early warning systems, recall is especially important because the model should avoid missing patients at risk of sepsis.

False negatives are dangerous because they represent septic patients that the model failed to detect.

False positives are also important because too many false alarms may contribute to alarm fatigue.

## Results

Add your results here after running the notebook:

- Accuracy:
- Precision:
- Recall:
- F1-score:
- ROC-AUC:

## Interpretation

The baseline model provides an initial benchmark. Its performance is not expected to be perfect, but it confirms that the preprocessing and machine learning pipeline works.

## Limitations

- Only patient-level aggregated features were used
- Time-series patterns were simplified
- Only one baseline model was trained
- Clinical validation was not performed
- Dataset imbalance remains a challenge

## Conclusion

Day 3 successfully created the first machine learning baseline for ICU sepsis prediction.

## Next Step

Day 4 will focus on improving the model using more advanced algorithms such as Random Forest and better evaluation strategies.
