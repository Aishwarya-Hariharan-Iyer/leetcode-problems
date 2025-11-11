# Write your MySQL query statement below
SELECT id,
SUM(IF(MONTH = 'Jan', revenue, null)) AS 'Jan_Revenue',
SUM(IF(MONTH = 'Feb', revenue, null)) AS 'Feb_Revenue',
SUM(IF(MONTH = 'Mar', revenue, null)) AS 'Mar_Revenue',
SUM(IF(MONTH = 'Apr', revenue, null)) AS 'Apr_Revenue',
SUM(IF(MONTH = 'May', revenue, null)) AS 'May_Revenue',
SUM(IF(MONTH = 'Jun', revenue, null)) AS 'Jun_Revenue',
SUM(IF(MONTH = 'Jul', revenue, null)) AS 'Jul_Revenue',
SUM(IF(MONTH = 'Aug', revenue, null)) AS 'Aug_Revenue',
SUM(IF(MONTH = 'Sep', revenue, null)) AS 'Sep_Revenue',
SUM(IF(MONTH = 'Oct', revenue, null)) AS 'Oct_Revenue',
SUM(IF(MONTH = 'Nov', revenue, null)) AS 'Nov_Revenue',
SUM(IF(MONTH = 'Dec', revenue, null)) AS 'Dec_Revenue'
FROM Department
GROUP BY id
