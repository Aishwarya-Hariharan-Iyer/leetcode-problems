# Write your MySQL query statement below
WITH window_avg AS (
    SELECT 
        visited_on,
        DENSE_RANK() OVER (ORDER BY visited_on) AS rn,
        SUM(amount) OVER (
            ORDER BY visited_on
            RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW
        ) AS amount,
        ROUND(SUM(amount) OVER (
            ORDER BY visited_on
            RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW
        )/7, 2) AS average_amount
    FROM Customer
)

SELECT
visited_on,
amount,
average_amount
FROM window_avg
WHERE rn >= 7
GROUP BY visited_on