import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DASHBOARD_DATA_DIR = BASE_DIR / "dashboard_data"


def load_csv(file_name):
    file_path = DASHBOARD_DATA_DIR / file_name
    return pd.read_csv(file_path)


def get_metric_value(summary_df, metric_name):
    return summary_df.loc[
        summary_df["Metric"] == metric_name,
        "Value"
    ].values[0]