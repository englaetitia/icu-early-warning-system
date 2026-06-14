# Week 3 Day 1 — Streamlit Dashboard Setup

git

## Overview

Week 3 marked the transition of the ICU Early Warning Prediction System from research notebooks into an interactive healthcare AI application.

The objective of Day 1 was to establish the initial Streamlit dashboard architecture and create the first working version of the user interface.

This dashboard will eventually support:

- ICU patient monitoring
- Sepsis risk visualization
- Clinical alert management
- Explainable AI outputs
- Patient-level decision support

---

# Objectives

The objectives of this stage were:

- Install and configure Streamlit
- Build the initial dashboard structure
- Create reusable application files
- Implement sidebar navigation
- Develop the dashboard homepage
- Establish a deployment-oriented architecture

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

## 1. Dashboard Architecture Setup

A dedicated application folder was created to separate dashboard components from research notebooks.

### Application Structure

```text
app/
├── config.py
├── streamlit_app.py
└── utils.py
```

---

## 2. Configuration File

A configuration file was created to centralize dashboard settings, including:

- Application title
- Subtitle
- Sidebar title
- Page icon
- Layout configuration

---

## 3. Utility Functions

Reusable helper functions were introduced to simplify future dashboard development.

The initial utility module focused on loading CSV files that will later power dashboard visualizations.

---

## 4. Streamlit Dashboard Development

The first version of the dashboard was implemented.

The application included:

### Sidebar Navigation

- Home
- Patient Monitoring
- Risk Analytics
- Explainability
- System Information

### Homepage Components

- Dashboard title
- Healthcare AI description
- Current system capabilities
- Best-performing model information

---

# Generated Outputs

## Application Files

```text
app/
├── config.py
├── streamlit_app.py
└── utils.py
```

## Figures

```text
figures/day15_dashboard_setup/
└── dashboard_homepage.png
```

---

# Results and Findings

## First Interactive Dashboard

The Streamlit application successfully launched locally using:

```bash
python -m streamlit run streamlit_app.py
```

The dashboard was accessible through:

```text
http://localhost:8501
```

---

## Dashboard Features Implemented

The first dashboard version included:

| Feature                 | Status    |
| ----------------------- | --------- |
| Homepage                | Completed |
| Sidebar Navigation      | Completed |
| Dashboard Configuration | Completed |
| Utility Module          | Completed |
| Streamlit Integration   | Completed |

---

# Dashboard Preview

![Dashboard Homepage](../../figures/day15_dashboard_setup/dashboard_homepage.png)

The homepage provides an overview of the ICU Early Warning Prediction System and highlights its current capabilities.

---

# Clinical Interpretation

Although the dashboard currently displays static information, this stage represents a major milestone in the project's evolution.

The ICU Early Warning Prediction System has progressed from:

```text
Research Notebooks
        ↓
Explainable Machine Learning
        ↓
Interactive Healthcare AI Dashboard
```

This transition significantly improves usability and moves the project closer to real-world clinical deployment.

---

# Deployment Importance

Establishing the Streamlit infrastructure provides the foundation for future dashboard capabilities, including:

- patient-level monitoring
- sepsis risk visualization
- SHAP explainability panels
- ICU risk analytics
- real-time prediction interfaces

This architecture will support deployment-oriented healthcare AI workflows.

---

# Conclusion

Week 3 Day 1 successfully introduced the first interactive dashboard for the ICU Early Warning Prediction System.

The project now includes:

- a functional Streamlit application,
- deployment-oriented application structure,
- reusable dashboard components,
- interactive navigation,
- and a scalable foundation for future healthcare AI interfaces.

This milestone marks the beginning of transforming the project from a research prototype into an end-user clinical decision support application.
