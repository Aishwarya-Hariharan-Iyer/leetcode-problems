# Write your MySQL query statement below
WITH grade_partitions AS (
    SELECT student_id,
    course_id,
    grade,
    RANK() OVER (PARTITION BY student_id ORDER BY grade DESC, course_id) AS rn
    FROM Enrollments
)

SELECT student_id, course_id, grade
FROM grade_partitions
WHERE rn = 1
ORDER BY student_id
