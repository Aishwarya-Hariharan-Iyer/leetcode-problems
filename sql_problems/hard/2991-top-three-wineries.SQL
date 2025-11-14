# Write your MySQL query statement below
WITH combined_points AS 
(
    SELECT
    country,
    winery,
    SUM(points) AS combined_points
    FROM Wineries
    GROUP BY country, winery
),
countries AS (
    SELECT country
    FROM combined_points
    GROUP BY country
    ORDER BY country
),
ranked_wines AS (
    SELECT
    country,
    winery,
    combined_points,
    ROW_NUMBER() OVER (PARTITION BY country ORDER BY combined_points DESC, winery ASC) AS row_no
    FROM 
    combined_points
),
top_winery AS (
    SELECT
    country,
    COALESCE(CONCAT(TRIM(winery), " (", combined_points, ")"), "No top winery") AS top_winery
    FROM ranked_wines
    WHERE row_no = 1
    GROUP BY country
),
second_winery AS (
    SELECT
    country,
    COALESCE(CONCAT(TRIM(winery), " (", combined_points, ")"), "No second winery") AS second_winery
    FROM ranked_wines
    WHERE row_no = 2
    GROUP BY country
),
third_winery AS (
    SELECT
    country,
    COALESCE(CONCAT(TRIM(winery), " (", combined_points, ")"), "No third winery") AS third_winery
    FROM ranked_wines
    WHERE row_no = 3
    GROUP BY country
)

SELECT
countries.country,
COALESCE(top_winery.top_winery, "No top winery") AS top_winery,
COALESCE(second_winery.second_winery, "No second winery") AS second_winery,
COALESCE(third_winery.third_winery, "No third winery") AS third_winery
FROM countries
LEFT JOIN top_winery ON top_winery.country = countries.country
LEFT JOIN second_winery ON second_winery.country = countries.country
LEFT JOIN third_winery ON third_winery.country = countries.country

-- SELECT * FROM countries