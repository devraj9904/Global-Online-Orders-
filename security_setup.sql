-- 1. Create the Data Analyst Role
-- Analysts should only be able to view data, not change it.
CREATE ROLE data_analyst WITH LOGIN PASSWORD 'secure_analyst_password';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO data_analyst;

-- 2. Create the Data Engineer Role
-- Engineers need to view, add, and modify data for the pipeline.
CREATE ROLE data_engineer WITH LOGIN PASSWORD 'secure_engineer_password';
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO data_engineer;