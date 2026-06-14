# Week 3 Day 2 — Dashboard Summary Metrics

## Overview

Week 3 Day 2 focused on connecting the Streamlit dashboard to the real dashboard-ready outputs generated during Week 2.

In Week 3 Day 1, the dashboard structure was created.
In Day 2, the dashboard became data-driven by displaying ICU-level summary metrics and patient risk distribution using real model outputs.

---

# Objectives

The objectives of this stage were:

- Load dashboard-ready CSV files
- Display ICU-level summary metrics
- Visualize patient risk category distribution
- Connect the dashboard to real prediction outputs
- Improve clinical monitoring usability

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

## 1. Load Dashboard Data

The dashboard was connected to the CSV files generated during Week 2:

```text
dashboard_data/
├── dashboard_patient_predictions.csv
├── dashboard_risk_distribution.csv
├── dashboard_summary_metrics.csv
├── dashboard_top_10_high_risk_patients.csv
└── dashboard_clinical_view.csv
```

---

## 2. Update Utility Functions

The `utils.py` file was updated to support reusable loading of dashboard CSV files.

A helper function was also added to extract metric values from the summary metrics table.

---

## 3. Display ICU Overview Metrics

The dashboard homepage was updated to display ICU-level summary cards.

The following metrics were shown:

| Metric                 |  Value |
| ---------------------- | -----: |
| Total ICU Patients     |    100 |
| True Sepsis Cases      |     14 |
| Predicted Sepsis Cases |     17 |
| Average Risk Score     | 17.69% |

---

## 4. Visualize Risk Category Distribution

A risk category distribution chart was added to show how patients were classified by clinical risk level.

The dashboard displayed patient counts across:

- Low Risk
- Moderate Risk
- Critical Risk

---

# Generated Outputs

## Updated Application Files

```text
app/
├── streamlit_app.py
├── utils.py
└── config.py
```

## Dashboard Screenshot

```text
figures/day16_summary_metrics/
└── dashboard_summary_metrics.png
```

---

# Results and Findings

## ICU Summary Metrics

The dashboard successfully displayed real prediction results from the saved Week 2 outputs.

### Key observations:

- The dashboard monitored **100 ICU patients**
- There were **14 true sepsis cases**
- The model predicted **17 sepsis cases**
- The average risk score across patients was **17.69%**

---

# Dashboard Preview

![Dashboard Summary Metrics](../../figures/day16_summary_metrics/dashboard_summary_metrics.png)

The dashboard now provides an ICU-level overview with live summary metrics and patient risk distribution.

---

# Clinical Interpretation

The dashboard metrics provide a high-level overview of ICU patient risk status.

The difference between true sepsis cases and predicted sepsis cases shows that the model is slightly more cautious, flagging more patients than the actual number of septic cases.

In healthcare AI, this can be clinically reasonable because missing a septic patient may be more dangerous than reviewing a few additional alerts.

The average risk score of **17.69%** suggests that most patients are currently classified as relatively low risk, while a smaller subset requires closer monitoring.

---

# Deployment Importance

This stage transformed the Streamlit dashboard from a static interface into a data-driven healthcare monitoring tool.

The dashboard can now:

- read prediction outputs
- display ICU-level metrics
- visualize patient risk categories
- support clinical monitoring workflows

This is an important step toward building a real clinical decision support interface.

---

# Conclusion

Week 3 Day 2 successfully connected the ICU Early Warning Prediction dashboard to real prediction outputs.

The system now provides:

- ICU summary metrics
- patient risk distribution visualization
- real dashboard data integration
- early clinical monitoring functionality

This prepares the project for Week 3 Day 3, where individual patient monitoring tables will be added.
