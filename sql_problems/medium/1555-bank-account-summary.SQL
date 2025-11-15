# Write your MySQL query statement below
WITH amount_to_add AS (
    SELECT
    paid_to AS user_id,
    SUM(amount) AS to_add
    FROM Transactions
    GROUP BY paid_to
),
amount_to_deduct AS (
    SELECT
    paid_by AS user_id,
    SUM(amount) AS to_deduct
    FROM Transactions
    GROUP BY paid_by
)

SELECT 
    Users.user_id,
    user_name,
    credit + COALESCE(to_add, 0) - COALESCE(to_deduct, 0) AS credit,
    CASE WHEN credit + COALESCE(to_add, 0) - COALESCE(to_deduct, 0) < 0 THEN "Yes" ELSE "No" END AS credit_limit_breached
    FROM Users LEFT JOIN amount_to_add ON Users.user_id = amount_to_add.user_id
    LEFT JOIN amount_to_deduct ON Users.user_id = amount_to_deduct.user_id