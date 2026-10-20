SELECT
    COUNT(*) AS 'FISH_COUNT'
FROM fish_info i
JOIN fish_name_info ni
  ON i.fish_type = ni.fish_type
WHERE ni.fish_name IN ('BASS', 'SNAPPER');