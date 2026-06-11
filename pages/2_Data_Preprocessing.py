import streamlit as st
import pandas as pd

from utils.data_loader import (
    load_active_data,
    save_processed_data
)

from utils.preprocessing import (
    handle_missing_values,
    remove_duplicates,
    convert_to_datetime,
    create_date_features,
    get_missing_summary,
    get_correlation_matrix
)

from utils.visualization import (
    create_missing_chart,
    create_duplicate_chart,
    create_dtype_chart,
    create_correlation_heatmap
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Data Preprocessing",
    page_icon="🧹",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("🧹 Data Preprocessing")

st.divider()

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
df_original = load_active_data()

if df_original is None:

    st.error(
        "Processed dataset not found."
    )

    st.stop()

df_processed = df_original.copy()

# --------------------------------------------------
# OPTIONS
# --------------------------------------------------
missing_method = st.selectbox(
    "Missing Value Method",
    [
        "Drop Missing Values",
        "Fill Numerical Values with Mean",
        "Fill Numerical Values with Median",
        "Fill Numerical Values with Zero"
    ]
)

remove_duplicate_rows = st.checkbox(
    "Remove Duplicate Rows",
    value=True
)

# --------------------------------------------------
# DATE COLUMN
# --------------------------------------------------
date_columns = [
    col
    for col in df_processed.columns
    if "date" in col.lower()
]

selected_date_column = st.selectbox(
    "Select Date Column",
    date_columns
)

# --------------------------------------------------
# FEATURE ENGINEERING
# --------------------------------------------------
extract_year = st.checkbox(
    "Year",
    value=True
)

extract_month = st.checkbox(
    "Month",
    value=True
)

extract_quarter = st.checkbox(
    "Quarter",
    value=True
)

extract_day = st.checkbox(
    "Day",
    value=True
)

# --------------------------------------------------
# PROCESS
# --------------------------------------------------
df_processed = handle_missing_values(
    df_processed,
    missing_method
)

if remove_duplicate_rows:

    df_processed = remove_duplicates(
        df_processed
    )

df_processed = convert_to_datetime(
    df_processed,
    selected_date_column
)

df_processed = create_date_features(
    df_processed,
    selected_date_column
)

# --------------------------------------------------
# METRICS
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Rows Before",
        df_original.shape[0]
    )

    st.metric(
        "Columns Before",
        df_original.shape[1]
    )

with col2:

    st.metric(
        "Rows After",
        df_processed.shape[0]
    )

    st.metric(
        "Columns After",
        df_processed.shape[1]
    )

st.divider()

# --------------------------------------------------
# DATA PREVIEW
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    st.subheader(
        "Original Dataset"
    )

    st.dataframe(
        df_original.head(),
        use_container_width=True
    )

with col2:

    st.subheader(
        "Processed Dataset"
    )

    st.dataframe(
        df_processed.head(),
        use_container_width=True
    )

st.divider()

# --------------------------------------------------
# MISSING SUMMARY
# --------------------------------------------------
missing_summary = get_missing_summary(
    df_processed
)

st.subheader(
    "Missing Value Summary"
)

st.dataframe(
    missing_summary,
    use_container_width=True
)

# --------------------------------------------------
# DATATYPE TABLE
# --------------------------------------------------
dtype_df = pd.DataFrame(
    {
        "Column Name":
            df_processed.columns,

        "Data Type":
            df_processed.dtypes.astype(str)
    }
)

st.subheader(
    "Data Types"
)

st.dataframe(
    dtype_df,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# CHARTS
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    fig1 = create_missing_chart(
        get_missing_summary(df_original),
        "Missing Values Before"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with col2:

    fig2 = create_missing_chart(
        get_missing_summary(df_processed),
        "Missing Values After"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

col1, col2 = st.columns(2)

with col1:

    fig3 = create_duplicate_chart(
        df_original.shape[0],
        df_processed.shape[0]
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

with col2:

    fig4 = create_dtype_chart(
        df_processed
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

st.divider()

# --------------------------------------------------
# HEATMAP
# --------------------------------------------------
correlation_matrix = get_correlation_matrix(
    df_processed
)

fig5 = create_correlation_heatmap(
    correlation_matrix
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# SAVE
# --------------------------------------------------
if st.button(
    "💾 Save Processed Dataset"
):

    success = save_processed_data(
        df_processed
    )

    if success:

        st.success(
            "Processed dataset saved successfully."
        )

    else:

        st.error(
            "Unable to save processed dataset."
        )