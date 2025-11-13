# Write your MySQL query statement below
WITH max_movie_user AS (
    SELECT name AS results
    FROM MovieRating LEFT JOIN Users ON MovieRating.user_id = Users.user_id
    GROUP BY MovieRating.user_id
    ORDER BY COUNT(*) DESC, name
    LIMIT 1
),
max_movie_rating AS (
    SELECT title AS results
    FROM MovieRating LEFT JOIN Movies ON MovieRating.movie_id = Movies.movie_id
    WHERE MovieRating.created_at < '2020-03-01' AND MovieRating.created_at > '2020-01-31'
    GROUP BY MovieRating.movie_id
    ORDER BY AVG(rating) DESC, title
    LIMIT 1
)

SELECT * FROM max_movie_user
UNION ALL
SELECT * FROM max_movie_rating