# Write your MySQL query statement below
WITH combined_orders_table AS 
(
    SELECT Company.com_id, Company.name, Orders.sales_id
    FROM Orders LEFT JOIN Company ON Company.com_id = Orders.com_id
    WHERE Company.name = 'RED'
)

-- select * from combined_orders_table

SELECT DISTINCT SalesPerson.name
FROM SalesPerson
WHERE SalesPerson.sales_id NOT IN (SELECT sales_id FROM combined_orders_table)
