# Write your MySQL query statement below
SELECT sq.customer_number FROM (
    SELECT Orders.customer_number, COUNT(Orders.order_number) AS count_orders
    FROM Orders
    GROUP BY customer_number
    ORDER BY count_orders DESC
    LIMIT 1) as sq