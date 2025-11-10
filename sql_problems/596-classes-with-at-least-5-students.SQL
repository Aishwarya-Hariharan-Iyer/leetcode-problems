# Write your MySQL query statement below
SELECT class FROM (SELECT class, COUNT(student) AS count_students
                    FROM Courses
                    GROUP BY class
                    HAVING count_students >= 5) as sq