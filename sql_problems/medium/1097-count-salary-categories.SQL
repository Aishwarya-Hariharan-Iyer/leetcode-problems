# Write your MySQL query statement below
WITH salary_category AS (
    SELECT
    account_id,
    CASE
    WHEN income < 20000 THEN 'Low Salary'
    WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
    ELSE 'High Salary'
    END AS category
    FROM Accounts
),
all_categories AS
(
    SELECT 'High Salary' AS category
    UNION SELECT 'Low Salary' AS category
    UNION SELECT 'Average Salary' AS category
)

SELECT
all_categories.category,
COALESCE(COUNT(account_id), 0) AS accounts_count
FROM all_categories LEFT JOIN salary_category 
ON all_categories.category = salary_category.category
GROUP BY category