# Week 2 Day 4 — Single-Patient Prediction Pipeline

## Overview

Week 2 Day 4 focused on building a reusable single-patient prediction pipeline for the ICU Early Warning Prediction System.

The objective was to simulate how the deployed model would operate in a real ICU workflow by predicting sepsis risk for one patient at a time.

The system now supports:

- single-patient inference
- sepsis probability estimation
- patient-level risk scoring
- clinical alert generation

---

# Objectives

The objectives of this stage were:

- Build a reusable patient-level inference pipeline
- Generate prediction probabilities for individual patients
- Create patient-level risk categories
- Generate clinical alert messages
- Prepare the project for dashboard integration

---

# Technologies Used

- Python
- Pandas
- NumPy
- Joblib
- Scikit-learn
- Gradient Boosting
- SMOTE

---

# Workflow

## 1. Load Saved Model

The saved Gradient Boosting + SMOTE model was reloaded using `joblib`.

## 2. Load Saved Feature Names

The saved feature structure was restored to ensure prediction consistency.

## 3. Load Processed ICU Dataset

The patient-level processed dataset from Week 1 was loaded.

## 4. Create Risk Categorization Logic

Prediction probabilities were converted into clinical risk categories:

| Risk Score | Category      |
| ---------- | ------------- |
| 0–25%      | Low Risk      |
| 25–50%     | Moderate Risk |
| 50–75%     | High Risk     |
| 75–100%    | Critical Risk |

## 5. Generate Clinical Alert Levels

Alert messages were added to improve patient prioritization.

## 6. Build Single-Patient Prediction Function

A reusable prediction function was created to automate:

- prediction generation
- risk scoring
- alert assignment

## 7. Generate Example Predictions

The system generated predictions for multiple ICU patients.

---

# Generated Outputs

## Results

```text id="3s0u6f"
results/
├── day11_single_patient_prediction.csv
└── day11_example_patient_predictions.csv
```

---

# Results and Findings

## Single-Patient Inference

The pipeline successfully generated:

- predicted sepsis label
- prediction probability
- risk score percentage
- clinical risk category
- clinical alert message

for individual ICU patients.

---

# Example Prediction Workflow

For each patient, the system produced:

| Output             | Description               |
| ------------------ | ------------------------- |
| Predicted Label    | Septic / Non-Septic       |
| Sepsis Probability | Model confidence          |
| Risk Score         | Percentage-based severity |
| Risk Category      | Clinical severity level   |
| Clinical Alert     | Monitoring recommendation |

---

# Clinical Interpretation

The single-patient prediction pipeline significantly improved deployment readiness.

The project can now operate on:

- one patient at a time
- reusable inference logic
- deployment-style workflows

This supports future integration into:

- dashboards
- APIs
- ICU monitoring systems
- real-time healthcare interfaces

---

# Deployment Importance

This stage transformed the project from notebook-based experimentation into a reusable inference architecture.

The pipeline now supports:

- scalable prediction workflows
- deployment integration
- individualized patient monitoring
- real-world clinical interface preparation

---

# Conclusion

Week 2 Day 4 successfully introduced reusable single-patient prediction capabilities into the ICU Early Warning Prediction System.

The project can now:

- perform patient-level inference
- generate risk scores
- create clinical alerts
- support deployment-oriented workflows

This established the foundation for explainable patient-level prediction in the next stage.
