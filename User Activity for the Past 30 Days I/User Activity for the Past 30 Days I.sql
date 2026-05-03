# Write your MySQL query statement below
SELECT 
    -- *,
    activity_date as day,
    Count(DISTINCT user_id) as active_users
FROM 
    Activity
WHERE
    activity_date > DATE_SUB('2019-07-27', INTERVAL 30 DAY)
    AND activity_date <= '2019-07-27'
GROUP BY
    activity_date;
