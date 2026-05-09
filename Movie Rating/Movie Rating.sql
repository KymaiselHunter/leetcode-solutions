# Write your MySQL query statement below

(    
    SELECT 
        name as results
    FROM MovieRating
    JOIN Users
    ON MovieRating.user_id = Users.user_id
    GROUP BY Users.user_id
    ORDER BY COUNT(*) DESC, name ASC
    LIMIT 1
)
UNION ALL
(
    SELECT 
        title as results
    FROM MovieRating
    JOIN Movies
    ON MovieRating.movie_id = Movies.movie_id
    WHERE created_at >= '2020-02-01'
    AND created_at < '2020-03-01'
    GROUP BY Movies.movie_id
    ORDER BY AVG(rating) DESC, title ASC
    LIMIT 1
);