# Write your MySQL query statement below
WITH filtered_bookings AS (
    SELECT 
    id,
    client_id,
    driver_id,
    status,
    request_at
    FROM Trips 
    LEFT JOIN Users AS u1 ON Trips.client_id = u1.users_id
    LEFT JOIN Users AS u2 ON Trips.driver_id = u2.users_id
    WHERE (request_at >= '2013-10-01' AND request_at <= '2013-10-03')
    AND u1.banned = 'No' AND u2.banned = 'No'

),
cancelled_bookings_table AS (
SELECT
request_at,
ROUND(
(SUM(CASE WHEN status = 'cancelled_by_driver' OR status = 'cancelled_by_client' THEN 1 ELSE 0 END) OVER (PARTITION BY request_at ORDER BY request_at ASC))
/
(COUNT(*) OVER (PARTITION BY request_at ORDER BY request_at ASC)),
2) AS cancelled_bookings
FROM filtered_bookings
)

SELECT 
request_at AS `Day`,
cancelled_bookings AS `Cancellation Rate`
FROM cancelled_bookings_table 
GROUP BY request_at


