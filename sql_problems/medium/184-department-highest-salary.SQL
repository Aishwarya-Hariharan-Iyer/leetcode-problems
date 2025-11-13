# Write your MySQL query statement below
WITH ordered_salaries AS 
(
    SELECT 
    departmentId,
    name AS employee,
    salary,
    DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM Employee
)

SELECT Department.name AS department, ordered_salaries.employee, ordered_salaries.salary
FROM ordered_salaries, Department
WHERE ordered_salaries.departmentId = Department.id AND ordered_salaries.salary_rank = 1

