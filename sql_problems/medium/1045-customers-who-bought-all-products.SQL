# Write your MySQL query statement below
WITH tl_count AS 
(
    SELECT COUNT(DISTINCT product_key) AS pdt_count
    FROM Product
),
customer_count AS 
(
    SELECT customer_id, COUNT(DISTINCT product_key) as cus_count
    FROM Customer
    GROUP BY customer_id
)

SELECT customer_id
FROM customer_count, tl_count
WHERE customer_count.cus_count = tl_count.pdt_count