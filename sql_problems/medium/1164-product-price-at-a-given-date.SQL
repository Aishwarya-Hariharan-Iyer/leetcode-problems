# Write your MySQL query statement below
WITH product_prices AS (
    SELECT
    product_id,
    new_price,
    change_date,
    CASE WHEN change_date <= DATE('2019-08-16') THEN 1 ELSE 0 END AS change_needed,
    CASE WHEN change_date <= DATE('2019-08-16') THEN "YES" ELSE "NO" END AS relevant_row
    FROM Products
),
atleast_one_change AS (
    SELECT product_id,
    MAX(change_date) AS date_changed
    FROM product_prices
    WHERE relevant_row = "YES"
    GROUP BY product_id
    HAVING SUM(change_needed) >= 1
),
no_change AS (
    SELECT product_id,
    10 AS price
    FROM product_prices
    GROUP BY product_id
    HAVING SUM(change_needed) = 0
),
changed_prices_table AS (
    SELECT 
    atleast_one_change.product_id,
    CASE 
    WHEN Products.product_id = atleast_one_change.product_id 
    AND Products.change_date = atleast_one_change.date_changed 
    THEN Products.new_price ELSE 0
    END AS price
    FROM Products, atleast_one_change
),
changed_prices_table_final AS (
    SELECT product_id,
    SUM(price) AS price
    FROM changed_prices_table
    GROUP BY product_id
)

SELECT * FROM no_change
UNION
SELECT * FROM changed_prices_table_final
