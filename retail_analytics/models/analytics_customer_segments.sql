WITH customer_stats AS (
    SELECT
        customerid,
        SUM(totalamount) AS lifetime_value,
        COUNT(orderid) AS order_count,
        AVG(totalamount) AS avg_order_value
    FROM {{ ref('fact_sales') }}
    GROUP BY 1
)

SELECT
    customerid,
    lifetime_value,
    order_count,
    avg_order_value,
    -- Window Function to rank customers by spending
    DENSE_RANK() OVER (ORDER BY lifetime_value DESC) AS spending_rank,
    -- categorize based on percentile
    CASE
        WHEN PERCENT_RANK() OVER (ORDER BY lifetime_value) > 0.9 THEN 'VIP'
        WHEN PERCENT_RANK() OVER (ORDER BY lifetime_value) > 0.5 THEN 'Regular'
        ELSE 'New/Occasional'
    END AS customer_segment
FROM customer_stats
