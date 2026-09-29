-- 코드를 입력하세요
SELECT
      ii.ingredient_type
    , SUM(fh.total_order) AS total_order
FROM icecream_info ii
INNER JOIN first_half fh
ON ii.flavor = fh.flavor
GROUP BY ii.ingredient_type
ORDER BY total_order ASC;