import pandas as pd


# --------------------------------------------------
# HANDLE MISSING VALUES
# --------------------------------------------------
def handle_missing_values(
    df,
    method
):

    df = df.copy()

    if method == "Drop Missing Values":

        df = df.dropna()

    elif method == "Fill Numerical Values with Mean":

        numerical_columns = df.select_dtypes(
            include="number"
        ).columns

        df[numerical_columns] = (
            df[numerical_columns]
            .fillna(
                df[numerical_columns].mean()
            )
        )

    elif method == "Fill Numerical Values with Median":

        numerical_columns = df.select_dtypes(
            include="number"
        ).columns

        df[numerical_columns] = (
            df[numerical_columns]
            .fillna(
                df[numerical_columns].median()
            )
        )

    elif method == "Fill Numerical Values with Zero":

        numerical_columns = df.select_dtypes(
            include="number"
        ).columns

        df[numerical_columns] = (
            df[numerical_columns]
            .fillna(0)
        )

    return df


# --------------------------------------------------
# REMOVE DUPLICATES
# --------------------------------------------------
def remove_duplicates(
    df
):

    df = df.copy()

    df = df.drop_duplicates()

    return df


# --------------------------------------------------
# CONVERT TO DATETIME
# --------------------------------------------------
def convert_to_datetime(
    df,
    column_name
):

    df = df.copy()

    df[column_name] = pd.to_datetime(
        df[column_name],
        errors="coerce"
    )

    return df


# --------------------------------------------------
# CREATE DATE FEATURES
# --------------------------------------------------
def create_date_features(
    df,
    column_name
):

    df = df.copy()

    df["Year"] = (
        df[column_name]
        .dt.year
    )

    df["Month"] = (
        df[column_name]
        .dt.month
    )

    df["Quarter"] = (
        df[column_name]
        .dt.quarter
    )

    df["Day"] = (
        df[column_name]
        .dt.day
    )

    return df


# --------------------------------------------------
# MISSING VALUE SUMMARY
# --------------------------------------------------
def get_missing_summary(
    df
):

    missing_summary = pd.DataFrame(
        {
            "Column": df.columns,

            "Missing Values":
                df.isnull().sum().values
        }
    )

    return missing_summary


# --------------------------------------------------
# CORRELATION MATRIX
# --------------------------------------------------
def get_correlation_matrix(
    df
):

    numerical_df = df.select_dtypes(
        include="number"
    )

    correlation_matrix = (
        numerical_df.corr()
    )

    return correlation_matrix