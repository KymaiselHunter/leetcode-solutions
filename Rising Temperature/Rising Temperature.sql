# Write your MySQL query statement below
SELECT A.id
    FROM Weather A
    JOIN Weather B
        on A.recordDate = DATE_ADD(B.recordDate, INTERVAL 1 DAY)
        AND A.temperature > B.temperature;
