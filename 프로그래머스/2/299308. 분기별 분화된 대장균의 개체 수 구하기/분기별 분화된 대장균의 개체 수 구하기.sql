SELECT
      CONCAT(QUARTER(differentiation_date), 'Q') AS 'QUARTER'
    , COUNT(id) AS 'ECOLI_COUNT'
FROM ecoli_data
GROUP BY QUARTER(differentiation_date)
ORDER BY QUARTER ASC;