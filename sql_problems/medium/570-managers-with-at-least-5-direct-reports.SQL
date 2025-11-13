# Write your MySQL query statement below
WITH manager_employees_count AS 
(
    SELECT COUNT(*) AS employee_counts, managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
)


SELECT Employee.name 
FROM Employee, manager_employees_count
WHERE Employee.id = manager_employees_count.managerId
AND manager_employees_count.employee_counts >= 5