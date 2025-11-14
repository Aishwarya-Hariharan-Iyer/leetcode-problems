# Write your MySQL query statement below
WITH manager_chain_lvl_2 AS (
    SELECT
    e1.employee_id,
    e1.manager_id AS m_lvl_1,
    e2.manager_id AS m_lvl_2
    FROM Employees AS e1 INNER JOIN Employees AS e2 ON e2.employee_id = e1.manager_id
    WHERE e1.employee_id != 1
),
manager_chain_lvl_3 AS (
    SELECT
    e1.employee_id,
    m_lvl_1,
    m_lvl_2,
    e2.manager_id AS m_lvl_3
    FROM manager_chain_lvl_2 AS e1 INNER JOIN Employees AS e2 ON e2.employee_id = e1.m_lvl_2
),
filtered_employees AS (
    SELECT
    CASE WHEN m_lvl_1 = 1 OR m_lvl_2 = 1 OR m_lvl_3 = 1 THEN employee_id END AS employee_id 
    FROM manager_chain_lvl_3
    ORDER BY employee_id
)

SELECT * FROM filtered_employees WHERE employee_id IS NOT NULL
