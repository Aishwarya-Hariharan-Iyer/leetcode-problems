# Write your MySQL query statement below
WITH min_3_sub AS (
    SELECT 
    student_id
    FROM study_sessions
    GROUP BY student_id
    HAVING COUNT(DISTINCT subject) >= 3
),
count_each_sub AS (
    SELECT
    study_sessions.student_id,
    subject,
    CASE WHEN COUNT(DISTINCT session_id) >= 2 THEN 0 ELSE 1 END AS sub_count
    FROM study_sessions INNER JOIN min_3_sub ON study_sessions.student_id = min_3_sub.min_3_sub.student_id
    GROUP BY student_id, subject
),
min_each_sub_twice AS (
    SELECT
    student_id
    FROM count_each_sub
    GROUP BY student_id
    HAVING SUM(sub_count) = 0
    
),
lag_dates AS (
    SELECT
    session_id,
    student_id,
    session_date,
    LAG(session_date) OVER (PARTITION BY student_id ORDER BY session_date) AS lag_dates
    FROM study_sessions
),
day_gap_check AS (
    SELECT
    student_id,
    CASE 
    WHEN TIMESTAMPDIFF(DAY, COALESCE(lag_dates, session_date), session_date) <= 2 THEN 0 ELSE 1
    END AS valid_session_gap
    FROM lag_dates
),
max_2_day_gap AS (
    SELECT
    day_gap_check.student_id
    FROM day_gap_check INNER JOIN min_each_sub_twice
    ON day_gap_check.student_id = min_each_sub_twice.student_id
    GROUP BY student_id
    HAVING MAX(valid_session_gap) = 0
),
cycle_details AS (
    SELECT
    study_sessions.student_id,
    COUNT(DISTINCT subject) AS cycle_length,
    SUM(hours_studied) AS total_study_hours
    FROM study_sessions INNER JOIN max_2_day_gap 
    ON study_sessions.student_id = max_2_day_gap.student_id
    GROUP BY study_sessions.student_id
)

SELECT
cycle_details.student_id,
student_name,
major,
cycle_length,
total_study_hours
FROM cycle_details INNER JOIN students ON cycle_details.student_id = students.student_id
ORDER BY cycle_length DESC, total_study_hours DESC
