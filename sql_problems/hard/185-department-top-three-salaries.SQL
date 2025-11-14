# Write your MySQL query statement below
WITH department_salary AS (
    SELECT
    Employee.name AS employee_name,
    Employee.salary,
    Department.name AS dept_name
    FROM Employee INNER JOIN Department ON Employee.departmentId = Department.id
),
salary_ranking AS (
    SELECT
    employee_name,
    salary,
    dept_name,
    DENSE_RANK() OVER (PARTITION BY dept_name ORDER BY salary DESC) AS salary_rank
    FROM department_salary
)

SELECT
dept_name AS department,
employee_name AS employee,
salary
FROM salary_ranking
WHERE salary_rank <= 3