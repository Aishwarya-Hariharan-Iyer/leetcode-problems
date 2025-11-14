# Write your MySQL query statement below
WITH delivery_types AS (
    SELECT 
    delivery_id,
    customer_id,
    order_date,
    CASE WHEN order_date = customer_pref_delivery_date THEN "immediate" ELSE "scheduled" END AS type
    FROM Delivery
),
first_orders AS (
    SELECT delivery_id,
    MIN(order_date) AS first_order_date,
    customer_id
    FROM Delivery
    GROUP BY customer_id
),
customer_first_order_checks AS (
    SELECT t1.delivery_id
    FROM Delivery AS t1 LEFT JOIN first_orders AS t2 ON t1.customer_id = t2.customer_id
    WHERE t1.order_date = t2.first_order_date 
)

SELECT
ROUND(SUM(CASE WHEN t2.type = "immediate" THEN 1 ELSE 0 END)/COUNT(*) * 100, 2) AS immediate_percentage
FROM customer_first_order_checks AS t1 LEFT JOIN delivery_types AS t2 ON t1.delivery_id = t2.delivery_id