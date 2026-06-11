import streamlit as st
import plotly.express as px

from utils.data_loader import (
    load_processed_data
)

from utils.report_utils import (
    load_forecast_report,
    load_inventory_report,
    get_dataset_summary
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Reports",
    page_icon="📑",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title(
    "📑 Reports"
)

st.divider()

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
df = load_processed_data()

if df is None:

    st.error(
        "Processed dataset not found."
    )

    st.stop()

forecast_df = load_forecast_report()

inventory_df = load_inventory_report()

# --------------------------------------------------
# DATASET SUMMARY
# --------------------------------------------------
summary = get_dataset_summary(
    df
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Rows",
        summary["Rows"]
    )

with col2:

    st.metric(
        "Columns",
        summary["Columns"]
    )

with col3:

    st.metric(
        "Numerical Columns",
        summary["Numerical Columns"]
    )

with col4:

    st.metric(
        "Categorical Columns",
        summary["Categorical Columns"]
    )

st.divider()

# --------------------------------------------------
# BUSINESS METRICS
# --------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Total Sales",
        round(
            df["Sales"].sum(),
            2
        )
    )

with col2:

    st.metric(
        "Total Profit",
        round(
            df["Profit"].sum(),
            2
        )
    )

with col3:

    st.metric(
        "Total Quantity",
        int(
            df["Quantity"].sum()
        )
    )

with col4:

    st.metric(
        "Total Orders",
        df.shape[0]
    )

st.divider()

# --------------------------------------------------
# FORECAST REPORT
# --------------------------------------------------
if forecast_df is not None:

    st.subheader(
        "Forecast Report"
    )

    st.dataframe(
        forecast_df,
        use_container_width=True
    )

    fig1 = px.line(
        forecast_df,
        x="Day",
        y="Predicted Sales",
        markers=True,
        title="Forecast Trend"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

st.divider()

# --------------------------------------------------
# INVENTORY REPORT
# --------------------------------------------------
if inventory_df is not None:

    st.subheader(
        "Inventory Report"
    )

    st.dataframe(
        inventory_df,
        use_container_width=True
    )

    fig2 = px.bar(
        inventory_df,
        x="Metric",
        y="Value",
        title="Inventory Metrics"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.divider()

# --------------------------------------------------
# SALES DISTRIBUTION
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    fig3 = px.histogram(
        df,
        x="Sales",
        nbins=30,
        title="Sales Distribution"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

with col2:

    fig4 = px.histogram(
        df,
        x="Profit",
        nbins=30,
        title="Profit Distribution"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

st.divider()

# --------------------------------------------------
# DOWNLOADS
# --------------------------------------------------
st.subheader(
    "Download Reports"
)

if forecast_df is not None:

    forecast_csv = (
        forecast_df.to_csv(
            index=False
        )
        .encode(
            "utf-8"
        )
    )

    st.download_button(
        "Download Forecast Report",
        forecast_csv,
        "forecast_results.csv",
        "text/csv"
    )

if inventory_df is not None:

    inventory_csv = (
        inventory_df.to_csv(
            index=False
        )
        .encode(
            "utf-8"
        )
    )

    st.download_button(
        "Download Inventory Report",
        inventory_csv,
        "inventory_report.csv",
        "text/csv"
    )

processed_csv = (
    df.to_csv(
        index=False
    )
    .encode(
        "utf-8"
    )
)

st.download_button(
    "Download Processed Dataset",
    processed_csv,
    "processed_sales.csv",
    "text/csv"
)