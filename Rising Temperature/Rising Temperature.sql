# Write your MySQL query statement below
SELECT A.id
    FROM Weather A
    JOIN Weather B
        on A.id - 1 = B.id
        AND A.temperature > B.temperature;
