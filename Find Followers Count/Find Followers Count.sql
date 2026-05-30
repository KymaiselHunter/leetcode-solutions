# Write your MySQL query statement below
SELECT 
    -- *,
    user_id,
    Count(*) AS followers_count
FROM Followers
GROUP BY user_id;