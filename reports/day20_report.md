# Week 3 Day 6 — SHAP Dashboard Integration

## Overview

Week 3 Day 6 focused on integrating explainable artificial intelligence (XAI) into the ICU Early Warning Prediction dashboard using SHAP (SHapley Additive exPlanations).

While previous dashboard stages provided predictions, monitoring, and patient prioritization, this stage aimed to improve transparency by explaining how physiological variables influenced the model's predictions.

The Explainability Dashboard enables users to understand both global model behavior and individual prediction rationale, reducing the "black-box" nature of machine learning in healthcare.

---

# Objectives

The objectives of this stage were:

- Integrate SHAP outputs into the Streamlit dashboard
- Present global model explainability
- Visualize feature importance
- Display patient-level explanation examples
- Improve transparency and trust in model predictions
- Support explainable clinical decision-making

---

# Technologies Used

- Python
- Streamlit
- SHAP
- Pandas
- Matplotlib
- VS Code
- Git
- GitHub

---

# Workflow

## 1. Reuse Previously Generated SHAP Outputs

The explainability dashboard utilized SHAP visualizations generated during Week 2.

The following explainability figures were incorporated:

```text
figures/day8_shap_explainability/
├── shap_summary_plot.png
├── shap_bar_plot.png
├── shap_waterfall_high_risk.png
└── shap_waterfall_low_risk.png
```

These visualizations were reused to improve deployment efficiency without recomputing SHAP values during dashboard execution.

---

## 2. Integrate Global Model Explainability

A dedicated section was added to display the SHAP Summary Plot.

The SHAP summary plot illustrates:

- the relative importance of physiological variables,
- how feature values influence predictions,
- variability of feature effects across ICU patients.

This provides an overview of how the Gradient Boosting + SMOTE model behaves globally.

---

## 3. Display Global Feature Importance

The SHAP Feature Importance (bar plot) was integrated into the dashboard.

This visualization highlights the average contribution of each feature to model predictions.

The most influential variables included:

- ICULOS_max,
- HR_min,
- Temp_mean,
- HR_mean,
- SBP_mean,
- Age_first,
- MAP_mean.

These findings aligned with previous analyses conducted during Week 2.

---

## 4. Present Patient-Level Explainability

Patient-level SHAP waterfall plots were incorporated to demonstrate how individual physiological variables contributed to a prediction.

These visualizations show:

- factors increasing predicted sepsis risk,
- factors decreasing predicted sepsis risk,
- the cumulative effect of features on the final prediction.

This enables clinicians to understand why the model classified a patient as low risk or critical risk.

---

## 5. Add Clinical Interpretation Panel

A clinical interpretation section was added to explain SHAP outputs using non-technical language.

The interpretation emphasized that:

- positive SHAP values increase predicted risk,
- negative SHAP values reduce predicted risk,
- explanations can improve clinician confidence and facilitate adoption of AI systems.

---

# Generated Outputs

## Dashboard Screenshot

```text
figures/day20_shap_dashboard/
└── dashboard_shap_view.png
```

## Updated Application Files

```text
app/
├── streamlit_app.py
├── config.py
└── utils.py
```

---

# Results and Findings

## Explainability Dashboard Features

The dashboard successfully integrated multiple explainability components.

| Feature                              | Status    |
| ------------------------------------ | --------- |
| SHAP Summary Plot                    | Completed |
| SHAP Global Feature Importance       | Completed |
| Patient-Level Waterfall Example      | Completed |
| Clinical Interpretation Panel        | Completed |
| Explainability Dashboard Integration | Completed |

---

## Global Model Insights

The SHAP summary analysis revealed that ICU Length of Stay (ICULOS_max), Heart Rate measurements, and Temperature variables had substantial influence on model predictions.

These variables consistently appeared among the strongest contributors to sepsis risk estimation.

Importantly, the identified features aligned with clinically meaningful physiological indicators associated with patient deterioration.

---

## Explainable Predictions

The waterfall plots demonstrated that predictions were not arbitrary.

Instead, they resulted from the combined contribution of multiple physiological factors.

This transparency allows users to investigate why predictions were generated and supports more informed interpretation of model outputs.

---

# Dashboard Preview

![Explainability Dashboard](../../figures/day20_shap_dashboard/dashboard_shap_view.png)

The Explainability Dashboard integrates global and patient-level explanations directly into the clinical monitoring interface.

---

# Clinical Interpretation

One of the primary barriers to adopting machine learning in healthcare is the lack of transparency associated with black-box models.

By integrating SHAP explanations, the ICU Early Warning Prediction System provides clinicians with insight into the reasoning behind predictions.

Understanding which physiological variables contribute to increased or decreased sepsis risk can improve trust, support clinical validation, and encourage responsible use of AI-assisted decision support systems.

Although the current implementation displays pre-generated SHAP visualizations, the architecture establishes a foundation for future development of real-time patient-specific explanations.

---

# Deployment Importance

This stage significantly strengthened the interpretability of the healthcare AI system.

The dashboard now combines:

- predictive analytics,
- patient monitoring,
- risk prioritization,
- and explainable artificial intelligence.

These capabilities move the project beyond traditional machine learning demonstrations and closer to the characteristics expected from modern clinical decision support systems.

---

# Conclusion

Week 3 Day 6 successfully integrated SHAP explainability into the ICU Early Warning Prediction dashboard.

The system now supports:

- global model transparency,
- feature importance visualization,
- patient-level explanation examples,
- clinician-friendly interpretation of predictions,
- and explainable healthcare AI principles.

This milestone represents a major advancement toward trustworthy and interpretable deployment-oriented healthcare AI solutions and prepares the project for the final review and consolidation phase of Week 3.
