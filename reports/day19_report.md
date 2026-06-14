# Week 3 Day 5 — Single Patient Dashboard

## Overview

Week 3 Day 5 focused on introducing a patient-centered dashboard view within the ICU Early Warning Prediction System.

While previous stages provided population-level monitoring and patient filtering capabilities, this stage enabled clinicians to review detailed prediction outputs for an individual patient.

The dashboard now supports personalized clinical review by presenting risk information, alert levels, and prediction summaries for selected patients.

---

# Objectives

The objectives of this stage were:

- Develop a single-patient dashboard interface
- Allow clinicians to select individual patients
- Display patient-specific prediction metrics
- Present risk categories and alert levels
- Improve transparency and usability of model outputs

---

# Technologies Used

- Python
- Streamlit
- Pandas
- VS Code
- Git
- GitHub

---

# Workflow

## 1. Load Patient-Level Prediction Data

The dashboard continued using the patient prediction outputs generated during Week 2.

The following dataset was utilized:

```text
dashboard_data/
└── dashboard_patient_predictions.csv
```

This dataset contains individual patient predictions and associated clinical information.

---

## 2. Implement Patient Selection

A patient selector was integrated into the dashboard using a dropdown menu.

Clinicians can now choose a specific patient from the monitored ICU population to review detailed information.

This functionality mimics patient overview interfaces commonly found in electronic health record systems.

---

## 3. Display Patient Risk Metrics

For each selected patient, the dashboard displays key prediction indicators:

- Risk Score Percentage
- Sepsis Probability
- Risk Category
- Clinical Alert Level

These metrics provide a concise summary of the patient's predicted condition.

---

## 4. Present Detailed Patient Information

A detailed patient information table was added to display the complete prediction record associated with the selected patient.

The table includes:

- Patient ID
- True Sepsis Label
- Predicted Sepsis Label
- Sepsis Probability
- Risk Score Percentage
- Risk Category
- Clinical Alert Level

This allows clinicians to review both summarized and detailed information simultaneously.

---

# Generated Outputs

## Dashboard Screenshot

```text
figures/day19_single_patient_dashboard/
└── dashboard_single_patient.png
```

## Updated Application Files

```text
app/
├── streamlit_app.py
├── utils.py
└── config.py
```

---

# Results and Findings

## Single Patient Dashboard Features

The dashboard successfully introduced individualized patient review capabilities.

| Feature                    | Status    |
| -------------------------- | --------- |
| Patient Selection          | Completed |
| Risk Score Display         | Completed |
| Sepsis Probability Display | Completed |
| Risk Category Display      | Completed |
| Clinical Alert Display     | Completed |
| Detailed Patient Table     | Completed |

---

## Individualized Clinical Review

The dashboard can now generate patient-specific summaries using the model's prediction outputs.

This enables clinicians to transition from population-level monitoring to detailed patient assessment.

The patient-centered design supports focused review and individualized decision-making.

---

# Dashboard Preview

![Single Patient Dashboard](../../figures/day19_single_patient_dashboard/dashboard_single_patient.png)

The dashboard now provides a dedicated view for reviewing prediction outputs associated with individual ICU patients.

---

# Clinical Interpretation

Early warning systems are most effective when clinicians can understand risk at the individual patient level.

Presenting patient-specific probabilities, alert levels, and classifications facilitates rapid interpretation of model outputs and supports targeted interventions.

This approach aligns with the principles of personalized medicine and clinical decision support.

By reducing the need to navigate large patient tables, the dashboard improves efficiency and allows healthcare professionals to focus on the patient currently under review.

---

# Deployment Importance

The introduction of a single-patient dashboard significantly improves the practicality of the ICU Early Warning Prediction System.

The application now supports workflows similar to those used in healthcare information systems, including:

- individualized patient review,
- targeted risk assessment,
- rapid access to prediction summaries,
- and integration of detailed patient information.

These capabilities increase the potential for future deployment in real clinical environments.

---

# Conclusion

Week 3 Day 5 successfully introduced a dedicated single-patient dashboard into the ICU Early Warning Prediction System.

The dashboard now supports:

- patient-specific selection,
- individualized prediction review,
- display of key risk metrics,
- clinical alert visualization,
- and detailed patient summaries.

This milestone establishes the foundation for the next stage of development: integrating SHAP explanations to help clinicians understand why the model generated a specific prediction for each patient.
