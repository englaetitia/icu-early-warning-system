# Week 3 Day 3 — Patient Monitoring Dashboard

## Overview

Week 3 Day 3 focused on transforming the Streamlit dashboard into a patient-centered ICU monitoring system.

Building upon the summary metrics introduced in Day 16, the dashboard was enhanced to display individual patient predictions, identify high-risk patients, and prioritize cases requiring urgent clinical attention.

This stage introduced patient-level monitoring capabilities similar to those found in clinical decision support systems.

---

# Objectives

The objectives of this stage were:

- Display patient-level prediction outputs
- Create an interactive ICU monitoring table
- Identify high-risk and critical-risk patients
- Prioritize patients requiring urgent review
- Improve the dashboard's clinical usability

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

## 1. Load Patient Monitoring Data

The dashboard was connected to the patient-level prediction outputs generated during Week 2.

The following files were used:

```text
dashboard_data/
├── dashboard_patient_predictions.csv
└── dashboard_top_10_high_risk_patients.csv
```

---

## 2. Display All ICU Patients

An interactive monitoring table was added using Streamlit.

The table displayed:

- Patient ID
- True Sepsis Label
- Predicted Sepsis Label
- Sepsis Probability
- Risk Score Percentage
- Risk Category
- Clinical Alert Level

This provided a complete overview of all monitored ICU patients.

---

## 3. Display Top 10 Highest-Risk Patients

A dedicated section was created to highlight the patients with the highest predicted sepsis risk.

These patients represent the most urgent cases identified by the model.

---

## 4. Identify High/Critical Risk Patients

Patients classified as:

- High Risk
- Critical Risk

were isolated into a separate monitoring table.

This allows clinicians to focus on patients requiring immediate attention.

---

# Generated Outputs

## Dashboard Screenshot

```text
figures/day17_patient_monitoring/
└── dashboard_patient_monitoring.png
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

## ICU Patient Monitoring

The dashboard successfully displayed patient-level prediction results for all ICU patients.

The monitoring interface included:

| Feature                       | Status    |
| ----------------------------- | --------- |
| All ICU Patients Table        | Completed |
| Top 10 Highest-Risk Patients  | Completed |
| High/Critical Risk Monitoring | Completed |
| Clinical Alert Display        | Completed |

---

## High-Risk Patient Detection

The dashboard identified:

```text
17 High/Critical Risk Patients
```

requiring closer monitoring.

This value matched the summary metrics displayed during Week 3 Day 2:

```text
Predicted Sepsis Cases = 17
```

demonstrating consistency across dashboard components.

---

# Dashboard Preview

![Patient Monitoring Dashboard](../../figures/day17_patient_monitoring/dashboard_patient_monitoring.png)

The dashboard now supports patient-level monitoring and prioritization of high-risk individuals.

---

# Clinical Interpretation

One of the major challenges in ICU environments is prioritizing which patients require immediate attention.

Rather than reviewing all monitored patients equally, the dashboard now enables clinicians to:

- review individual patient predictions,
- identify critical-risk cases,
- prioritize urgent reviews,
- support more efficient decision-making.

The ability to isolate the highest-risk patients represents an important feature of early warning systems.

---

# Deployment Importance

This stage significantly improved the practical utility of the ICU Early Warning Prediction System.

The dashboard evolved from displaying population-level summaries to supporting patient-centered monitoring workflows.

The application now provides functionality similar to real-world clinical dashboards by enabling rapid identification of patients requiring intervention.

---

# Conclusion

Week 3 Day 3 successfully introduced patient-level monitoring into the ICU Early Warning Prediction System.

The dashboard now supports:

- complete ICU patient review,
- high-risk patient prioritization,
- top-risk patient identification,
- clinical alert visualization,
- and patient-centered monitoring workflows.

This milestone moves the project closer to becoming a fully interactive clinical decision support application.
