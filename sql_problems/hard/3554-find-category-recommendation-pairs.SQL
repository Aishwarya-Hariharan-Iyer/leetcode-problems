# Write your MySQL query statement below
WITH user_category_purchases AS (
    SELECT ProductPurchases.user_id,
    ProductPurchases.product_id,
    SUM(ProductPurchases.quantity) AS quantity,
    ProductInfo.category
    FROM ProductPurchases INNER JOIN ProductInfo ON ProductPurchases.product_id = ProductInfo.product_id
    GROUP BY user_id, category
),
user_category_pair_purchases AS (
    SELECT user_category_purchases.user_id,
    user_category_purchases.category AS c1,
    user_category_purchases.quantity AS q1,
    ref.category AS c2,
    ref.quantity AS q2
    FROM user_category_purchases INNER JOIN user_category_purchases AS ref ON user_category_purchases.user_id = ref.user_id
    WHERE user_category_purchases.category < ref.category
),
all_pairs_counts AS (
    SELECT
    c1 AS category1,
    c2 AS category2,
    COUNT(DISTINCT user_id) AS customer_count
    FROM user_category_pair_purchases
    GROUP BY category1, category2
    ORDER BY customer_count DESC, category1 ASC, category2 ASC
)

SELECT * FROM all_pairs_counts WHERE customer_count >= 3