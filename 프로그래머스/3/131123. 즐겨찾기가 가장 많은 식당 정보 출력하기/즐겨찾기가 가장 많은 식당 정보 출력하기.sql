-- 코드를 입력하세요
SELECT
      r.food_type
    , r.rest_id
    , r.rest_name
    , r.favorites
FROM rest_info r
JOIN (
    SELECT
          food_type
        , MAX(favorites) AS max_favorites
    FROM rest_info
    GROUP BY food_type
) sub
ON r.food_type = sub.food_type AND r.favorites = sub.max_favorites
ORDER BY food_type DESC;