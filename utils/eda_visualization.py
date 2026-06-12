import pandas as pd
import plotly.express as px


# --------------------------------------------------
# MONTHLY SALES TREND
# --------------------------------------------------
def create_monthly_sales_trend(df):

    df = df.copy()

    if "Month" not in df.columns:

        if "Order Date" in df.columns:

            df["Order Date"] = pd.to_datetime(
                df["Order Date"],
                errors="coerce"
            )

            df["Month"] = (
                df["Order Date"]
                .dt.month_name()
            )

    monthly_sales = (
        df.groupby("Month")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        monthly_sales,
        x="Month",
        y="Sales",
        markers=True,
        title="Monthly Sales Trend"
    )

    return fig


# --------------------------------------------------
# MONTHLY PROFIT TREND
# --------------------------------------------------
def create_monthly_profit_trend(df):

    df = df.copy()

    if "Month" not in df.columns:

        if "Order Date" in df.columns:

            df["Order Date"] = pd.to_datetime(
                df["Order Date"],
                errors="coerce"
            )

            df["Month"] = (
                df["Order Date"]
                .dt.month_name()
            )

    monthly_profit = (
        df.groupby("Month")["Profit"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        monthly_profit,
        x="Month",
        y="Profit",
        markers=True,
        title="Monthly Profit Trend"
    )

    return fig


# --------------------------------------------------
# CATEGORY SALES CHART
# --------------------------------------------------
def create_category_sales_chart(df):

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        color="Category",
        title="Category-wise Sales"
    )

    return fig


# --------------------------------------------------
# REGION SALES CHART
# --------------------------------------------------
def create_region_sales_chart(df):

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        region_sales,
        x="Region",
        y="Sales",
        color="Region",
        title="Region-wise Sales"
    )

    return fig


# --------------------------------------------------
# SEGMENT SALES CHART
# --------------------------------------------------
def create_segment_sales_chart(df):

    segment_sales = (
        df.groupby("Segment")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        segment_sales,
        names="Segment",
        values="Sales",
        title="Segment-wise Sales"
    )

    return fig


# --------------------------------------------------
# TOP PRODUCTS CHART
# --------------------------------------------------
def create_top_products_chart(df):

    top_products = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_products,
        x="Sales",
        y="Product Name",
        orientation="h",
        title="Top 10 Products by Sales"
    )

    return fig


# --------------------------------------------------
# SALES DISTRIBUTION
# --------------------------------------------------
def create_sales_distribution(df):

    fig = px.histogram(
        df,
        x="Sales",
        nbins=30,
        title="Sales Distribution"
    )

    return fig


# --------------------------------------------------
# PROFIT DISTRIBUTION
# --------------------------------------------------
def create_profit_distribution(df):

    fig = px.histogram(
        df,
        x="Profit",
        nbins=30,
        title="Profit Distribution"
    )

    return fig


# --------------------------------------------------
# SALES VS PROFIT SCATTER
# --------------------------------------------------
def create_sales_profit_scatter(df):

    fig = px.scatter(
        df,
        x="Sales",
        y="Profit",
        color="Category",
        title="Sales vs Profit"
    )

    return fig