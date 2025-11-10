# Write your MySQL query statement below
SELECT employee.name AS employee
FROM employee, employee AS reference
WHERE employee.managerId = reference.id AND employee.salary > reference.salary