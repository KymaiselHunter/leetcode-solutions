# Write your MySQL query statement below
Select player_id, event_date as first_login
    FROM Activity
    WHERE (player_id, event_date) NOT IN(
        SELECT A.player_id, A.event_date
        FROM Activity A
        JOIN Activity B
            ON A.player_id = B.player_id
            AND A.event_date > B.event_date
        );