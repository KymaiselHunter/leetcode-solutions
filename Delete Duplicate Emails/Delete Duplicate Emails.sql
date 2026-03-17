# Write your MySQL query statement below
DELETE A FROM Person as A
    JOIN Person as B
    ON A.email = b.email
    AND A.id > B.id;
