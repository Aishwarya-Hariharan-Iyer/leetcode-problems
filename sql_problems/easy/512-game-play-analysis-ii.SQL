# Write your MySQL query statement below
WITH min_dates AS
                (
                    SELECT MIN(event_date) AS event_date, player_id
                    FROM Activity
                    GROUP BY player_id
                )
SELECT DISTINCT Activity.player_id, Activity.device_id
FROM Activity, min_dates
WHERE Activity.event_date = min_dates.event_date AND Activity.player_id = min_dates.player_id