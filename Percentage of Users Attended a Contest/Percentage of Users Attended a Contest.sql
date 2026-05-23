# Write your MySQL query statement below
SELECT 
    -- *,
    -- COUNT(*),
    -- (SELECT COUNT(*) FROM Users),
    contest_id,
    ROUND((COUNT(*) / (SELECT COUNT(*) FROM Users)) * 100, 2) AS percentage
FROM Users AS u
JOIN Register AS r
ON u.user_id = r.user_id
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;