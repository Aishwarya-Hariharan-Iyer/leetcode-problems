# Write your MySQL query statement below
WITH multiple_exam_takers AS (
    SELECT 
    student_id,
    subject,
    MIN(exam_date) AS first_date,
    MAX(exam_date) AS latest_date
    FROM Scores
    GROUP BY student_id, subject
    HAVING MAX(exam_date) != MIN(exam_date)
),
first_exam_scores AS (
    SELECT
    t1.student_id,
    t1.subject,
    latest_date,
    t2.score AS first_score
    FROM multiple_exam_takers AS t1 INNER JOIN Scores AS t2 ON
    t1.student_id = t2.student_id AND t1.subject = t2.subject
    AND t1.first_date = t2.exam_date
),
latest_exam_scores AS (
    SELECT
    t1.student_id,
    t1.subject,
    t1.first_score,
    t2.score AS latest_score
    FROM first_exam_scores AS t1 INNER JOIN Scores AS t2 ON
    t1.student_id = t2.student_id AND t1.subject = t2.subject
    AND t1.latest_date = t2.exam_date
)


SELECT * FROM latest_exam_scores
WHERE latest_score > first_score
ORDER BY student_id, subject