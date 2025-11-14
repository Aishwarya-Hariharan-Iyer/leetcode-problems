# Write your MySQL query statement below
WITH moving_sum AS (
    SELECT 
    person_name,
    SUM(weight) OVER (
        ORDER BY turn
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS weight_cum_sum
    FROM Queue
)

SELECT person_name
FROM moving_sum
WHERE weight_cum_sum <= 1000
ORDER BY weight_cum_sum DESC
LIMIT 1