# Write your MySQL query statement below
WITH combined_subject_student AS
(
    SELECT * FROM students CROSS JOIN subjects 
),
subject_test_counts AS
(
    SELECT student_id, subject_name, COUNT(subject_name) as attended_exams
    FROM examinations
    GROUP BY student_id, subject_name
),
results_table AS
(
    SELECT combined_subject_student.student_id, combined_subject_student.student_name, combined_subject_student.subject_name, subject_test_counts.attended_exams
    FROM combined_subject_student LEFT JOIN subject_test_counts 
    ON subject_test_counts.student_id = combined_subject_student.student_id AND subject_test_counts.subject_name = combined_subject_student.subject_name
)

SELECT student_id, student_name, subject_name, COALESCE(attended_exams, 0) AS attended_exams 
FROM results_table
ORDER BY student_id, subject_name