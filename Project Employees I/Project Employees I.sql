# Write your MySQL query statement below
SELECT 
    -- *,
    project_id,
    AVG(experience_years) AS average_years
FROM Project AS p
JOIN Employee AS e
ON e.employee_id = p.employee_id
GROUP BY project_id;