import joblib
import pandas as pd


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
def load_model():

    model_data = joblib.load(
        "models/trained_model.pkl"
    )

    model = model_data["model"]

    feature_names = model_data[
        "feature_names"
    ]

    encoders = model_data[
        "encoders"
    ]

    return (
        model,
        feature_names,
        encoders
    )


# --------------------------------------------------
# PREPARE FORECAST INPUT
# --------------------------------------------------
def prepare_forecast_input(
    df,
    feature_names,
    encoders
):

    df = df.copy()

    columns_to_drop = [
        "Sales",
        "Row ID",
        "Order ID",
        "Customer ID",
        "Customer Name",
        "Product ID",
        "Product Name",
        "Order Date",
        "Ship Date"
    ]

    existing_columns = [
        col
        for col in columns_to_drop
        if col in df.columns
    ]

    X = df.drop(
        columns=existing_columns
    )

    categorical_columns = (
        X.select_dtypes(
            include="object"
        ).columns
    )

    for col in categorical_columns:

        if col in encoders:

            encoder = encoders[col]

            X[col] = encoder.transform(
                X[col].astype(str)
            )

    X = X[feature_names]

    return X


# --------------------------------------------------
# GENERATE FORECAST
# --------------------------------------------------
def generate_forecast(
    model,
    X_input,
    forecast_days
):

    predictions = model.predict(
        X_input
    )

    predictions = predictions[
        :forecast_days
    ]

    forecast_df = pd.DataFrame(
        {
            "Day": range(
                1,
                len(predictions) + 1
            ),

            "Predicted Sales":
                predictions
        }
    )

    return forecast_df


# --------------------------------------------------
# FORECAST METRICS
# --------------------------------------------------
def get_forecast_metrics(
    forecast_df
):

    total_sales = (
        forecast_df[
            "Predicted Sales"
        ].sum()
    )

    average_sales = (
        forecast_df[
            "Predicted Sales"
        ].mean()
    )

    max_sales = (
        forecast_df[
            "Predicted Sales"
        ].max()
    )

    min_sales = (
        forecast_df[
            "Predicted Sales"
        ].min()
    )

    return (
        total_sales,
        average_sales,
        max_sales,
        min_sales
    )


# --------------------------------------------------
# SAVE FORECAST RESULTS
# --------------------------------------------------
def save_forecast_results(
    forecast_df
):

    forecast_df.to_csv(
        "outputs/reports/forecast_results.csv",
        index=False
    )