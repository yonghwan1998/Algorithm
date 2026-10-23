SELECT
      SUM(g.score) AS 'SCORE'
    , e.emp_no
    , e.emp_name
    , e.position
    , e.email
FROM hr_employees e
JOIN hr_grade g
  ON e.emp_no = g.emp_no
WHERE g.year = 2022
GROUP BY e.emp_no
ORDER BY SCORE DESC
LIMIT 1;