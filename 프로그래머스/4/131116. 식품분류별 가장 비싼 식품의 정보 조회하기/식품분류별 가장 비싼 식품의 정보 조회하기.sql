SELECT
      f.category
    , f.price AS 'MAX_PRICE'
    , f.product_name
FROM food_product f
JOIN (
    SELECT
          category
        , MAX(price) AS 'max_price'
    FROM food_product
    WHERE category IN ('과자', '국', '김치', '식용유')
    GROUP BY category
) sub
  ON f.category = sub.category AND f.price = sub.max_price
ORDER BY MAX_PRICE DESC;