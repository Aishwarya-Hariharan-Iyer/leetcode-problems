# Write your MySQL query statement below
WITH num_ranking AS (
    SELECT id,
    ROW_NUMBER() OVER(ORDER BY id ASC) AS r_no,
    ROW_NUMBER() OVER(PARTITION BY num ORDER BY id ASC) AS r_grp_no,
    num
    FROM 
    Logs
),
grp_ranking AS (
    SELECT
    id,
    (r_no - r_grp_no) AS grp_id,
    num
    FROM 
    num_ranking
),
conseq_nums AS 
(
    SELECT
    num,
    COUNT(*) AS conseq_nums
    FROM grp_ranking
    GROUP BY num, grp_id
),
conseq_nums_non_zero AS 
(
    SELECT 
    CASE WHEN conseq_nums >= 3 THEN num ELSE NULL END AS ConsecutiveNums
    FROM conseq_nums
)

SELECT DISTINCT ConsecutiveNums
FROM conseq_nums_non_zero
WHERE ConsecutiveNums IS NOT NULL
