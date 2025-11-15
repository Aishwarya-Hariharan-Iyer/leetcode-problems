# Write your MySQL query statement below
WITH customer_pdt_pairs AS 
(
    SELECT p1.user_id, p1.product_id as pid1, p2.product_id AS pid2
    FROM ProductPurchases AS p1 INNER JOIN ProductPurchases AS p2 ON
    p1.user_id = p2.user_id AND p1.product_id < p2.product_id
),
customer_counts AS 
(
    SELECT
    COUNT(DISTINCT user_id) AS customer_count, pid1, pid2
    FROM customer_pdt_pairs
    GROUP BY pid1, pid2
    HAVING COUNT(DISTINCT user_id) >= 3

)

SELECT 
pid1 AS product1_id,
pid2 AS product2_id,
p1.category AS product1_category,
p2.category AS product2_category,
customer_count
FROM customer_counts AS c1
INNER JOIN ProductInfo AS p1 ON c1.pid1 = p1.product_id
INNER JOIN ProductInfo AS p2 ON c1.pid2 = p2.product_id
ORDER BY customer_count DESC, product1_id, product2_id