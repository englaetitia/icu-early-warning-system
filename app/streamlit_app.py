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

    st.write("This section will display ICU patient-level risk predictions.")


elif page == "Risk Analytics":

    st.header("Risk Analytics")

    st.write("This section will display ICU risk distribution and summary metrics.")


elif page == "Explainability":

    st.header("Explainability")

    st.write("This section will display SHAP explainability outputs.")


elif page == "System Information":

    st.header("System Information")

    st.write("Project: ICU Early Warning Prediction System")

    st.write("Version: 1.0")

    st.write("Best Model: Gradient Boosting + SMOTE")

    st.write("Current Stage: Week 3 Dashboard Development")