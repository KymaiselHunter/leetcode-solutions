# Write your MySQL query statement below
SELECT 
    B.student_id,
    B.student_name,
    B.subject_name,
    IFNULL(A.attended_exams, 0) AS attended_exams
FROM (
    SELECT * 
    FROM Students
    CROSS JOIN Subjects
) AS B
LEFT JOIN(
    SELECT *, Count(*) as attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
) AS A
    ON A.student_id = B.student_id
    AND A.subject_name = B.subject_name
ORDER BY B.student_id, B.subject_name;
