# Week 3 Day 4 — Patient Search and Filtering

## Overview

Week 3 Day 4 focused on improving the usability and interactivity of the ICU Early Warning Prediction dashboard by introducing patient search and dynamic filtering capabilities.

While previous stages enabled patient monitoring and prioritization, this stage allows clinicians to rapidly locate individual patients and narrow the monitoring view to specific risk groups.

These functionalities simulate features commonly found in real-world clinical monitoring systems.

---

# Objectives

The objectives of this stage were:

- Enable patient search by Patient ID
- Introduce dynamic risk category filtering
- Improve navigation through patient records
- Enhance clinical workflow efficiency
- Support prioritization of patients requiring intervention

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

## 1. Load Patient Prediction Data

The dashboard continued using the prediction outputs generated during Week 2.

The following datasets were utilized:

```text
dashboard_data/
├── dashboard_patient_predictions.csv
└── dashboard_top_10_high_risk_patients.csv
```

---

## 2. Implement Patient Search

A search component was added to allow clinicians to retrieve patient information using Patient IDs.

The search functionality enables users to:

- display all patients,
- select a specific patient,
- quickly retrieve individual records.

This reduces the time required to locate patient information.

---

## 3. Introduce Risk Category Filtering

Dynamic filtering was implemented using the dashboard's risk classifications.

Users can select one or multiple categories:

- Low Risk
- Moderate Risk
- Critical Risk

The patient monitoring table updates automatically based on the selected filters.

---

## 4. Update Filtered Monitoring View

A filtered patient table was integrated into the dashboard.

The table displays only the patients matching the selected search criteria and risk filters.

This provides a focused monitoring environment for clinical review.

---

## 5. Maintain High-Risk Prioritization

The Top 10 Highest-Risk Patients section remained accessible regardless of filter selections.

This ensures that the most urgent cases are continuously visible to clinicians.

---

# Generated Outputs

## Dashboard Screenshot

```text
figures/day18_patient_search/
└── dashboard_patient_search.png
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

## Interactive Dashboard Features

The dashboard successfully incorporated dynamic patient exploration capabilities.

| Feature                 | Status    |
| ----------------------- | --------- |
| Patient Search          | Completed |
| Risk Category Filtering | Completed |
| Dynamic Patient Table   | Completed |
| Top 10 Risk Monitoring  | Completed |

---

## Filtered Patient Monitoring

When all risk categories were selected, the dashboard displayed:

```text
Filtered Patients: 100
```

representing the complete monitored ICU population.

The filtering functionality allows clinicians to immediately focus on smaller subsets of interest by selecting only the desired risk categories.

---

# Dashboard Preview

![Patient Search Dashboard](../../figures/day18_patient_search/dashboard_patient_search.png)

The dashboard now supports interactive patient retrieval and filtering, improving the efficiency of clinical review.

---

# Clinical Interpretation

ICU environments require rapid access to relevant patient information.

Patient search functionality enables clinicians to immediately retrieve records without manually reviewing large patient lists.

Risk category filtering further improves efficiency by allowing healthcare professionals to focus on patients requiring closer observation.

These capabilities contribute to faster decision-making and improved prioritization.

---

# Deployment Importance

This stage transformed the dashboard from a static monitoring interface into an interactive clinical tool.

The application now supports workflows commonly observed in healthcare information systems, including:

- individual patient retrieval,
- targeted monitoring,
- risk-based prioritization,
- and dynamic review of patient populations.

Such features increase the practicality of the ICU Early Warning Prediction System for potential clinical deployment.

---

# Conclusion

Week 3 Day 4 successfully introduced patient search and dynamic filtering capabilities into the ICU Early Warning Prediction dashboard.

The system now supports:

- patient identification through search,
- interactive filtering by risk category,
- focused patient monitoring,
- continued prioritization of critical cases,
- and enhanced clinical usability.

This milestone further advances the project toward becoming a fully interactive and deployment-ready clinical decision support system.
