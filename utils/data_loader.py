import os
import pandas as pd


# --------------------------------------------------
# LOAD SAMPLE DATA
# --------------------------------------------------
def load_sample_data():

    try:

        df = pd.read_csv(
            "dataset/sample_sales.csv",
            encoding="latin1"
        )

        return df

    except Exception:

        return None


# --------------------------------------------------
# SAVE UPLOADED DATA
# --------------------------------------------------
def save_uploaded_data(
    df
):

    try:

        df.to_csv(
            "dataset/uploaded_sales.csv",
            index=False
        )

        return True

    except Exception:

        return False


# --------------------------------------------------
# LOAD UPLOADED DATA
# --------------------------------------------------
def load_uploaded_data():

    try:

        df = pd.read_csv(
            "dataset/uploaded_sales.csv",
            encoding="latin1"
        )

        return df

    except Exception:

        return None


# --------------------------------------------------
# SAVE PROCESSED DATA
# --------------------------------------------------
def save_processed_data(
    df
):

    try:

        df.to_csv(
            "dataset/processed_sales.csv",
            index=False
        )

        return True

    except Exception:

        return False


# --------------------------------------------------
# LOAD ACTIVE DATASET
# --------------------------------------------------
def load_processed_data():

    try:

        if os.path.exists(
            "dataset/processed_sales.csv"
        ):

            return pd.read_csv(
                "dataset/processed_sales.csv",
                encoding="latin1"
            )

        elif os.path.exists(
            "dataset/uploaded_sales.csv"
        ):

            return pd.read_csv(
                "dataset/uploaded_sales.csv",
                encoding="latin1"
            )

        else:

            return pd.read_csv(
                "dataset/sample_sales.csv",
                encoding="latin1"
            )

    except Exception:

        return None
# --------------------------------------------------
# LOAD ACTIVE DATASET
# --------------------------------------------------
def load_active_data():

    uploaded_df = load_uploaded_data()

    if uploaded_df is not None:

        return uploaded_df

    return load_sample_data()    