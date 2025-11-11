# Write your MySQL query statement below

WITH durations_table AS (
    SELECT activity.machine_id, activity.process_id, (activity.timestamp - reference.timestamp) AS durations
    FROM activity, activity AS reference
    WHERE activity.machine_id = reference.machine_id AND activity.process_id = reference.process_id
    AND activity.activity_type = 'end' AND reference.activity_type = 'start'
)

SELECT machine_id, ROUND(AVG(durations), 3) AS processing_time
FROM durations_table
GROUP BY machine_id
