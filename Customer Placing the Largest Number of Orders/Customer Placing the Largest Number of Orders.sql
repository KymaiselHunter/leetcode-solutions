# Write your MySQL query statement below
SELECT 
    -- *, COUNT(*)
    customer_number
FROM 
    ORDERS
GROUP BY 
    customer_number
ORDER BY
    COUNT(*) DESC 
LIMIT 1;