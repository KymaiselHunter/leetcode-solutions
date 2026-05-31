# Write your MySQL query statement below
SELECT MAX(num) as num
FROM
(
    SELECT
    *
    FROM MyNumbers
    GROUP BY num
    HAVING Count(*) = 1
) as A;