# Write your MySQL query statement below
WITH min_years AS
(
SELECT
product_id,
MIN(`year`) OVER (PARTITION BY product_id) AS ref_year
FROM Sales
),
min_year_grps AS
(
    SELECT *
    FROM min_years
    GROUP BY product_id
)

SELECT
Sales.product_id,
Sales.`year` AS first_year,
Sales.quantity,
Sales.price
FROM Sales, min_year_grps
WHERE Sales.`year` = min_year_grps.ref_year 
AND Sales.product_id = min_year_grps.product_id