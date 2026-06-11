import streamlit as st
import pandas as pd

from utils.data_loader import load_processed_data

from utils.model_utils import (
    prepare_data,
    train_linear_regression,
    train_random_forest,
    train_decision_tree,
    evaluate_model,
    save_model
)

from utils.model_visualization import (
    create_actual_vs_predicted_plot,
    create_residual_plot,
    create_error_distribution_plot,
    create_feature_importance_plot,
    create_model_comparison_plot
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Model Training",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("🤖 Model Training")

st.divider()

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
df = load_processed_data()

if df is None:
    st.error("Processed dataset not found.")
    st.stop()

# --------------------------------------------------
# MODEL SELECTION
# --------------------------------------------------
selected_model = st.selectbox(
    "Select Model",
    [
        "Linear Regression",
        "Random Forest",
        "Decision Tree"
    ]
)

# --------------------------------------------------
# TRAIN MODEL
# --------------------------------------------------
if st.button("🚀 Train Model"):

    (
        X_train,
        X_test,
        y_train,
        y_test,
        feature_names,
        encoders
    ) = prepare_data(df)

    # ------------------------------------------
    # MODEL TRAINING
    # ------------------------------------------
    if selected_model == "Linear Regression":

        model = train_linear_regression(
            X_train,
            y_train
        )

    elif selected_model == "Random Forest":

        model = train_random_forest(
            X_train,
            y_train
        )

    else:

        model = train_decision_tree(
            X_train,
            y_train
        )

    # ------------------------------------------
    # EVALUATION
    # ------------------------------------------
    (
        y_pred,
        mae,
        mse,
        rmse,
        r2
    ) = evaluate_model(
        model,
        X_test,
        y_test
    )

    # ------------------------------------------
    # SAVE MODEL
    # ------------------------------------------
    save_model(
        model,
        feature_names,
        encoders
    )

    st.success(
        "Model trained and saved successfully."
    )

    # ------------------------------------------
    # METRICS
    # ------------------------------------------
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("MAE", round(mae, 2))

    with col2:
        st.metric("MSE", round(mse, 2))

    with col3:
        st.metric("RMSE", round(rmse, 2))

    with col4:
        st.metric("R² Score", round(r2, 4))

    st.divider()

    # ------------------------------------------
    # ACTUAL VS PREDICTED
    # ------------------------------------------
    col1, col2 = st.columns(2)

    with col1:

        fig1 = create_actual_vs_predicted_plot(
            y_test,
            y_pred
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    with col2:

        fig2 = create_residual_plot(
            y_test,
            y_pred
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # ------------------------------------------
    # ERROR DISTRIBUTION + FEATURE IMPORTANCE
    # ------------------------------------------
    col1, col2 = st.columns(2)

    with col1:

        fig3 = create_error_distribution_plot(
            y_test,
            y_pred
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    with col2:

        fig4 = create_feature_importance_plot(
            model,
            feature_names
        )

        if fig4 is not None:

            st.plotly_chart(
                fig4,
                use_container_width=True
            )

    st.divider()

    # ------------------------------------------
    # MODEL COMPARISON
    # ------------------------------------------
    comparison_df = pd.DataFrame(
        {
            "Model": [selected_model],
            "R2 Score": [r2]
        }
    )

    fig5 = create_model_comparison_plot(
        comparison_df
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )