# Write your MySQL query statement below
WITH criteria_table AS (
    SELECT
    id,
    visit_date,
    people,
    CASE WHEN people >= 100 THEN 'YES' ELSE 'NO' END AS criteria
    FROM Stadium
),
partitions_table AS 
(
    SELECT
    id,
    visit_date,
    criteria,
    people,
    (CAST(id AS SIGNED) - ROW_NUMBER() OVER (PARTITION BY criteria     ORDER BY visit_date)) AS group_id
    FROM criteria_table
),
group_counts AS
(
    SELECT
    id,
    visit_date,
    people,
    COUNT(*) OVER (PARTITION BY criteria, group_id) AS group_count
    FROM partitions_table
)

SELECT id, visit_date, people
FROM group_counts
WHERE group_count >= 3
ORDER BY visit_date ASC