import pandas as pd
import plotly.express as px


# --------------------------------------------------
# ACTUAL VS PREDICTED
# --------------------------------------------------
def create_actual_vs_predicted_plot(
    y_test,
    y_pred
):

    df_plot = pd.DataFrame(
        {
            "Actual": y_test,
            "Predicted": y_pred
        }
    )

    fig = px.scatter(
        df_plot,
        x="Actual",
        y="Predicted",
        title="Actual vs Predicted"
    )

    return fig


# --------------------------------------------------
# RESIDUAL PLOT
# --------------------------------------------------
def create_residual_plot(
    y_test,
    y_pred
):

    residuals = y_test - y_pred

    df_plot = pd.DataFrame(
        {
            "Predicted": y_pred,
            "Residuals": residuals
        }
    )

    fig = px.scatter(
        df_plot,
        x="Predicted",
        y="Residuals",
        title="Residual Plot"
    )

    return fig


# --------------------------------------------------
# ERROR DISTRIBUTION
# --------------------------------------------------
def create_error_distribution_plot(
    y_test,
    y_pred
):

    errors = y_test - y_pred

    fig = px.histogram(
        x=errors,
        nbins=30,
        title="Error Distribution"
    )

    return fig


# --------------------------------------------------
# FEATURE IMPORTANCE
# --------------------------------------------------
def create_feature_importance_plot(
    model,
    feature_names
):

    if not hasattr(
        model,
        "feature_importances_"
    ):

        return None

    importance_df = pd.DataFrame(
        {
            "Feature": feature_names,
            "Importance": model.feature_importances_
        }
    )

    importance_df = (
        importance_df
        .sort_values(
            by="Importance",
            ascending=False
        )
    )

    fig = px.bar(
        importance_df,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Feature Importance"
    )

    return fig


# --------------------------------------------------
# MODEL COMPARISON
# --------------------------------------------------
def create_model_comparison_plot(
    comparison_df
):

    fig = px.bar(
        comparison_df,
        x="Model",
        y="R2 Score",
        color="Model",
        title="Model Comparison"
    )

    return fig