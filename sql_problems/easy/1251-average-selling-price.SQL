# Write your MySQL query statement below
WITH product_prices AS
(
    SELECT prices.product_id, prices.price, unitssold.units 
    FROM prices LEFT JOIN unitssold
    ON prices.product_id = unitssold.product_id
    AND prices.start_date <= unitssold.purchase_date AND prices.end_date >= unitssold.purchase_date

)


SELECT product_id, COALESCE(ROUND(SUM(units * price)/SUM(units), 2), 0) AS average_price
FROM product_prices
GROUP BY product_id
