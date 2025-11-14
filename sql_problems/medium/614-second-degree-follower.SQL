# Write your MySQL query statement below
WITH follows_atleast_one_user AS (
    SELECT follower AS name
    FROM Follow
    GROUP BY follower
    HAVING COUNT(followee) >= 1
),
followee_count_table AS (
    SELECT followee AS name,
    COUNT(follower) AS num
    FROM Follow
    GROUP BY followee
    HAVING COUNT(follower) >= 1
)

SELECT
followee_count_table.name AS follower,
followee_count_table.num
FROM followee_count_table INNER JOIN follows_atleast_one_user ON followee_count_table.name = follows_atleast_one_user.name
ORDER BY followee_count_table.name