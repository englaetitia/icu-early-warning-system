# Week 2 Day 5 — Explainable Patient Prediction

## Overview

Week 2 Day 5 focused on combining:

- patient-level prediction
- clinical risk scoring
- SHAP explainability

into one explainable healthcare AI workflow.

The ICU Early Warning Prediction System can now generate:

- sepsis prediction
- risk category
- alert level
- patient-specific explanation

for individual ICU patients.

---

# Objectives

The objectives of this stage were:

- Combine explainability with patient inference
- Explain individual patient predictions
- Identify top physiological contributors
- Improve clinical transparency
- Build explainable healthcare AI outputs

---

# Technologies Used

- Python
- Pandas
- NumPy
- SHAP
- Joblib
- Scikit-learn
- Gradient Boosting
- SMOTE

---

# Workflow

## 1. Reload Saved Model

The saved Gradient Boosting + SMOTE model was loaded.

## 2. Load Processed ICU Dataset

The patient-level processed dataset was reloaded.

## 3. Generate Patient-Level Predictions

The system generated:

- prediction probability
- risk score
- risk category
- clinical alert

for individual patients.

## 4. Create SHAP Explainer

A SHAP explainer object was generated for the trained model.

## 5. Generate Patient-Level SHAP Values

SHAP values were calculated for individual patients.

## 6. Create SHAP Waterfall Explanation

A waterfall visualization was generated to explain prediction behavior.

## 7. Identify Top Risk Drivers

The most influential physiological variables were extracted.

---

# Generated Outputs

## Figures

```text id="9wov8j"
figures/day12_explainable_patient_prediction/
└── day12_single_patient_shap_waterfall.png
```

## Results

```text id="6gho4y"
results/
├── day12_single_patient_shap_explanation.csv
├── day12_explainable_single_patient_prediction.csv
└── day12_multiple_explainable_patient_predictions.csv
```

---

# Results and Findings

## Important Physiological Contributors

The explainable prediction workflow identified important contributing variables such as:

- ICULOS_max
- HR_mean
- Temp_mean
- Age_first
- MAP_mean
- O2Sat_mean

These variables strongly influenced patient-level prediction behavior.

---

# Figures

## Explainable Patient SHAP Waterfall Plot

![Explainable Patient SHAP Waterfall](../../figures/day12_explainable_patient_prediction/day12_single_patient_shap_waterfall.png)

The waterfall explanation demonstrates how physiological variables increased or decreased predicted sepsis risk for one patient.

---

# Patient-Level Interpretation

The explainable prediction framework identified:

### Features increasing predicted risk:

- MAP_mean
- HR_min
- O2Sat_mean

### Features decreasing predicted risk:

- ICULOS_max
- HR_mean
- Temp_mean

This demonstrates that prediction reasoning is individualized and clinically interpretable.

---

# Clinical Interpretation

Explainable patient-level predictions are critical in healthcare AI because clinicians require reasoning behind high-risk alerts.

The explainability framework improved:

- transparency
- interpretability
- clinician trust
- explainable clinical inference

The project now supports patient-specific clinical reasoning instead of black-box prediction behavior.

---

# Deployment Importance

This stage significantly improved deployment readiness because the system can now provide:

- prediction confidence
- risk severity
- explainable reasoning
- patient-level physiological interpretation

This is highly important for:

- clinician adoption
- dashboard integration
- healthcare AI transparency
- deployment credibility

---

# Conclusion

Week 2 Day 5 successfully introduced explainable patient-level prediction into the ICU Early Warning Prediction System.

The project can now:

- explain individual predictions
- identify influential physiological variables
- generate interpretable patient-level alerts
- support explainable healthcare AI workflows

This established the foundation for dashboard-ready explainable clinical inference.
