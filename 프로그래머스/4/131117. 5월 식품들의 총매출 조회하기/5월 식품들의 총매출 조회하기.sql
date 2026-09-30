-- 코드를 입력하세요
SELECT
      fp.product_id AS 'PRODUCT_ID'
    , fp.product_name AS 'PRODUCT_NAME'
    , fp.price * SUM(fo.amount) AS 'TOTAL_SALES'
FROM food_product fp
JOIN food_order fo
  ON fp.product_id = fo.product_id
WHERE fo.produce_date LIKE '2022-05%'
GROUP BY fp.product_id
ORDER BY total_sales DESC, fp.product_id ASC;