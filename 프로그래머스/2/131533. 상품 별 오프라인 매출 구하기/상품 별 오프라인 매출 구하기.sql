-- 코드를 입력하세요
SELECT
      p.product_code AS product_code
    , p.price * SUM(os.sales_amount) AS sales
FROM product p
INNER JOIN offline_sale os
ON p.product_id = os.product_id
GROUP BY os.product_id
ORDER BY sales DESC, product_code ASC;