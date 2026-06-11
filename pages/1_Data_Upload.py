import streamlit as st
import pandas as pd

from utils.data_loader import (
    load_sample_data,
    save_uploaded_data
)

from utils.preprocessing import (
    get_missing_summary
)

from utils.visualization import (
    create_missing_chart
)


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Data Upload",
    page_icon="📤",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title(
    "📤 Data Upload"
)

st.divider()

# --------------------------------------------------
# DATA SOURCE
# --------------------------------------------------
dataset_source = st.radio(
    "Select Dataset Source",
    [
        "Sample Dataset",
        "Upload Dataset"
    ]
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
df = None

if dataset_source == "Sample Dataset":

    df = load_sample_data()

else:

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(
            uploaded_file,
            encoding="latin1"
        )

# --------------------------------------------------
# DISPLAY DATA
# --------------------------------------------------
if df is not None:

    # ----------------------------------------------
    # METRICS
    # ----------------------------------------------
    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Rows",
            df.shape[0]
        )

    with col2:

        st.metric(
            "Columns",
            df.shape[1]
        )

    with col3:

        st.metric(
            "Numerical Columns",
            len(
                df.select_dtypes(
                    include="number"
                ).columns
            )
        )

    with col4:

        st.metric(
            "Categorical Columns",
            len(
                df.select_dtypes(
                    exclude="number"
                ).columns
            )
        )

    st.divider()

    # ----------------------------------------------
    # PREVIEW
    # ----------------------------------------------
    st.subheader(
        "Dataset Preview"
    )

    st.dataframe(
        df.head(10),
        use_container_width=True
    )

    st.divider()

    # ----------------------------------------------
    # MISSING SUMMARY
    # ----------------------------------------------
    st.subheader(
        "Missing Value Summary"
    )

    missing_summary = get_missing_summary(
        df
    )

    st.dataframe(
        missing_summary,
        use_container_width=True
    )

    st.divider()

    # ----------------------------------------------
    # CHART
    # ----------------------------------------------
    fig = create_missing_chart(
        missing_summary,
        "Missing Values"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ----------------------------------------------
    # SAVE
    # ----------------------------------------------
    if dataset_source == "Upload Dataset":

        if st.button(
            "💾 Save Uploaded Dataset"
        ):

            success = save_uploaded_data(
                df
            )

            if success:

                st.success(
                    "Dataset saved successfully."
                )

            else:

                st.error(
                    "Unable to save dataset."
                )

