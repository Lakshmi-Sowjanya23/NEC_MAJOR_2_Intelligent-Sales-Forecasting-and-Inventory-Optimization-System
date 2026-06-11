import joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# --------------------------------------------------
# PREPARE DATA
# --------------------------------------------------
def prepare_data(df):

    df = df.copy()

    target_column = "Sales"

    columns_to_drop = [
        "Sales",
        "Row ID",
        "Order ID",
        "Customer ID",
        "Customer Name",
        "Product ID",
        "Product Name",
        "Order Date",
        "Ship Date"
    ]

    existing_columns = [
        col
        for col in columns_to_drop
        if col in df.columns
    ]

    X = df.drop(
        columns=existing_columns
    )

    y = df[target_column]

    encoders = {}

    categorical_columns = (
        X.select_dtypes(
            include="object"
        ).columns
    )

    for col in categorical_columns:

        encoder = LabelEncoder()

        X[col] = encoder.fit_transform(
            X[col].astype(str)
        )

        encoders[col] = encoder

    feature_names = X.columns.tolist()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    return (
        X_train,
        X_test,
        y_train,
        y_test,
        feature_names,
        encoders
    )


# --------------------------------------------------
# LINEAR REGRESSION
# --------------------------------------------------
def train_linear_regression(
    X_train,
    y_train
):

    model = LinearRegression()

    model.fit(
        X_train,
        y_train
    )

    return model


# --------------------------------------------------
# RANDOM FOREST
# --------------------------------------------------
def train_random_forest(
    X_train,
    y_train
):

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    return model


# --------------------------------------------------
# DECISION TREE
# --------------------------------------------------
def train_decision_tree(
    X_train,
    y_train
):

    model = DecisionTreeRegressor(
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    return model


# --------------------------------------------------
# EVALUATE MODEL
# --------------------------------------------------
def evaluate_model(
    model,
    X_test,
    y_test
):

    y_pred = model.predict(
        X_test
    )

    mae = mean_absolute_error(
        y_test,
        y_pred
    )

    mse = mean_squared_error(
        y_test,
        y_pred
    )

    rmse = np.sqrt(
        mse
    )

    r2 = r2_score(
        y_test,
        y_pred
    )

    return (
        y_pred,
        mae,
        mse,
        rmse,
        r2
    )


# --------------------------------------------------
# SAVE MODEL
# --------------------------------------------------
def save_model(
    model,
    feature_names,
    encoders
):

    model_data = {

        "model": model,

        "feature_names": feature_names,

        "encoders": encoders

    }

    joblib.dump(
        model_data,
        "models/trained_model.pkl"
    )


# --------------------------------------------------
# LOAD SAVED MODEL
# --------------------------------------------------
def load_saved_model():

    model_data = joblib.load(
        "models/trained_model.pkl"
    )

    return model_data