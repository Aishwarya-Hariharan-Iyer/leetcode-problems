# Write your MySQL query statement below

SELECT activity_date as day, COUNT(user_id) AS active_users
FROM (
    SELECT DISTINCT activity_date, user_id FROM Activity
) AS sq
WHERE activity_date >= '2019-06-28' AND activity_date <= '2019-07-27'
GROUP BY activity_date