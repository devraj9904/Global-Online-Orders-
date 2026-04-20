WITH ranked_products AS (
    SELECT
        dp.categoryname,
        dp.productname,
        SUM(fs.totalamount) AS total_sales,
        ROW_NUMBER()
            OVER (
                PARTITION BY dp.categoryname ORDER BY SUM(fs.totalamount) DESC
            )
            AS rank_in_category
    FROM {{ ref('fact_sales') }} AS fs
    INNER JOIN {{ ref('dim_products') }} AS dp ON fs.productid = dp.productid
    GROUP BY 1, 2
)

SELECT
    categoryname,
    productname,
    total_sales
FROM ranked_products
WHERE rank_in_category = 1
