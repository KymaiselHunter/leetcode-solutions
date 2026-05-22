# Write your MySQL query statement below
SELECT 
    -- *,
    p.product_id,
    -- price * units,
    -- SUM(units),
    ROUND(SUM(p.price * u.units) / SUM(units), 2) AS average_price
    -- price * units / SUM(units)
FROM Prices AS p
JOIN UnitsSold AS u
ON purchase_date BETWEEN start_date AND end_date
AND p.product_id = u.product_id
GROUP BY p.product_id;