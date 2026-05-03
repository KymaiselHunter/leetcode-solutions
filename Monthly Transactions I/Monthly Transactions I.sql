# Write your MySQL query statement below
SELECT
    -- *,
    -- DATE_FORMAT(trans_date, "%Y-%m")
    -- COUNT(*)
    DATE_FORMAT(trans_date, "%Y-%m") as month,
    country,
    COUNT(*) as trans_count,
    SUM(CASE WHEN STATE = "approved" THEN 1 ELSE 0 END) AS approved_count,
    SUM(amount) as trans_total_amount,
    SUM(CASE WHEN STATE = "approved" THEN amount ELSE 0 END) AS approved_total_amount
FROM 
    Transactions
GROUP BY
    country, DATE_FORMAT(trans_date, "%Y-%m");

