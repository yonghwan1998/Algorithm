SELECT
      u.user_id AS 'USER_ID'
    , u.nickname AS 'NICKNAME'
    , b.TOTAL_SALES AS 'TOTAL_SALES'
FROM used_goods_user u
JOIN (
    SELECT
          writer_id
        , SUM(price) AS 'TOTAL_SALES'
    FROM used_goods_board
    WHERE status = 'DONE'
    GROUP BY writer_id
    HAVING SUM(price) >= 700000
) b
ON u.user_id = b.writer_id
ORDER BY TOTAL_SALES ASC;