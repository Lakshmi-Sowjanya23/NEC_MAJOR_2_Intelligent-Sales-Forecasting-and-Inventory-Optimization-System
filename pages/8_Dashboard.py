import streamlit as st

from utils.data_loader import (
    load_processed_data
)

from utils.report_utils import (
    load_forecast_report,
    load_inventory_report,
    get_dataset_summary
)

from utils.eda_visualization import (
    create_monthly_sales_trend,
    create_monthly_profit_trend,
    create_category_sales_chart,
    create_region_sales_chart,
    create_segment_sales_chart,
    create_top_products_chart,
    create_sales_distribution,
    create_profit_distribution,
    create_sales_profit_scatter
)

from utils.preprocessing import (
    get_correlation_matrix
)

from utils.visualization import (
    create_correlation_heatmap
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title(
    "📊 Dashboard"
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

summary = get_dataset_summary(
    df
)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.header(
    "Dataset Statistics"
)

st.sidebar.metric(
    "Rows",
    summary["Rows"]
)

st.sidebar.metric(
    "Columns",
    summary["Columns"]
)

st.sidebar.metric(
    "Numerical Columns",
    summary["Numerical Columns"]
)

st.sidebar.metric(
    "Categorical Columns",
    summary["Categorical Columns"]
)

# --------------------------------------------------
# KPI CARDS
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
# MONTHLY TRENDS
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        create_monthly_sales_trend(
            df
        ),
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        create_monthly_profit_trend(
            df
        ),
        use_container_width=True
    )

# --------------------------------------------------
# CATEGORY & REGION
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        create_category_sales_chart(
            df
        ),
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        create_region_sales_chart(
            df
        ),
        use_container_width=True
    )

# --------------------------------------------------
# SEGMENT & TOP PRODUCTS
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        create_segment_sales_chart(
            df
        ),
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        create_top_products_chart(
            df
        ),
        use_container_width=True
    )

# --------------------------------------------------
# DISTRIBUTIONS
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        create_sales_distribution(
            df
        ),
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        create_profit_distribution(
            df
        ),
        use_container_width=True
    )

# --------------------------------------------------
# SALES VS PROFIT
# --------------------------------------------------
st.plotly_chart(
    create_sales_profit_scatter(
        df
    ),
    use_container_width=True
)

# --------------------------------------------------
# HEATMAP
# --------------------------------------------------
correlation_matrix = get_correlation_matrix(
    df
)

st.plotly_chart(
    create_correlation_heatmap(
        correlation_matrix
    ),
    use_container_width=True
)

# --------------------------------------------------
# FORECAST TREND
# --------------------------------------------------
if forecast_df is not None:

    st.subheader(
        "Forecast Trend"
    )

    st.line_chart(
        forecast_df.set_index(
            "Day"
        )
    )

# --------------------------------------------------
# INVENTORY REPORT
# --------------------------------------------------
if inventory_df is not None:

    st.subheader(
        "Inventory Metrics"
    )

    st.dataframe(
        inventory_df,
        use_container_width=True
    )

# --------------------------------------------------
# DATASET PREVIEW
# --------------------------------------------------
st.subheader(
    "Dataset Preview"
)

st.dataframe(
    df.head(10),
    use_container_width=True
)

# --------------------------------------------------
# STATISTICAL SUMMARY
# --------------------------------------------------
st.subheader(
    "Statistical Summary"
)

st.dataframe(
    df.describe(),
    use_container_width=True
)