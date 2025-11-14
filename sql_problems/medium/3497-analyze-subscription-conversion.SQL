# Write your MySQL query statement below
WITH filtered_users AS (
    SELECT 
    user_id 
    FROM UserActivity
    GROUP BY user_id
    HAVING MAX(activity_type) = "paid"
),
activity_duration_free_trial AS (
    SELECT
    filtered_users.user_id,
    activity_type,
    ROUND(AVG(activity_duration), 2) AS avg_duration
    FROM filtered_users INNER JOIN UserActivity ON filtered_users.user_id = UserActivity.user_id
    GROUP BY user_id, activity_type
), 
combined_table AS (
    SELECT
    user_id,
    COALESCE(CASE WHEN activity_type = "free_trial" THEN avg_duration END, 0) AS trial_avg_duration,
     COALESCE(CASE WHEN activity_type = "paid" THEN avg_duration END, 0) AS paid_avg_duration
    FROM activity_duration_free_trial
)

SELECT
user_id,
SUM(trial_avg_duration) AS trial_avg_duration,
SUM(paid_avg_duration) AS paid_avg_duration
FROM combined_table
GROUP BY user_id