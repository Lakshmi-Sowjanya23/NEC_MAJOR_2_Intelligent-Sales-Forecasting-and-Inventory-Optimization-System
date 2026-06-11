import pandas as pd


# --------------------------------------------------
# LOAD FORECAST REPORT
# --------------------------------------------------
def load_forecast_report():

    try:

        forecast_df = pd.read_csv(
            "outputs/reports/forecast_results.csv"
        )

        return forecast_df

    except Exception:

        return None


# --------------------------------------------------
# LOAD INVENTORY REPORT
# --------------------------------------------------
def load_inventory_report():

    try:

        inventory_df = pd.read_csv(
            "outputs/reports/inventory_report.csv"
        )

        return inventory_df

    except Exception:

        return None


# --------------------------------------------------
# DATASET SUMMARY
# --------------------------------------------------
def get_dataset_summary(
    df
):

    summary = {

        "Rows":
            df.shape[0],

        "Columns":
            df.shape[1],

        "Numerical Columns":
            len(
                df.select_dtypes(
                    include="number"
                ).columns
            ),

        "Categorical Columns":
            len(
                df.select_dtypes(
                    exclude="number"
                ).columns
            )
    }

    return summary


# --------------------------------------------------
# SAVE REPORT
# --------------------------------------------------
def save_report(
    df,
    path
):

    df.to_csv(
        path,
        index=False
    )