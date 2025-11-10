# Write your MySQL query statement below
SELECT Weather.id 
FROM Weather, Weather AS Reference
WHERE DATEDIFF(Weather.recordDate, Reference.recordDate) = 1 AND Weather.temperature > Reference.temperature