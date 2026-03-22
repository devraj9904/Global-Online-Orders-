# Global Online Retail Analytics Platform
EAS 550: Data Model Query Language - Phase 1 
Team 6: Akshat Sharma, Sujal Sharma, Devraj Tikam 

## 1. Project Overview
This platform is designed to process and analyze transactional data for a global online retail system. The system ingests raw data encompassing customers, orders, products, suppliers, and shipping information. For Phase 1, we have implemented a cloud-native infrastructure using PostgreSQL on Neon, featuring a fully normalized relational schema in Third Normal Form (3NF).

## 2. Proposed Architecture
The end-to-end data lifecycle for this project is as follows:
Raw CSV Data → Python/Pandas (Cleaning) → PostgreSQL (Neon Cloud) → dbt Core (Transformation) → Streamlit Dashboard → Render Deployment.

## 3. Relational Modeling (3NF)
Our database schema is designed to eliminate data redundancy and ensure referential integrity.
* Bridge Tables: We utilized `order_details` to resolve the many-to-many relationship between orders and products.
* Constraints: The schema enforces `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, and `UNIQUE` constraints across all tables.



## 4. Technical Setup & Ingestion
### Prerequisites
* Python 3.9+
* Libraries: `pandas`, `sqlalchemy`, `psycopg2-binary`, `python-dotenv` 

### Setup Instructions
1. Clone the Repository:
   ```bash
   git clone <your-repo-url>
   ```
2. Environment Variables: Create a `.env` file in the root directory and add your Neon connection string:
   ```env
   DATABASE_URL=postgresql://user:password@hostname/dbname?sslmode=require
   ```
3. Run Ingestion Pipeline: Execute the idempotent Python script to clean and load the dataset into the cloud.
   ```bash
   python ingest_data.py
   ```

## 5. Security & Monitoring
* RBAC: We implemented Role-Based Access Control with two distinct roles: `data_analyst` (SELECT only) and `data_engineer` (SELECT, INSERT, UPDATE).
* Resource Monitoring: Compute usage is actively monitored via the Neon Dashboard to manage the 100 CU-hour monthly limit and ensure proper connection pooling.

## 6. Generative AI Disclosure
In accordance with the course policy, we disclose the use of Gemini 3 Flash for the following tasks:
* Tasks Assisted: Syntax assistance for SQLAlchemy/Pandas, boilerplate generation for the README, and conceptual explanations of 3NF.
* Sample Prompt: *"Write an idempotent Python script using Pandas and SQLAlchemy to clean and load data into PostgreSQL while handling NaNs."



