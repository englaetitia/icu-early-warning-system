import streamlit as st
import pandas as pd

from config import *
from utils import load_csv, get_metric_value


st.set_page_config(
    page_title=APP_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT
)


summary_metrics = load_csv("dashboard_summary_metrics.csv")
risk_distribution = load_csv("dashboard_risk_distribution.csv")
patient_predictions = load_csv("dashboard_patient_predictions.csv")


st.title("🚑 ICU Early Warning Prediction System")

st.markdown(APP_SUBTITLE)

st.divider()


st.sidebar.title(SIDEBAR_TITLE)

page = st.sidebar.radio(
    "Select Dashboard Section",
    [
        "Home",
        "Patient Monitoring",
        "Risk Analytics",
        "Explainability",
        "System Information"
    ]
)


if page == "Home":

    st.header("ICU Overview")

    total_patients = get_metric_value(summary_metrics, "Total Patients")
    true_sepsis_cases = get_metric_value(summary_metrics, "True Sepsis Cases")
    predicted_sepsis_cases = get_metric_value(summary_metrics, "Predicted Sepsis Cases")
    high_critical_patients = get_metric_value(summary_metrics, "High or Critical Risk Patients")
    average_risk_score = get_metric_value(summary_metrics, "Average Risk Score (%)")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        label="Total ICU Patients",
        value=int(total_patients)
    )

    col2.metric(
        label="True Sepsis Cases",
        value=int(true_sepsis_cases)
    )

    col3.metric(
        label="Predicted Sepsis Cases",
        value=int(predicted_sepsis_cases)
    )

    col4.metric(
        label="Avg Risk Score",
        value=f"{float(average_risk_score):.2f}%"
    )

    st.divider()

    st.subheader("Risk Category Distribution")

    st.bar_chart(
        risk_distribution.set_index("Risk_Category")["Number_of_Patients"]
    )

    st.divider()

    st.info("Current best model: Gradient Boosting + SMOTE")


elif page == "Patient Monitoring":

    st.header("Patient Monitoring")

    patient_data = patient_predictions.copy()

    st.subheader("Patient Search")

    patient_ids = patient_data["Patient_ID"].astype(str).unique()

    selected_patient = st.selectbox(
        "Search by Patient ID",
        options=["All Patients"] + sorted(patient_ids.tolist())
    )

    if selected_patient != "All Patients":

        patient_data = patient_data[
            patient_data["Patient_ID"].astype(str) == selected_patient
        ]

    st.subheader("Risk Category Filter")

    risk_options = patient_predictions["Risk_Category"].unique()

    selected_risks = st.multiselect(
        "Select Risk Categories",
        options=risk_options,
        default=risk_options
    )

    patient_data = patient_data[
        patient_data["Risk_Category"].isin(selected_risks)
    ]

    st.divider()

    st.subheader(
        f"Filtered Patients ({len(patient_data)})"
    )

    st.dataframe(
        patient_data,
        use_container_width=True
    )

    st.divider()

    st.subheader("Top 10 Highest-Risk Patients")

    st.dataframe(
        load_csv("dashboard_top_10_high_risk_patients.csv"),
        use_container_width=True
    )


elif page == "Risk Analytics":

    st.header("Single Patient Dashboard")

    patient_ids = patient_predictions["Patient_ID"].astype(str)

    selected_patient_id = st.selectbox(
        "Select Patient",
        sorted(patient_ids.tolist())
    )

    patient = patient_predictions[
        patient_predictions["Patient_ID"].astype(str)
        == selected_patient_id
    ].iloc[0]

    st.subheader(f"Patient: {selected_patient_id}")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Risk Score",
        f"{patient['Risk_Score_Percent']:.2f}%"
    )

    col2.metric(
        "Sepsis Probability",
        f"{patient['Sepsis_Probability']:.3f}"
    )

    col3.metric(
        "Risk Category",
        patient["Risk_Category"]
    )

    col4.metric(
        "Clinical Alert",
        patient["Clinical_Alert_Level"]
    )

    st.divider()

    st.subheader("Patient Details")

    st.dataframe(
        patient.to_frame().T,
        use_container_width=True
    )


elif page == "Explainability":

    st.header("Explainability")

    st.write("This section will display SHAP explainability outputs.")


elif page == "System Information":

    st.header("System Information")

    st.write("Project: ICU Early Warning Prediction System")

    st.write("Version: 1.0")

    st.write("Best Model: Gradient Boosting + SMOTE")

    st.write("Current Stage: Week 3 Dashboard Development")