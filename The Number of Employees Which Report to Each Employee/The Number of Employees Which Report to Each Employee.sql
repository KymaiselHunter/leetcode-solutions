# Write your MySQL query statement below
SELECT
    Employees.employee_id,
    Employees.name,
    Reports.reports_count,
    Reports.average_age
FROM
    Employees
JOIN
(
    SELECT 
        *,
        COUNT(*) AS reports_count,
        ROUND(AVG(age)) AS average_age
    FROM 
        Employees
    WHERE 
        reports_to IS NOT NULL
    GROUP BY 
        reports_to
) AS Reports
ON Reports.reports_to = Employees.employee_id;