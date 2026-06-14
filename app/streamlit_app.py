import streamlit as st

from config import *


st.set_page_config(
    page_title=APP_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT
)


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

    st.header("Welcome")

    st.write(
        """
        This dashboard provides an interactive interface for the
        ICU Early Warning Prediction System.

        Current capabilities include:

        - Patient-level risk prediction
        - Explainable AI using SHAP
        - Clinical alert generation
        - Dashboard-ready healthcare analytics
        """
    )

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