# Write your MySQL query statement below
WITH unique_coords AS (
    SELECT
    pid,
    tiv_2015,
    tiv_2016
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
),
filtered_investments AS (
    SELECT
    pid,
    tiv_2016,
    COUNT(*) OVER (PARTITION BY tiv_2015) AS count_matches
    FROM Insurance
),
matching_investments AS (
    SELECT
    pid,
    tiv_2016
    FROM filtered_investments
    WHERE count_matches > 1
)

SELECT ROUND(SUM(matching_investments.tiv_2016), 2) AS tiv_2016
FROM matching_investments JOIN unique_coords ON matching_investments.pid = unique_coords.pid
