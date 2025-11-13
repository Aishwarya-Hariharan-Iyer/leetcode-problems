# Write your MySQL query statement below
SELECT * FROM (
SELECT
product_id,
CASE WHEN Products.store1 IS NOT NULL THEN 'store1' END AS store,
CASE WHEN Products.store1 IS NOT NULL THEN store1 END AS price
FROM
Products

UNION ALL

SELECT
product_id,
CASE WHEN Products.store2 IS NOT NULL THEN 'store2' END AS store,
CASE WHEN Products.store2 IS NOT NULL THEN store2 END AS price
FROM
Products

UNION ALL

SELECT
product_id,
CASE WHEN Products.store3 IS NOT NULL THEN 'store3' END AS store,
CASE WHEN Products.store3 IS NOT NULL THEN store3 END AS price
FROM
Products

) AS sq
WHERE price IS NOT NULL