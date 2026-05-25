# Week 1 Day 6 — Advanced Ensemble Learning for ICU Early Warning Prediction

## Project Overview

Day 6 focused on improving the ICU early warning prediction system using advanced ensemble learning techniques and clinically meaningful evaluation strategies.

Previous project stages demonstrated that class imbalance significantly affected septic patient detection. While Day 5 improved recall using SMOTE and threshold optimization, the objective of Day 6 was to build a more intelligent predictive system capable of learning complex nonlinear physiological deterioration patterns.

This notebook introduced Gradient Boosting ensemble learning combined with advanced clinical evaluation techniques including:

- SMOTE-enhanced training
- ROC curve analysis
- threshold optimization
- physiological feature importance analysis
- probability calibration
- clinically interpretable evaluation

---

# Objectives

The primary goals of Day 6 were:

- improve septic patient detection
- learn nonlinear ICU physiological relationships
- reduce false negatives
- improve clinical interpretability
- generate more reliable sepsis risk probabilities
- simulate realistic ICU early warning system behavior

---

# Dataset Information

The project used the processed ICU patient-level dataset generated during previous preprocessing stages.

## Dataset Characteristics

The dataset included aggregated physiological features such as:

- heart rate
- oxygen saturation
- temperature
- blood pressure
- respiratory rate
- ICU length of stay
- demographic information

### Final Dataset Shape

| Metric              | Value |
| ------------------- | ----- |
| Total Patients      | 100   |
| Feature Count       | 16    |
| Septic Patients     | 14    |
| Non-Septic Patients | 86    |

---

# Class Imbalance Analysis

The dataset remained moderately imbalanced:

- 86% non-septic patients
- 14% septic patients

Although less extreme than many real-world ICU datasets, imbalance still affected septic patient sensitivity and required balancing techniques during training.

---

# Advanced Ensemble Learning

## Gradient Boosting

Day 6 introduced Gradient Boosting as an advanced ensemble learning method.

Unlike traditional linear models, Gradient Boosting can:

- capture nonlinear physiological relationships
- learn complex feature interactions
- model subtle ICU deterioration patterns
- improve predictive robustness

This approach significantly improved physiological pattern recognition compared to previous baseline models.

---

# Baseline Gradient Boosting Results

## Performance Metrics

| Metric    | Value |
| --------- | ----- |
| Accuracy  | 0.84  |
| Precision | 0.33  |
| Recall    | 0.33  |
| F1-score  | 0.33  |
| ROC-AUC   | 0.79  |

## Clinical Interpretation

The baseline Gradient Boosting model achieved stronger discriminatory performance compared to previous traditional machine learning approaches.

Key improvements included:

- higher ROC-AUC
- improved nonlinear learning
- successful septic patient detection without balancing

However, septic patient recall remained limited because some septic patients were still missed.

---

# SMOTE-Enhanced Gradient Boosting

## SMOTE Balancing

Synthetic Minority Oversampling Technique (SMOTE) was applied to improve minority-class representation during training.

SMOTE generated synthetic septic patient examples to help the model better learn physiological deterioration patterns associated with sepsis.

---

# Gradient Boosting + SMOTE Results

## Performance Metrics

| Metric    | Value |
| --------- | ----- |
| Accuracy  | 0.80  |
| Precision | 0.33  |
| Recall    | 0.67  |
| F1-score  | 0.44  |
| ROC-AUC   | 0.76  |

## Clinical Interpretation

The SMOTE-enhanced model substantially improved septic patient detection performance.

### Main Improvement

Recall improved from:

```text
0.33 → 0.67
```
