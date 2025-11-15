# Write your MySQL query statement below
WITH orders_counts AS (
    SELECT 
    buyer_id,
    COUNT(order_id) AS orders_in_2019
    FROM Orders
    WHERE DATE("2019-01-01") <= order_date AND DATE("2019-12-31") >= order_date
    GROUP BY buyer_id
)

SELECT 
user_id AS buyer_id,
join_date,
COALESCE(orders_in_2019, 0) AS orders_in_2019
FROM Users LEFT JOIN orders_counts ON user_id = buyer_id