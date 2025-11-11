# Write your MySQL query statement below

SELECT SQRT(POW(Point.x - Reference.x, 2)) as shortest
FROM Point CROSS JOIN Point AS Reference
WHERE Point.x != Reference.x
ORDER BY shortest
LIMIT 1