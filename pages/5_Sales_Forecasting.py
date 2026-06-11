import streamlit as st
import plotly.express as px

from utils.data_loader import (
    load_processed_data
)

from utils.forecast_utils import (
    load_model,
    prepare_forecast_input,
    generate_forecast,
    get_forecast_metrics,
    save_forecast_results
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Sales Forecasting",
    page_icon="📈",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title(
    "📈 Sales Forecasting"
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
# LOAD MODEL
# --------------------------------------------------
try:

    model, feature_names, encoders = load_model()

except Exception:

    st.error(
        "Model not found. Train and save a model first."
    )

    st.stop()

# --------------------------------------------------
# INPUTS
# --------------------------------------------------
forecast_days = st.slider(
    "Forecast Days",
    7,
    90,
    30
)

selected_region = st.selectbox(
    "Region",
    sorted(
        df["Region"].unique()
    )
)

selected_category = st.selectbox(
    "Category",
    sorted(
        df["Category"].unique()
    )
)

selected_segment = st.selectbox(
    "Segment",
    sorted(
        df["Segment"].unique()
    )
)

# --------------------------------------------------
# FILTER DATA
# --------------------------------------------------
filtered_df = df[
    (df["Region"] == selected_region)
    &
    (df["Category"] == selected_category)
    &
    (df["Segment"] == selected_segment)
]

# --------------------------------------------------
# GENERATE FORECAST
# --------------------------------------------------
if st.button(
    "🚀 Generate Forecast"
):

    if filtered_df.empty:

        st.warning(
            "No data available for selected filters."
        )

    else:

        X_input = prepare_forecast_input(
            filtered_df,
            feature_names,
            encoders
        )

        forecast_df = generate_forecast(
            model,
            X_input,
            forecast_days
        )

        (
            total_sales,
            average_sales,
            max_sales,
            min_sales
        ) = get_forecast_metrics(
            forecast_df
        )

        # ------------------------------------------
        # METRICS
        # ------------------------------------------
        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Predicted Sales",
                round(
                    total_sales,
                    2
                )
            )

        with col2:

            st.metric(
                "Average Daily Sales",
                round(
                    average_sales,
                    2
                )
            )

        with col3:

            st.metric(
                "Maximum Forecast",
                round(
                    max_sales,
                    2
                )
            )

        with col4:

            st.metric(
                "Minimum Forecast",
                round(
                    min_sales,
                    2
                )
            )

        st.divider()

        # ------------------------------------------
        # TABLE
        # ------------------------------------------
        st.subheader(
            "Forecast Results"
        )

        st.dataframe(
            forecast_df,
            use_container_width=True
        )

        st.divider()

        # ------------------------------------------
        # FORECAST TREND
        # ------------------------------------------
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

        # ------------------------------------------
        # DISTRIBUTION
        # ------------------------------------------
        fig2 = px.histogram(
            forecast_df,
            x="Predicted Sales",
            nbins=20,
            title="Forecast Distribution"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

        st.divider()

        # ------------------------------------------
        # SAVE RESULTS
        # ------------------------------------------
        save_forecast_results(
            forecast_df
        )

        csv_data = forecast_df.to_csv(
            index=False
        ).encode(
            "utf-8"
        )

        st.download_button(
            "📥 Download Forecast CSV",
            data=csv_data,
            file_name="forecast_results.csv",
            mime="text/csv"
        )