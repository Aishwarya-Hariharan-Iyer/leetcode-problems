# Write your MySQL query statement below
WITH RECURSIVE all_dates AS (
    SELECT DATE('2019-01-01') AS dates
    UNION ALL
    SELECT DATE_ADD(dates, INTERVAL 1 DAY) FROM all_dates
    WHERE dates < DATE('2019-12-31')
),
failed_dates AS (
    SELECT 
    fail_date AS dates, 'failed' AS status
    FROM Failed
),
succeed_dates AS (
    SELECT 
    success_date AS dates, 'succeeded' AS status
    FROM Succeeded
),
merged_status AS (
    SELECT * FROM succeed_dates
    UNION
    SELECT * FROM failed_dates
    
),
period_dates AS (
    SELECT all_dates.dates, merged_status.status
    FROM all_dates INNER JOIN merged_status ON all_dates.dates = merged_status.dates
),
grp_ids AS (
    SELECT
    dates,
    (ROW_NUMBER() OVER (ORDER BY dates) 
    - ROW_NUMBER() OVER (PARTITION BY status ORDER BY dates)) AS grp_id,
    status
    FROM period_dates
)

SELECT 
status AS period_state,
MIN(dates) AS start_date,
MAX(dates) AS end_date
FROM grp_ids
GROUP BY grp_id, status
ORDER BY start_date
