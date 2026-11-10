SELECT
      y.year AS 'YEAR'
    , y.max_size_of_colony - e.size_of_colony AS 'YEAR_DEV'
    , e.id
FROM ecoli_data e
JOIN (
    SELECT
          YEAR(differentiation_date) AS 'year'
        , MAX(size_of_colony) 'max_size_of_colony'
    FROM ecoli_data
    GROUP BY YEAR(differentiation_date)
) y
  ON YEAR(e.differentiation_date) = y.year
ORDER BY YEAR ASC, YEAR_DEV ASC;