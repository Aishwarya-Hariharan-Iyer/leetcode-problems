# Write your MySQL query statement below
WITH requester_friends AS (
    SELECT 
    requester_id AS id,
    COUNT(DISTINCT accepter_id) AS num
    FROM RequestAccepted
    GROUP BY requester_id
),
accepter_friends AS (
    SELECT 
    accepter_id AS id,
    COUNT(DISTINCT requester_id) AS num
    FROM RequestAccepted
    GROUP BY accepter_id  
),
combined_table AS (
    SELECT * FROM requester_friends
    UNION ALL
    SELECT * FROM accepter_friends

)

SELECT
id,
SUM(num) AS num
FROM combined_table
GROUP BY id
ORDER BY num DESC
LIMIT 1