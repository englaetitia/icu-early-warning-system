# ICU Early Warning Prediction System

## Week 1 — Day 1 Report

---

# Objective

The objective of Day 1 was to initialize the ICU Early Warning Prediction System project environment and perform the first exploration of the PhysioNet Sepsis Challenge dataset.

---

# Tasks Completed

## 1. Project Environment Setup

The project structure was created locally using VS Code.

Main folders created:

- data/
- notebooks/
- preprocessing/
- models/
- evaluation/
- dashboard/
- reports/

Required Python libraries were installed successfully.

---

## 2. GitHub Repository Initialization

A GitHub repository was created and connected to the local project using Git.

Initial project files and structure were pushed successfully.

---

## 3. Dataset Download and Extraction

The PhysioNet Sepsis Challenge 2019 dataset was downloaded and extracted.

Patient `.psv` files were placed inside:

`data/raw/`

Each file represents one ICU patient.

---

## 4. First Dataset Exploration

A first exploration notebook was created:

- `01_dataset_exploration.ipynb`

The notebook included:

- loading patient data,
- inspecting dataset shape,
- checking columns,
- analyzing missing values,
- identifying the target variable,
- first time-series visualization.

---

# Initial Observations

## Dataset Structure

- Each file corresponds to one ICU patient.
- Each row represents one hour of ICU monitoring.
- The dataset is time-series based.

---

## Medical Features

The dataset contains:

- vital signs,
- laboratory measurements,
- demographic information,
- sepsis labels.

Examples:

- Heart Rate (HR)
- Oxygen Saturation (O2Sat)
- Temperature (Temp)
- Respiratory Rate (Resp)

---

## Missing Values

A large number of missing values were observed in several medical features.

This indicates that preprocessing and missing data handling will be a critical phase of the project.

Several features showed extremely high missing percentages, including:

- EtCO2
- TroponinI
- Fibrinogen
- Lactate

---

## Prediction Target

The target variable is:

- `SepsisLabel`

Where:

- `0` = non-septic
- `1` = septic

The explored patient did not develop sepsis during the ICU stay.

---

## Time-Series Nature

The ICU dataset is fundamentally a time-series dataset.

The heart rate visualization demonstrated how patient measurements evolve over ICU hours.

This confirms that temporal modeling techniques such as LSTMs and Transformers may later be useful for this project.

---

# Challenges Encountered

- PhysioNet dataset download interface was initially confusing.
- Virtual environment setup issues occurred on Windows/PowerShell.
- Dataset extraction and organization required manual adjustments.

---

# Knowledge Gained

By the end of Day 1, the following concepts were understood:

- ICU data organization
- Time-series medical data structure
- Sepsis prediction objective
- Importance of preprocessing in healthcare AI
- Dataset exploration workflow
- Missing data challenges in medical datasets

---

# Next Steps (Day 2)

Planned tasks for Day 2:

- Learn ICU terminology in more detail
- Study sepsis progression and deterioration patterns
- Understand each medical feature clinically
- Begin deeper exploratory analysis

---

# Status

✅ Week 1 — Day 1 completed successfully.
