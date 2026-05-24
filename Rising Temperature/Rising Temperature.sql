# Write your MySQL query statement below
SELECT
    -- *
    t.id AS id
FROM Weather AS t
JOIN Weather AS y
ON DATE_SUB(t.recordDate, INTERVAL 1 DAY) = y.recordDate
WHERE t.temperature > y.temperature;