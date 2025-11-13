# Write your MySQL query statement below
WITH relevant_players AS (
    SELECT 
    player_id,
    TIMESTAMPDIFF(DAY, LAG(event_date)
    OVER
    (PARTITION BY player_id ORDER BY event_date ASC), event_date)
    AS date_diff,
    DENSE_RANK()
    OVER
    (PARTITION BY player_id ORDER BY event_date ASC)
    AS rank_date
    FROM Activity
)


SELECT
COALESCE(ROUND((COUNT(DISTINCT CASE WHEN date_diff = 1 AND rank_date = 2 THEN player_id END)/COUNT(DISTINCT player_id)), 2), 0)
AS fraction
FROM relevant_players