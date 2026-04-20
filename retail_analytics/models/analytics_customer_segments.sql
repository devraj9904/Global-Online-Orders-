

WITH customer_stats AS (
    SELECT 
        customerid,
        SUM(totalamount) as lifetime_value,
        COUNT(orderid) as order_count,
        AVG(totalamount) as avg_order_value
    FROM {{ ref('fact_sales') }}
    GROUP BY 1
)

SELECT 
    customerid,
    lifetime_value,
    order_count,
    avg_order_value,
    -- Window Function to rank customers by spending
    DENSE_RANK() OVER (ORDER BY lifetime_value DESC) as spending_rank,
    -- categorize based on percentile
    CASE 
        WHEN PERCENT_RANK() OVER (ORDER BY lifetime_value) > 0.9 THEN 'VIP'
        WHEN PERCENT_RANK() OVER (ORDER BY lifetime_value) > 0.5 THEN 'Regular'
        ELSE 'New/Occasional'
    END as customer_segment
FROM customer_stats