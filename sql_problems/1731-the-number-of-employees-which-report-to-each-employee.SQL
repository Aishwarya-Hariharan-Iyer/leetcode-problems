# Write your MySQL query statement below
WITH managers_group AS 
(
    SELECT reports_to AS manager, ROUND(AVG(age)) AS average_age, COUNT(employee_id) AS reports_count
    FROM Employees
    WHERE reports_to IS NOT NULL
    GROUP BY reports_to
)

SELECT Employees.employee_id, Employees.name, managers_group.reports_count, managers_group.average_age
FROM managers_group LEFT JOIN Employees ON Employees.employee_id = managers_group.manager
ORDER BY Employees.employee_id