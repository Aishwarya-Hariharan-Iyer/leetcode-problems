# Write your MySQL query statement below
SELECT person.email AS Email
FROM person GROUP BY email
HAVING COUNT(Email) > 1;