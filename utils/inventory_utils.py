import pandas as pd


# --------------------------------------------------
# AVERAGE DEMAND
# --------------------------------------------------
def calculate_average_demand(
    forecast_df
):

    average_demand = (
        forecast_df[
            "Predicted Sales"
        ].mean()
    )

    return average_demand


# --------------------------------------------------
# SAFETY STOCK
# --------------------------------------------------
def calculate_safety_stock(
    average_demand,
    safety_stock_percent
):

    safety_stock = (
        average_demand
        * safety_stock_percent
        / 100
    )

    return safety_stock


# --------------------------------------------------
# REORDER POINT
# --------------------------------------------------
def calculate_reorder_point(
    average_demand,
    lead_time,
    safety_stock
):

    reorder_point = (
        average_demand
        * lead_time
        + safety_stock
    )

    return reorder_point


# --------------------------------------------------
# EOQ
# --------------------------------------------------
def calculate_eoq(
    annual_demand,
    ordering_cost,
    holding_cost
):

    eoq = (
        (
            2
            * annual_demand
            * ordering_cost
        )
        /
        holding_cost
    ) ** 0.5

    return eoq


# --------------------------------------------------
# INVENTORY SUMMARY
# --------------------------------------------------
def create_inventory_summary(
    average_demand,
    safety_stock,
    reorder_point,
    eoq
):

    maximum_inventory = (
        reorder_point
        + eoq
    )

    minimum_inventory = (
        reorder_point
        - safety_stock
    )

    summary_df = pd.DataFrame(
        {
            "Metric": [
                "Average Demand",
                "Safety Stock",
                "Reorder Point",
                "EOQ",
                "Maximum Inventory",
                "Minimum Inventory"
            ],

            "Value": [
                average_demand,
                safety_stock,
                reorder_point,
                eoq,
                maximum_inventory,
                minimum_inventory
            ]
        }
    )

    return summary_df


# --------------------------------------------------
# SAVE INVENTORY REPORT
# --------------------------------------------------
def save_inventory_report(
    summary_df
):

    summary_df.to_csv(
        "outputs/reports/inventory_report.csv",
        index=False
    )