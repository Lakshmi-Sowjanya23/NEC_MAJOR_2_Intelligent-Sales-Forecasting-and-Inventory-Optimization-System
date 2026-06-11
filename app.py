import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Intelligent Sales Forecasting and Inventory Optimization System",
    page_icon="📈",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title(
    "📈 Intelligent Sales Forecasting and Inventory Optimization System"
)

st.markdown(
    """
Welcome to the **Intelligent Sales Forecasting and Inventory Optimization System**.

This platform combines Machine Learning, Forecasting, Inventory Optimization, and Business Intelligence to improve decision-making and supply chain efficiency.
"""
)

st.divider()

# --------------------------------------------------
# PROJECT MODULES
# --------------------------------------------------
st.subheader(
    "🚀 Project Modules"
)

col1, col2 = st.columns(2)

with col1:

    st.info(
        """
📤 Data Upload

🧹 Data Preprocessing

📊 EDA Analysis

🤖 Model Training
"""
    )

with col2:

    st.info(
        """
📈 Sales Forecasting

📦 Inventory Optimization

📑 Reports

📊 Dashboard
"""
    )

st.divider()

# --------------------------------------------------
# OBJECTIVES
# --------------------------------------------------
st.subheader(
    "🎯 Objectives"
)

st.markdown(
    """
- Predict future sales accurately.
- Optimize inventory levels.
- Improve supply chain efficiency.
- Provide business intelligence dashboards.
- Reduce inventory costs and maximize profitability.
"""
)

st.divider()

# --------------------------------------------------
# TECHNOLOGIES
# --------------------------------------------------
st.subheader(
    "🛠 Technologies Used"
)

st.markdown(
    """
- Python
- Streamlit
- Pandas
- NumPy
- Scikit-Learn
- Plotly
- Joblib
"""
)

st.divider()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.success(
    "✅ System Ready. Use the sidebar to navigate through different modules."
)