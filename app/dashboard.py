import streamlit as st
import psycopg2
from psycopg2 import pool
import pandas as pd
import os
from dotenv import load_dotenv
import warnings
import plotly.express as px

warnings.filterwarnings('ignore', category=UserWarning)
load_dotenv()

# --- 1. SETUP & CONNECTION POOLING ---
st.set_page_config(page_title="Global Orders BI", layout="wide")

@st.cache_resource
def init_connection_pool():
    return psycopg2.pool.SimpleConnectionPool(1, 20, dsn=os.getenv("DATABASE_URL"))

conn_pool = init_connection_pool()

@st.cache_data
def fetch_data(query):
    conn = conn_pool.getconn()
    try:
        df = pd.read_sql_query(query, conn)
    finally:
        conn_pool.putconn(conn)
    return df

# --- 2. FETCHING THE DATA ---
# We fetch the top products query you wrote in Phase 2
top_products_query = """
    SELECT 
        dp.categoryname,
        dp.productname,
        SUM(fs.totalamount) as total_sales
    FROM analytics_ci.fact_sales fs
    INNER JOIN analytics_ci.dim_products dp ON fs.productid = dp.productid
    GROUP BY 1, 2
"""
df_sales = fetch_data(top_products_query)

# --- 3. THE DASHBOARD UI ---
st.title("📊 Global Online Orders Dashboard")
st.markdown("---")

# THE WIDGET (Rubric Requirement)
st.sidebar.header("Dashboard Filters")
categories = ["All"] + df_sales['categoryname'].unique().tolist()
selected_category = st.sidebar.selectbox("Select a Product Category", categories)

# Filter the dataframe based on the widget
if selected_category != "All":
    df_filtered = df_sales[df_sales['categoryname'] == selected_category]
else:
    df_filtered = df_sales

# Layout with columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top Products by Revenue")
    # VISUALIZATION 1 (Rubric Requirement)
    fig_bar = px.bar(
        df_filtered.sort_values('total_sales', ascending=False).head(10), 
        x='productname', 
        y='total_sales',
        color='categoryname',
        title="Top 10 Products"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    st.subheader("Revenue Distribution")
    # VISUALIZATION 2 (Rubric Requirement)
    # We aggregate by category for the pie chart
    df_pie = df_filtered.groupby('categoryname')['total_sales'].sum().reset_index()
    fig_pie = px.pie(
        df_pie, 
        names='categoryname', 
        values='total_sales',
        title="Sales by Category"
    )
    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")
st.dataframe(df_filtered, use_container_width=True)