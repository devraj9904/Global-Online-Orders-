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

#1. SETUP & CONNECTION POOLING
st.set_page_config(page_title="Global Orders BI", page_icon="📦", layout="wide")

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

# 2. FETCHING THE DATA 
query = """
    SELECT 
        dp.categoryname,
        dp.productname,
        SUM(fs.totalamount) as total_sales
    FROM analytics_ci.fact_sales fs
    INNER JOIN analytics_ci.dim_products dp ON fs.productid = dp.productid
    GROUP BY 1, 2
"""
df_sales = fetch_data(query)

# 3. DASHBOARD UI
st.title("📦 Global Online Orders Dashboard")
st.markdown("Track and analyze our top-performing products and revenue distribution globally.")
st.markdown("---")

# CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@400;600;700&display=swap');

    /* ── Root & body ── */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #fdfdfc !important;
    }

    [data-testid="stApp"] {
        background-color: #fdfdfc;
        font-family: 'Syne', sans-serif;
        color: #1e293b;
    }

    /* ── Main content padding ── */
    .main .block-container {
        padding: 2.5rem 3rem 4rem;
        max-width: 1400px;
    }

    /* ── Page title ── */
    h1 {
        font-family: 'Syne', sans-serif !important;
        font-weight: 700 !important;
        font-size: 1.75rem !important;
        letter-spacing: -0.02em !important;
        color: #0f172a !important;
        margin-bottom: 0.25rem !important;
    }

    /* ── Subtitle / description text ── */
    [data-testid="stMarkdownContainer"] p {
        font-family: 'Syne', sans-serif;
        font-size: 0.875rem;
        color: #475569;
        letter-spacing: 0.01em;
    }

    /* ── Horizontal rule ── */
    hr {
        border: none !important;
        border-top: 1px solid #e2e8f0 !important;
        margin: 1.25rem 0 2rem !important;
    }

    /* ── Section subheaders ── */
    h2, h3 {
        font-family: 'Syne', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.8rem !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
        color: #334155 !important;
        margin-bottom: 1rem !important;
    }

    /* ── KPI metric cards ── */
    [data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-top: 3px solid #0ea5e9;
        padding: 1.4rem 1.5rem 1.2rem;
        border-radius: 6px;
        position: relative;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    [data-testid="stMetric"]:hover {
        border-color: #cbd5e1;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }

    /* KPI label */
    [data-testid="stMetricLabel"] {
        font-family: 'Syne', sans-serif !important;
        font-size: 0.7rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.12em !important;
        text-transform: uppercase !important;
        color: #64748b !important;
    }

    /* KPI value */
    [data-testid="stMetricValue"] {
        font-family: 'DM Mono', monospace !important;
        font-size: 1.65rem !important;
        font-weight: 500 !important;
        color: #0f172a !important;
        letter-spacing: -0.02em !important;
        margin-top: 0.3rem !important;
    }

    /* KPI delta */
    [data-testid="stMetricDelta"] {
        font-family: 'DM Mono', monospace !important;
        font-size: 0.75rem !important;
    }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background-color: #f8fafc !important;
        border-right: 1px solid #e2e8f0 !important;
    }

    [data-testid="stSidebar"] .block-container {
        padding: 2rem 1.25rem;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        font-family: 'Syne', sans-serif !important;
        font-size: 0.7rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.12em !important;
        text-transform: uppercase !important;
        color: #334155 !important;
        margin-bottom: 1.25rem !important;
    }

    /* Sidebar selectbox */
    [data-testid="stSidebar"] [data-testid="stSelectbox"] > div > div {
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 4px !important;
        color: #1e293b !important;
        font-family: 'Syne', sans-serif !important;
        font-size: 0.85rem !important;
        transition: border-color 0.15s ease;
    }

    [data-testid="stSidebar"] [data-testid="stSelectbox"] > div > div:focus-within {
        border-color: #0ea5e9 !important;
        box-shadow: 0 0 0 2px rgba(14, 165, 233, 0.1) !important;
    }

    /* ── Plotly chart containers ── */
    [data-testid="stPlotlyChart"] {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 1rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
    }

    /* ── Dataframe ── */
    [data-testid="stDataFrame"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 6px !important;
        font-family: 'DM Mono', monospace !important;
        font-size: 0.8rem !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
    }

    /* Dataframe header row */
    [data-testid="stDataFrame"] th {
        background-color: #f8fafc !important;
        color: #475569 !important;
        font-family: 'Syne', sans-serif !important;
        font-size: 0.68rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
        border-bottom: 1px solid #e2e8f0 !important;
        padding: 0.65rem 1rem !important;
    }

    /* Dataframe cells */
    [data-testid="stDataFrame"] td {
        color: #334155 !important;
        border-bottom: 1px solid #f1f5f9 !important;
        padding: 0.55rem 1rem !important;
    }

    [data-testid="stDataFrame"] tr:hover td {
        background-color: #f8fafc !important;
        color: #0f172a !important;
    }

    /* ── Column gap refinement ── */
    [data-testid="column"] {
        gap: 1.25rem;
    }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar {
        width: 4px;
        height: 4px;
    }
    ::-webkit-scrollbar-track {
        background: #fdfdfc;
    }
    ::-webkit-scrollbar-thumb {
        background: #cbd5e1;
        border-radius: 2px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #94a3b8;
    }

    /* ── Hide Streamlit chrome ── */
    #MainMenu, footer, header {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.header("Filter Options")
categories = ["All"] + sorted(df_sales['categoryname'].unique().tolist())
selected_category = st.sidebar.selectbox("Select a Product Category", categories)

if selected_category != "All":
    df_filtered = df_sales[df_sales['categoryname'] == selected_category]
else:
    df_filtered = df_sales

#4. KPI METRICS
kpi1, kpi2, kpi3 = st.columns(3)
total_rev = df_filtered['total_sales'].sum()
top_product = df_filtered.loc[df_filtered['total_sales'].idxmax()]['productname'] if not df_filtered.empty else "N/A"
total_items = df_filtered['productname'].nunique()

kpi1.metric(label="Total Revenue", value=f"${total_rev:,.2f}")
kpi2.metric(label="Unique Products Sold", value=total_items)
kpi3.metric(label="Top Performing Product", value=top_product)

st.markdown("<br>", unsafe_allow_html=True)

#5. CHARTS


plotly_layout = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Syne, sans-serif", color="#475569", size=11),
    margin=dict(l=0, r=0, t=30, b=0),
    xaxis=dict(
        gridcolor="#f1f5f9",
        tickcolor="#f1f5f9",
        linecolor="#f1f5f9",
        tickfont=dict(family="DM Mono, monospace", size=10, color="#64748b"),
        tickformat="$,.0f" # <-- Fix 1: Formats the X-axis as currency
    ),
    yaxis=dict(
        gridcolor="#f1f5f9",
        tickcolor="rgba(0,0,0,0)",
        linecolor="rgba(0,0,0,0)",
        tickfont=dict(family="Syne, sans-serif", size=10, color="#64748b"),
    ),
)

