# Write your MySQL query statement below
SELECT A.id
    FROM Weather A
    JOIN Weather B
        on A.recordDate - 1 = B.recordDate
        AND A.temperature > B.temperature;
