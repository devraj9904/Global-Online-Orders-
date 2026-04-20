WITH monthly_sales AS (
    SELECT
        DATE_TRUNC('month', o.orderdate) AS sales_month,
        SUM(od.quantity * p.price) AS total_revenue
    FROM {{ ref('fact_sales') }} AS f
    INNER JOIN public.orders AS o ON f.orderid = o.orderid
    INNER JOIN public.products AS p ON f.productid = p.productid
    GROUP BY 1
)

SELECT
    sales_month,
    total_revenue,
    LAG(total_revenue) OVER (ORDER BY sales_month) AS prev_month_revenue,
    (total_revenue - LAG(total_revenue) OVER (ORDER BY sales_month))
    / NULLIF(LAG(total_revenue) OVER (ORDER BY sales_month), 0)
    * 100 AS mom_growth_percentage
FROM monthly_sales
