SELECT
      p.id
    , p.name
    , p.host_id
FROM places p
WHERE host_id IN (
    SELECT
        host_id
    from places
    GROUP BY host_id
    HAVING COUNT(*) >= 2
)
ORDER BY id ASC;