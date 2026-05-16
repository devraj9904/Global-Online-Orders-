🌍 Global Online Retail Analytics Platform
EAS 550: Data Model Query Language
Team 6: Akshat Sharma · Sujal Sharma · Devraj Tikam

A complete end-to-end data engineering and analytics platform that processes raw global retail data and transforms it into an interactive Business Intelligence dashboard. This project demonstrates modern data engineering practices including data cleaning, normalized database design, dimensional modeling, automated testing, CI/CD, and cloud deployment.

🚀 Live Dashboard

👉 https://global-online-orders.onrender.com

Note: The application is hosted on Render's free tier, so it may take 30–60 seconds to wake up after a period of inactivity.

🎥 Demo Video

👉 https://youtu.be/K1OWxqrYM6k

📊 Project Overview

This platform is designed to process and analyze transactional data for a global online retail system. The system ingests raw data containing:

Customers
Orders
Order Details
Products
Categories
Suppliers
Shipping Information

The project implements a cloud-native analytics pipeline using:

Python and Pandas for data cleaning
PostgreSQL on Neon for cloud database hosting
dbt Core for data transformation and testing
Streamlit and Plotly for dashboard development
GitHub Actions for CI/CD
Render for public deployment

The final result is a scalable analytics platform that converts raw CSV data into actionable business insights.

✨ Key Features
✅ Cloud-hosted PostgreSQL database on Neon
✅ Fully normalized relational schema (Third Normal Form)
✅ Star schema transformation using dbt
✅ Automated data quality tests
✅ CI/CD pipeline with GitHub Actions
✅ Interactive BI dashboard with filtering and visualizations
✅ Connection pooling and caching for performance optimization
✅ Public deployment on Render

🏗️ Proposed Architecture




🗄️ Relational Modeling (3NF)

Our database schema is designed to eliminate redundancy and ensure referential integrity.

Core Design Principles
Third Normal Form (3NF): All entities are separated into logically distinct tables.
Bridge Table: order_details resolves the many-to-many relationship between orders and products.
Referential Integrity: Foreign key constraints enforce valid relationships.
Data Consistency: Primary keys, unique constraints, and not-null constraints ensure clean data.
Key Tables
customers
orders
order_details
products
categories
suppliers
shippers
🔄 End-to-End Pipeline Workflow
1. Raw Data Acquisition

The source dataset is obtained from Kaggle and contains transactional retail data.

2. Data Cleaning

Python and Pandas are used to:

Remove duplicates and missing values
Standardize formats
Prepare normalized tables
3. Cloud Database Loading

SQLAlchemy loads cleaned data into Neon PostgreSQL.

4. Data Transformation

dbt converts normalized data into a Star Schema optimized for analytics.

5. Data Validation

Automated tests ensure data integrity and transformation correctness.

6. Dashboard Development

Streamlit and Plotly create an interactive analytics dashboard with:

KPI cards (Total Revenue, Unique Products Sold, Top Product)
Top products by revenue
Revenue distribution by category
Raw data exploration
Sidebar filtering by category
7. Deployment

Render hosts the application with automatic deployments from GitHub.

📸 Dashboard Preview
📌 Main Dashboard Overview

Interactive dashboard featuring category filters, KPI cards, and revenue visualizations.

📈 Revenue Analytics

Bar charts and donut charts reveal top-performing products and category-level revenue distribution.

📋 Raw Data Detail

Users can inspect the underlying PostgreSQL query results directly within the dashboard.

⚙️ Technology Stack
Layer	Technology
Data Source	Kaggle Global Retail Dataset
Data Cleaning	Python, Pandas
Database	PostgreSQL (Neon Serverless)
Data Modeling	dbt Core
Data Quality	dbt Tests
Backend Connectivity	psycopg2, SQLAlchemy
Dashboard	Streamlit, Plotly
CI/CD	GitHub Actions
Deployment	Render

🧪 Reproducibility & Running Locally
Prerequisites
Python 3.9 or higher
PostgreSQL-compatible database (Neon recommended)
Git
1. Clone the Repository
git clone https://github.com/devraj9904/Global-Online-Orders.git
cd Global-Online-Orders
2. Install Dependencies
pip install -r requirements.txt
3. Configure Environment Variables

Create a .env file in the project root:

DATABASE_URL=postgresql://<user>:<password>@<host>/<database>?sslmode=require
4. Run the Data Ingestion Pipeline
python ingest_data.py
5. Run dbt Transformations and Tests
dbt run
dbt test
6. Launch the Dashboard
cd app
streamlit run dashboard.py
7. Open in Browser

Visit:

http://localhost:8501
🔐 Security & Monitoring
Role-Based Access Control (RBAC)

Two database roles were implemented:

data_analyst: Read-only access (SELECT)
data_engineer: Read and write access (SELECT, INSERT, UPDATE)
Resource Monitoring

Compute usage and connection metrics are monitored through the Neon Dashboard to stay within monthly compute limits and ensure efficient connection pooling.

🤖 Generative AI Disclosure

In accordance with course policy, generative AI tools (including Gemini and ChatGPT) were used for:

SQLAlchemy and Pandas syntax assistance
README documentation refinement
Conceptual explanations of normalization and dimensional modeling

All generated content was reviewed, validated, and modified by the project team.

📁 Project Structure
Global-Online-Orders/
│
├── app/
│   ├── dashboard.py
│   ├── requirements.txt
│   └── .env
│
├── ingest_data.py
│
├── dbt/
│   ├── models/
│   └── tests/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── assets/
│   ├── dashboard_main.png
│   ├── sales_trends.png
│   └── raw_data_table.png
│
├── .python-version
└── README.md

📈 Business Insights Enabled

This dashboard allows users to:

Identify top-performing products
Compare revenue across product categories
Analyze overall sales performance
Explore detailed transaction-level data

🧠 Skills Demonstrated
Data Engineering
ETL / ELT Pipeline Development
Relational Database Design
Third Normal Form (3NF)
Dimensional Modeling
dbt Transformations and Testing
CI/CD Automation
Dashboard Development
Cloud Deployment
Performance Optimization

🚀 Future Enhancements
Workflow orchestration with Apache Airflow
Sales forecasting using machine learning
Role-based dashboard authentication
Real-time data ingestion with Apache Kafka

👥 Team Members
Sujal Sharma
Devraj Tikam
Akshat Sharma

⭐ Acknowledgments

This project was developed as part of EAS 550: Data Model Query Language at the University at Buffalo.