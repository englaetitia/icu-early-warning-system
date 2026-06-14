# Week 2 Day 2 — Patient-Level Risk Scoring

## Overview

Week 2 Day 2 focused on converting raw model probabilities into clinically understandable patient risk categories.

Instead of only generating binary predictions:

- 0 = Non-Septic
- 1 = Septic

the system now generates:

- sepsis probability
- risk score percentage
- risk category
- clinical alert level

---

# Objectives

The objectives of this stage were:

- Create clinically interpretable risk scores
- Categorize patient severity levels
- Improve ICU monitoring usability
- Prioritize high-risk patients
- Move closer toward deployment-ready outputs

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Gradient Boosting
- SMOTE

---

# Workflow

## 1. Reload Saved Model Pipeline

The Gradient Boosting + SMOTE workflow was rebuilt.

## 2. Generate Prediction Probabilities

The model generated sepsis probabilities for ICU patients.

## 3. Convert Probabilities Into Risk Scores

Probabilities were converted into percentage-based risk scores.

## 4. Assign Risk Categories

Patients were categorized into:

| Risk Score | Category      |
| ---------- | ------------- |
| 0–25%      | Low Risk      |
| 25–50%     | Moderate Risk |
| 50–75%     | High Risk     |
| 75–100%    | Critical Risk |

## 5. Generate Clinical Alert Levels

Clinical alert messages were added for patient prioritization.

---

# Generated Outputs

## Figures

```text
figures/day9_patient_risk_scoring/
└── risk_category_distribution.png
```

## Results

```text
results/
├── day9_patient_level_risk_scores.csv
├── day9_risk_category_distribution.csv
└── day9_high_risk_patients.csv
```

---

# Key Findings

## Risk Distribution

The generated patient distribution showed:

- Most patients were classified as Low Risk
- A smaller group was classified as Critical Risk
- Moderate Risk patients appeared less frequently

The model was selective when assigning extremely high-risk classifications.

---

# Clinical Interpretation

The risk scoring framework improved the clinical usability of the system.

Instead of returning only predictions, the system now provides:

- interpretable risk levels
- severity-based categorization
- clinical monitoring recommendations

This enables:

- patient prioritization
- ICU monitoring support
- clinician-friendly interpretation

---

# Conclusion

Week 2 Day 2 successfully introduced patient-level risk scoring into the ICU Early Warning Prediction System.

The system can now:

- estimate patient severity
- categorize clinical risk
- generate interpretable alert levels

This was an important step toward real-world deployment and dashboard integration.
