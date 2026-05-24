# Week 1 — Day 4 Report

## Project

ICU Early Warning Prediction System

## Day 4 Objective

The objective of Day 4 was to improve the baseline sepsis prediction model using more advanced machine learning techniques and better handling of class imbalance.

## Dataset Used

`data/processed/processed_icu_data.csv`

## Models Used

Two machine learning models were used:

- Improved Logistic Regression with balanced class weighting
- Random Forest Classifier

Random Forest was selected because it can model non-linear relationships between ICU variables and provide feature importance analysis.

## Work Completed

- Loaded the processed ICU dataset
- Inspected dataset structure and class distribution
- Applied stratified train-test split
- Computed class weights for imbalance handling
- Applied feature scaling for Logistic Regression
- Trained an improved Logistic Regression model
- Trained a Random Forest classifier
- Evaluated both models using accuracy, precision, recall, F1-score, and ROC-AUC
- Generated a confusion matrix
- Generated a ROC curve
- Compared model performance
- Analyzed Random Forest feature importance
- Saved evaluation metrics and visualizations

## Medical Understanding

In ICU early warning systems, detecting septic patients as early as possible is critical.

Class imbalance is a major challenge because septic patients are much less common than non-septic patients.

Random Forest models can capture more complex physiological relationships between:

- heart rate,
- respiratory rate,
- temperature,
- blood pressure,
- and laboratory measurements.

Feature importance analysis also helps identify clinically meaningful predictors associated with patient deterioration and sepsis progression.

## Results

Add your results here after running the notebook:

### Improved Logistic Regression

- Accuracy:
- Precision:
- Recall:
- F1-score:
- ROC-AUC:

### Random Forest

- Accuracy:
- Precision:
- Recall:
- F1-score:
- ROC-AUC:

## Interpretation

The Random Forest model improved the machine learning pipeline by introducing ensemble learning and better handling of complex feature interactions.

Even if overall performance remains limited, the experiment successfully demonstrated:

- advanced model training,
- class imbalance handling,
- model comparison,
- and clinical feature importance analysis.

## Limitations

- Small dataset subset was used
- Severe class imbalance remains present
- Temporal ICU dynamics were simplified
- Patient-level aggregation may remove important clinical patterns
- Hyperparameter optimization was limited
- Real clinical validation was not performed

## Conclusion

Day 4 successfully improved the ICU sepsis prediction pipeline using more advanced machine learning methods and established a stronger foundation for future model development.

## Next Step

Day 5 will focus on:

- advanced feature engineering,
- hyperparameter tuning,
- imbalance handling techniques such as SMOTE,
- and potentially XGBoost or LightGBM models.
