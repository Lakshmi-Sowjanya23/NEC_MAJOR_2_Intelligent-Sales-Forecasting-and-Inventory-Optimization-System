import streamlit as st

from utils.data_loader import (
    load_processed_data
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
    page_title="EDA Analysis",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title(
    "📊 Exploratory Data Analysis"
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

    fig1 = create_monthly_sales_trend(
        df
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with col2:

    fig2 = create_monthly_profit_trend(
        df
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# --------------------------------------------------
# CATEGORY & REGION
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    fig3 = create_category_sales_chart(
        df
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

with col2:

    fig4 = create_region_sales_chart(
        df
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# --------------------------------------------------
# SEGMENT & TOP PRODUCTS
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    fig5 = create_segment_sales_chart(
        df
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

with col2:

    fig6 = create_top_products_chart(
        df
    )

    st.plotly_chart(
        fig6,
        use_container_width=True
    )

# --------------------------------------------------
# DISTRIBUTIONS
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    fig7 = create_sales_distribution(
        df
    )

    st.plotly_chart(
        fig7,
        use_container_width=True
    )

with col2:

    fig8 = create_profit_distribution(
        df
    )

    st.plotly_chart(
        fig8,
        use_container_width=True
    )

# --------------------------------------------------
# SCATTER PLOT
# --------------------------------------------------
fig9 = create_sales_profit_scatter(
    df
)

st.plotly_chart(
    fig9,
    use_container_width=True
)

# --------------------------------------------------
# HEATMAP
# --------------------------------------------------
correlation_matrix = (
    get_correlation_matrix(
        df
    )
)

fig10 = create_correlation_heatmap(
    correlation_matrix
)

st.plotly_chart(
    fig10,
    use_container_width=True
)

st.divider()

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