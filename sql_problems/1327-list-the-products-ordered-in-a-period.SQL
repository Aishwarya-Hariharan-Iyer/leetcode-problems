# Write your MySQL query statement below
WITH product_orders AS (
    SELECT product_id, SUM(unit) AS unit
    FROM Orders
    WHERE '2020-01-31' < order_date AND '2020-03-01' > order_date
    GROUP BY product_id
)

SELECT Products.product_name, product_orders.unit
FROM Products, product_orders
WHERE Products.product_id = product_orders.product_id AND product_orders.unit >= 100