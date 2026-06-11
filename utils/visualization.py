import plotly.express as px


# --------------------------------------------------
# MISSING VALUE CHART
# --------------------------------------------------
def create_missing_chart(
    missing_summary,
    title
):

    fig = px.bar(
        missing_summary,
        x="Column",
        y="Missing Values",
        title=title
    )

    return fig


# --------------------------------------------------
# DUPLICATE CHART
# --------------------------------------------------
def create_duplicate_chart(
    rows_before,
    rows_after
):

    removed_rows = rows_before - rows_after

    fig = px.pie(
        names=[
            "Remaining Rows",
            "Removed Rows"
        ],

        values=[
            rows_after,
            removed_rows
        ],

        title="Duplicate Analysis"
    )

    return fig


# --------------------------------------------------
# DATA TYPE CHART
# --------------------------------------------------
def create_dtype_chart(
    df
):

    numerical_columns = len(
        df.select_dtypes(
            include="number"
        ).columns
    )

    categorical_columns = len(
        df.select_dtypes(
            exclude="number"
        ).columns
    )

    fig = px.pie(
        names=[
            "Numerical Columns",
            "Categorical Columns"
        ],

        values=[
            numerical_columns,
            categorical_columns
        ],

        title="Data Type Distribution"
    )

    return fig


# --------------------------------------------------
# CORRELATION HEATMAP
# --------------------------------------------------
def create_correlation_heatmap(
    correlation_matrix
):

    fig = px.imshow(
        correlation_matrix,
        text_auto=True,
        aspect="auto",
        title="Correlation Heatmap"
    )

    return fig