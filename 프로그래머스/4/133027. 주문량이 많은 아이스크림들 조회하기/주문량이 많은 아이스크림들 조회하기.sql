SELECT
    sub.flavor
FROM (
    SELECT
          shipment_id
        , flavor
        , total_order
    from first_half

    UNION ALL

    SELECT
          shipment_id
        , flavor
        , total_order
    from july
) AS sub
GROUP BY sub.flavor
ORDER BY SUM(sub.total_order) DESC
LIMIT 3;