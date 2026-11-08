SELECT
      id
    , CASE
        WHEN PERCENT_RANK() OVER (ORDER BY size_of_colony DESC) * 100 <= 25 THEN 'CRITICAL'
        WHEN PERCENT_RANK() OVER (ORDER BY size_of_colony DESC) * 100 <= 50 THEN 'HIGH'
        WHEN PERCENT_RANK() OVER (ORDER BY size_of_colony DESC) * 100 <= 75 THEN 'MEDIUM'
        WHEN PERCENT_RANK() OVER (ORDER BY size_of_colony DESC) * 100 <= 100 THEN 'LOW'
    END AS 'COLONY_NAME'
FROM ecoli_data
ORDER BY id ASC;