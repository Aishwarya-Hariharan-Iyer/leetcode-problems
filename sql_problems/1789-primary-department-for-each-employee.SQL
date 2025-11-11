# Write your MySQL query statement below
WITH single_department_employees AS
(
    SELECT employee_id, department_id, COUNT(department_id) AS number_depts
        FROM Employee
        GROUP BY employee_id
        HAVING number_depts = 1
),
primary_department_employees AS
(
    SELECT employee_id, department_id 
    FROM Employee
    WHERE Employee.primary_flag = 'Y'

)

SELECT employee_id, department_id FROM primary_department_employees
UNION
SELECT employee_id, department_id from single_department_employees
