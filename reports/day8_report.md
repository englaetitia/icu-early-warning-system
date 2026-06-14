# Week 2 Day 1 — SHAP Explainability

## Overview

Week 2 Day 1 focused on adding explainability to the ICU Early Warning Prediction System using SHAP (SHapley Additive exPlanations).

The previously selected best-performing model:

- **Gradient Boosting + SMOTE**

was analyzed to understand how physiological variables influenced sepsis predictions.

---

# Objectives

The objectives of this stage were:

- Introduce explainable AI into the project
- Interpret model decision behavior
- Identify the most influential physiological variables
- Generate patient-level prediction explanations
- Improve transparency and clinical trust

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SHAP
- Scikit-learn
- Gradient Boosting Classifier
- SMOTE

---

# Workflow

## 1. Reload Processed ICU Dataset

The processed patient-level ICU dataset from Week 1 was loaded.

## 2. Rebuild Best Model

The Gradient Boosting + SMOTE model was retrained.

## 3. Generate SHAP Values

SHAP values were generated for all test patients.

## 4. Create Explainability Visualizations

The following explainability outputs were generated:

- SHAP Summary Plot
- SHAP Feature Importance Plot
- Patient-Level SHAP Waterfall Plot

---

# Generated Outputs

## Figures

```text
figures/day8_shap_explainability/
├── shap_summary_plot.png
├── shap_bar_plot.png
└── patient_level_shap_waterfall.png
```

## Results

```text
results/
└── day8_shap_feature_importance.csv
```

---

# Key Findings

## Most Important Features

The SHAP analysis identified the following variables as the most influential:

1. ICULOS_max
2. HR_min
3. Temp_mean
4. HR_mean
5. SBP_mean
6. Age_first
7. MAP_mean

These variables contributed most strongly to the model’s sepsis predictions.

---

# SHAP Summary Interpretation

The SHAP summary plot demonstrated how physiological variables affected prediction behavior across all patients.

### Important observations:

- Longer ICU stay increased prediction impact
- Heart rate abnormalities strongly influenced predictions
- Temperature variation contributed significantly
- Blood pressure variables affected risk estimation
- Oxygen saturation contributed moderately

The model successfully learned clinically meaningful physiological relationships.

---

# Patient-Level Explanation

A SHAP waterfall plot was generated for an individual ICU patient.

### Main contributing factors:

#### Features reducing predicted risk:

- ICULOS_max
- HR_min
- Temp_mean
- SBP_mean

#### Features increasing predicted risk:

- Age_first
- HR_mean
- O2Sat_min

This demonstrates that the system can provide interpretable patient-specific explanations.

---

# Clinical Interpretation

Explainability is essential in healthcare AI because clinicians require understanding behind model predictions.

The SHAP framework improved:

- transparency
- interpretability
- clinician trust
- deployment readiness

This stage transformed the project from a predictive model into a more explainable medical AI system.

---

# Conclusion

Week 2 Day 1 successfully introduced explainable AI into the ICU Early Warning Prediction System.

The system can now:

- identify influential physiological variables
- explain individual patient predictions
- provide interpretable reasoning behind sepsis alerts

This established the foundation for patient-level risk scoring and explainable clinical inference in later stages.
