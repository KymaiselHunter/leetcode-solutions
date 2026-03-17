# Write your MySQL query statement below
SELECT DISTINCT a.email
    FROM Person as A
    JOIN PERSON as B
        on A.email = B.email
        AND A.id <> B.id;