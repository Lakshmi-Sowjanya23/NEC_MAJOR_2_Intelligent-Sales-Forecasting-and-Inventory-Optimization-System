import streamlit as st
import pandas as pd
import plotly.express as px

from utils.inventory_utils import (
    calculate_average_demand,
    calculate_safety_stock,
    calculate_reorder_point,
    calculate_eoq,
    create_inventory_summary,
    save_inventory_report
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Inventory Optimization",
    page_icon="📦",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title(
    "📦 Inventory Optimization"
)

st.divider()

# --------------------------------------------------
# LOAD FORECAST DATA
# --------------------------------------------------
try:

    forecast_df = pd.read_csv(
        "outputs/reports/forecast_results.csv"
    )

except Exception:

    st.error(
        "Forecast results not found. Generate forecasts first."
    )

    st.stop()

# --------------------------------------------------
# INPUTS
# --------------------------------------------------
safety_stock_percent = st.slider(
    "Safety Stock (%)",
    5,
    50,
    20
)

lead_time = st.slider(
    "Lead Time (Days)",
    1,
    30,
    7
)

holding_cost = st.number_input(
    "Holding Cost Per Unit",
    min_value=1.0,
    value=10.0
)

ordering_cost = st.number_input(
    "Ordering Cost",
    min_value=1.0,
    value=100.0
)

# --------------------------------------------------
# CALCULATIONS
# --------------------------------------------------
average_demand = calculate_average_demand(
    forecast_df
)

safety_stock = calculate_safety_stock(
    average_demand,
    safety_stock_percent
)

reorder_point = calculate_reorder_point(
    average_demand,
    lead_time,
    safety_stock
)

annual_demand = average_demand * 365

eoq = calculate_eoq(
    annual_demand,
    ordering_cost,
    holding_cost
)

summary_df = create_inventory_summary(
    average_demand,
    safety_stock,
    reorder_point,
    eoq
)

# --------------------------------------------------
# METRICS
# --------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Average Demand",
        round(
            average_demand,
            2
        )
    )

with col2:

    st.metric(
        "Safety Stock",
        round(
            safety_stock,
            2
        )
    )

with col3:

    st.metric(
        "Reorder Point",
        round(
            reorder_point,
            2
        )
    )

with col4:

    st.metric(
        "EOQ",
        round(
            eoq,
            2
        )
    )

st.divider()

# --------------------------------------------------
# INVENTORY SUMMARY TABLE
# --------------------------------------------------
st.subheader(
    "Inventory Summary"
)

st.dataframe(
    summary_df,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# INVENTORY LEVELS
# --------------------------------------------------
fig1 = px.bar(
    summary_df,
    x="Metric",
    y="Value",
    title="Inventory Levels"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# --------------------------------------------------
# DEMAND VS SAFETY STOCK
# --------------------------------------------------
fig2 = px.bar(
    x=[
        "Average Demand",
        "Safety Stock"
    ],
    y=[
        average_demand,
        safety_stock
    ],
    title="Demand vs Safety Stock"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# --------------------------------------------------
# EOQ DISTRIBUTION
# --------------------------------------------------
fig3 = px.pie(
    names=[
        "EOQ",
        "Reorder Point"
    ],
    values=[
        eoq,
        reorder_point
    ],
    title="EOQ Distribution"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# --------------------------------------------------
# INVENTORY COMPONENTS
# --------------------------------------------------
fig4 = px.pie(
    summary_df,
    names="Metric",
    values="Value",
    hole=0.5,
    title="Inventory Components"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# SAVE REPORT
# --------------------------------------------------
save_inventory_report(
    summary_df
)

csv_data = summary_df.to_csv(
    index=False
).encode(
    "utf-8"
)

st.download_button(
    "📥 Download Inventory Report",
    data=csv_data,
    file_name="inventory_report.csv",
    mime="text/csv"
)