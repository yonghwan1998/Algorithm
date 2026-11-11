WITH RECURSIVE cte_hour
AS (
    SELECT 0 AS n

    UNION ALL

    SELECT n + 1
    FROM cte_hour
    WHERE n < 23
)

SELECT
      ch.n AS 'HOUR'
    , IFNULL(sub.count, 0) AS 'COUNT'
FROM cte_hour ch
LEFT JOIN (
    SELECT
          HOUR(datetime) AS 'hour'
        , COUNT(*) AS 'count'
    FROM animal_outs
    GROUP BY HOUR(datetime)
) sub
ON ch.n = sub.hour
ORDER BY HOUR ASC;