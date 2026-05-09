# Write your MySQL query statement below
-- SELECT *
-- FROM Tree
-- WHERE p_id IS NULL;

SELECT id,
    CASE
        WHEN p_id IS null THEN 'Root'
        WHEN id in (
            SELECT p_id
            FROM Tree
        ) THEN 'Inner'
        ELSE "Leaf"
    END AS type
FROM TREE;
-- SELECT DISTINCT A.id 
-- FROM Tree AS A
-- JOIN Tree AS B
-- ON A.id = B.p_id
-- WHERE A.p_id IS NOT NULL; 