col1, col2 = st.columns(2)


if selected_category == "All":
    pie_grouping = 'categoryname'
    bar_color = 'categoryname'
    pie_title = "Revenue Distribution by Category"
else:
    pie_grouping = 'productname'
    bar_color = 'productname'
    pie_title = f"Revenue Share within {selected_category}"

with col1:
    st.subheader("Top Products by Revenue")
    top_10 = df_filtered.sort_values('total_sales', ascending=False).head(10)
    fig_bar = px.bar(
        top_10,
        x='total_sales',
        y='productname',
        orientation='h',
        color=bar_color,
        color_discrete_sequence=["#0ea5e9", "#0284c7", "#0369a1", "#075985", "#38bdf8", "#7dd3fc", "#0c4a6e", "#bae6fd", "#082f49", "#00a8cc"]
    )
    fig_bar.update_layout(
        **plotly_layout,
        xaxis_title="Total Sales",
        yaxis_title="",
        showlegend=False,
    )
    fig_bar.update_yaxes(categoryorder='total ascending')
    fig_bar.update_traces(marker_line_width=0)

    st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})

with col2:
    st.subheader(pie_title)
    df_pie = df_filtered.groupby(pie_grouping)['total_sales'].sum().reset_index()
    fig_pie = px.pie(
        df_pie,
        names=pie_grouping,
        values='total_sales',
        hole=0.55,
        color_discrete_sequence=["#0ea5e9", "#0284c7", "#0369a1", "#075985", "#38bdf8", "#7dd3fc", "#0c4a6e"]
    )
    fig_pie.update_layout(
        **plotly_layout,

        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.1,
            xanchor="center",
            x=0.5,
            font=dict(family="Syne, sans-serif", size=11, color="#475569"),
            bgcolor="rgba(0,0,0,0)",
        )
    )
    fig_pie.update_traces(
        textfont=dict(family="DM Mono, monospace", size=11, color="#ffffff"),
        marker=dict(line=dict(color="#ffffff", width=2)), 
        textposition='inside',
        textinfo='percent'
    )

    st.plotly_chart(fig_pie, use_container_width=True, config={'displayModeBar': False})

st.markdown("---")
st.subheader("Raw Data Detail")
st.dataframe(
    df_filtered.style.format({"total_sales": "${:,.2f}"}), 
    use_container_width=True
)