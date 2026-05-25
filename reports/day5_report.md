# Week 1 Day 5 — Advanced Imbalance Handling for ICU Sepsis Prediction

## Overview

Day 5 focused on improving septic patient detection by addressing the severe class imbalance problem observed in previous modeling stages.

Previous models achieved relatively strong overall accuracy but failed to correctly identify septic patients, which is a critical issue in medical early warning systems. Therefore, this stage focused on:

- SMOTE oversampling
- Recall optimization
- Threshold tuning
- Improved minority-class learning
- Clinically meaningful evaluation

---

# Objectives

The main objectives of Day 5 were:

- Improve septic patient detection
- Reduce false negatives
- Handle severe class imbalance
- Apply advanced oversampling techniques
- Optimize classification thresholds
- Improve clinical relevance of predictions

---

# Dataset Used

The processed ICU patient-level dataset generated during Day 2 preprocessing was used.

### Main Physiological Features

- Heart Rate (HR)
- Oxygen Saturation (O2Sat)
- Temperature
- Systolic Blood Pressure (SBP)
- Mean Arterial Pressure (MAP)
- Respiratory Rate
- Age
- Gender
- ICU Length of Stay (ICULOS)

### Target Variable

- `SepsisLabel_max`

---

# Understanding Class Imbalance

The dataset contains significantly fewer septic patients compared to non-septic patients.

This situation is called **class imbalance**.

In healthcare datasets, class imbalance is very common because critical conditions such as sepsis occur less frequently than normal patient cases.

Machine learning models trained on highly imbalanced data often become biased toward the majority class, resulting in:

- high accuracy,
- but poor septic patient detection.

This issue was observed during Day 4 where the Random Forest model achieved strong accuracy but failed to correctly classify septic patients.

---

# What is Oversampling?

Oversampling is a technique used to increase the number of minority-class samples during training.

The objective is to help the model learn minority-class patterns more effectively.

Instead of training on extremely unbalanced data, oversampling creates a more balanced dataset for the learning process.

### Common Oversampling Techniques

- Random Oversampling
- SMOTE
- ADASYN

For this project, SMOTE was selected because it creates synthetic patient samples instead of simply duplicating existing ones.

---

# What is SMOTE?

SMOTE stands for:

## Synthetic Minority Oversampling Technique

SMOTE generates new synthetic minority-class samples by interpolating between existing septic patient samples.

Instead of copying data directly, SMOTE creates realistic artificial feature combinations based on neighboring septic cases.

### Advantages of SMOTE

- Reduces overfitting
- Improves minority-class learning
- Increases recall
- Better suited for medical prediction tasks

SMOTE was applied only to the training dataset to avoid data leakage.

---

# Methodology

## 1. Data Loading

The processed patient-level ICU dataset was loaded from the preprocessing pipeline.

## 2. Stratified Train-Test Split

A stratified train-test split was used to preserve the same sepsis distribution in both training and testing datasets.

## 3. SMOTE Oversampling

SMOTE was applied to the training dataset to generate synthetic septic patient samples.

## 4. Random Forest Training

A Random Forest classifier was trained using:

- SMOTE-balanced data
- Class weighting
- Tuned hyperparameters

## 5. Threshold Optimization

Multiple probability thresholds were evaluated to improve recall and reduce false negatives.

---

# Baseline Random Forest + SMOTE Results

| Metric    | Value |
| --------- | ----- |
| Accuracy  | 0.80  |
| Precision | 0.33  |
| Recall    | 0.33  |
| F1-score  | 0.33  |
| ROC-AUC   | 0.73  |

---

# Baseline Results Analysis

Compared with Day 4:

- ROC-AUC remained strong
- Septic patient detection improved
- Recall increased from 0.00 to 0.33

This demonstrates that SMOTE helped the model learn clinically meaningful septic patient patterns.

However, recall was still insufficient for a real ICU early warning system.

---

# Threshold Optimization

By default, classification models use a probability threshold of 0.50.

However, medical prediction systems often require lower thresholds to prioritize recall and reduce false negatives.

Different thresholds between:

- 0.10
- 0.85

were evaluated using:

- Recall
- Precision
- F1-score

---

# Best Threshold Selection

The best recall-focused threshold identified was:

## Threshold = 0.25

---

# Optimized Model Results

| Metric    | Value |
| --------- | ----- |
| Accuracy  | 0.50  |
| Precision | 0.23  |
| Recall    | 1.00  |
| F1-score  | 0.38  |
| ROC-AUC   | 0.73  |

---

# Interpretation of Optimized Results

After threshold optimization:

- Recall improved dramatically to 1.00
- All septic patients in the test set were detected
- False negatives were eliminated
- Precision decreased due to increased false positives

This tradeoff is common in healthcare AI systems.

In medical early warning systems, detecting all high-risk patients is often more important than maintaining high precision because missing a septic patient may have severe clinical consequences.

---

# Confusion Matrix Analysis

The optimized confusion matrix showed:

- 3 septic patients correctly detected
- 0 septic patients missed
- Increased false positives among non-septic patients

This demonstrates that the model became significantly more sensitive to septic cases after threshold tuning.

---

# ROC Curve Analysis

The ROC-AUC score remained:

## ROC-AUC = 0.73

This indicates that the model maintains acceptable discrimination ability between septic and non-septic patients.

The ROC curve confirmed that the model learned meaningful physiological relationships from ICU patient data.

---

# Feature Importance Analysis

The most influential physiological variables included:

- ICU Length of Stay
- Heart Rate
- Temperature
- Blood Pressure
- Oxygen Saturation
- Respiratory Rate

These findings are medically meaningful because sepsis strongly affects cardiovascular and respiratory stability.

---

# Key Improvements Achieved in Day 5

Day 5 introduced several major improvements:

- SMOTE oversampling
- Recall-focused learning
- Threshold optimization
- Improved septic patient detection
- Elimination of false negatives
- Stronger clinical relevance

The project now behaves more like a realistic ICU early warning system rather than a standard accuracy-focused classifier.

---

# Limitations

Despite improvements, several limitations remain:

- Small minority-class sample size
- Increased false positives
- Limited feature engineering
- No temporal sequence modeling yet
- No deep learning implementation

---

# Future Improvements

Potential future enhancements include:

- XGBoost or LightGBM
- Temporal ICU sequence modeling
- LSTM-based deep learning
- Advanced calibration techniques
- Larger ICU datasets
- Real-time ICU monitoring integration

---

# Conclusion

Day 5 focused on solving the class imbalance problem in ICU sepsis prediction.

SMOTE oversampling and threshold optimization significantly improved septic patient detection performance and eliminated false negatives during testing.

Although precision decreased, the model became much more clinically useful because it prioritized identifying high-risk septic patients.

This stage represents an important transition from general machine learning toward medically meaningful ICU early warning prediction systems.

---

# Project Status After Day 5

Completed components:

- ICU dataset exploration
- Missing value analysis
- ICU preprocessing pipeline
- Patient-level feature engineering
- Baseline Logistic Regression
- Random Forest modeling
- SMOTE oversampling
- Threshold optimization
- Recall-focused evaluation
- Feature importance analysis
- Clinical interpretation pipeline

The project is now progressing toward more advanced medical AI modeling and clinically meaningful ICU prediction systems.
