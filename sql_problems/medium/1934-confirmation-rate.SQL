# Write your MySQL query statement below
WITH confirmation_rate_table AS (
    SELECT 
    user_id, 
    COUNT(CASE WHEN action = 'confirmed' THEN 1 END)/COUNT(*) AS confirmation_rate
    FROM Confirmations
    GROUP BY user_id
)

SELECT 
Signups.user_id,
ROUND(COALESCE(confirmation_rate_table.confirmation_rate, 0), 2) AS confirmation_rate
FROM Signups LEFT JOIN confirmation_rate_table 
ON Signups.user_id = confirmation_rate_table.user_id