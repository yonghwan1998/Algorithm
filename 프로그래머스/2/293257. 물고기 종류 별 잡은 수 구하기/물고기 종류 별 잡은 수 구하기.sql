SELECT
      COUNT(*) AS 'FISH_COUNT'
    , ni.fish_name AS 'FISH_NAME'
FROM fish_info i
JOIN fish_name_info ni
  ON i.fish_type = ni.fish_type
GROUP BY i.fish_type
ORDER BY FISH_COUNT DESC;