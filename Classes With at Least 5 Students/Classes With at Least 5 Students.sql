# Write your MySQL query statement below
SELECT 
    -- *, COUNT(*)
    class
FROM
    COURSES
GROUP BY
    class
HAVING COUNT(*) >= 5;