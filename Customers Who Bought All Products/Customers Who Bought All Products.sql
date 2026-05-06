# Write your MySQL query statement below
SELECT 
    -- *,
    -- COUNT(*),
    customer_id
FROM (
    SELECT DISTINCT 
        c.customer_id,
        c.product_key
    FROM Customer as C
    JOIN Product as P
    ON c.product_key = p.product_key
) as A
GROUP BY Customer_id
HAVING COUNT(*) = (
    SELECT COUNT(*)
    FROM Product
);