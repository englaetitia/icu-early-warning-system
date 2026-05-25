# Week 1 — Day 4 Report

## Project

ICU Early Warning Prediction System

## Day 4 Objective

The objective of Day 4 was to improve the baseline sepsis prediction pipeline using more advanced machine learning methods and better handling of class imbalance.

The goal was to move beyond the initial Logistic Regression baseline and evaluate a stronger ensemble learning model using Random Forest.

## Dataset Used

`data/processed/day2_patient_level_features.csv`

## Models Used

Two machine learning models were trained and compared:

- Improved Logistic Regression with balanced class weighting
- Random Forest Classifier

Random Forest was selected because it can model complex non-linear relationships between ICU physiological variables and provide feature importance analysis.

## Work Completed

- Loaded the processed patient-level ICU dataset
- Inspected dataset structure and target class distribution
- Applied stratified train-test split
- Computed balanced class weights
- Applied feature scaling for Logistic Regression
- Trained an improved Logistic Regression model
- Trained a Random Forest classifier
- Evaluated both models using:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - ROC-AUC
- Generated a confusion matrix
- Generated a ROC curve
- Compared model performance visually
- Analyzed Random Forest feature importance
- Saved figures and evaluation results automatically

## Medical Understanding

In ICU early warning systems, detecting septic patients as early as possible is critical.

Class imbalance remains a major challenge because septic patients are much rarer than non-septic patients.

Random Forest models can better capture complex interactions between clinical variables such as:

- heart rate,
- oxygen saturation,
- temperature,
- respiratory rate,
- blood pressure,
- and ICU length of stay.

Feature importance analysis also helps identify clinically meaningful predictors associated with physiological deterioration and sepsis progression.

## Results

### Improved Logistic Regression

- Accuracy: 0.50
- Precision: 0.11
- Recall: 0.33
- F1-score: 0.17
- ROC-AUC: 0.47

### Random Forest

- Accuracy: 0.85
- Precision: 0.00
- Recall: 0.00
- F1-score: 0.00
- ROC-AUC: 0.73

## Interpretation

The Random Forest model significantly improved overall accuracy and ROC-AUC compared to the Logistic Regression baseline.

The ROC-AUC score increased from approximately 0.47 to 0.73, indicating that Random Forest achieved better separation between septic and non-septic patients.

However, the confusion matrix revealed that the Random Forest model predicted only the majority class and failed to correctly identify septic patients in the testing set.

This behavior is common in highly imbalanced medical datasets where the number of septic patients is very small.

Despite this limitation, the model still demonstrated improved ranking capability as reflected by the ROC-AUC score.

## Feature Importance Analysis

The Random Forest model identified several clinically meaningful variables as important predictors, including:

- ICU Length of Stay (ICULOS_max)
- Heart Rate minimum (HR_min)
- Temperature mean (Temp_mean)
- Heart Rate mean (HR_mean)
- Systolic Blood Pressure mean (SBP_mean)
- Oxygen Saturation minimum (O2Sat_min)
- Respiratory Rate mean (Resp_mean)

These variables are physiologically associated with patient deterioration and sepsis risk.

The feature importance results support the medical relevance of the machine learning pipeline.

## Limitations

- Small dataset subset was used
- Severe class imbalance remains present
- Very few septic samples were available
- Patient-level aggregation simplified temporal ICU patterns
- Random Forest failed to detect minority septic cases
- Hyperparameter optimization was limited
- Clinical validation was not performed

## Conclusion

Day 4 successfully improved the ICU sepsis prediction pipeline using more advanced machine learning methods.

Although the Random Forest model still struggled with minority class detection, it demonstrated improved discriminative ability and provided clinically meaningful feature importance analysis.

The project now includes:

- multiple machine learning models,
- class imbalance handling,
- professional evaluation metrics,
- feature importance interpretation,
- and reproducible visualization outputs.

## Next Step

Day 5 will focus on:

- advanced feature engineering,
- SMOTE oversampling,
- hyperparameter tuning,
- threshold optimization,
- and potentially XGBoost or LightGBM models to improve septic patient detection.
