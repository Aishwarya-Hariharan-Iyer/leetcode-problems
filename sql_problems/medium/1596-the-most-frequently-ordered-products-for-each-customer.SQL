# Write your MySQL query statement below
WITH pdt_counts AS (
    SELECT 
    customer_id,
    product_id,
    COUNT(order_id) AS pdt_num
    FROM Orders
    GROUP BY customer_id, product_id
),
pdt_ranks AS (
    SELECT 
    pdt_counts.customer_id,
    pdt_counts.product_id,
    RANK() OVER (PARTITION BY customer_id ORDER BY pdt_num DESC) AS rn,
    Products.product_name
    FROM pdt_counts INNER JOIN Products ON pdt_counts.product_id = Products.product_id
)

SELECT 
customer_id,
product_id,
product_name
FROM pdt_ranks
WHERE rn = 1