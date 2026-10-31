# HR_DEPARTMENT, HR_EMPLOYEES, HR_GRADE 테이블을 이용해 사원별 성과금 정보를 조회하려합니다.
# 평가 점수별 등급과 등급에 따른 성과금 정보가 아래와 같을 때,
# 사번, 성명, 평가 등급, 성과금을 조회하는 SQL문을 작성해주세요.
SELECT
      e.emp_no
    , e.emp_name
    , CASE 
        WHEN AVG(g.score) >= 96 THEN 'S'
        WHEN AVG(g.score) >= 90 THEN 'A'
        WHEN AVG(g.score) >= 80 THEN 'B'
        ELSE 'C'
    END AS 'GRADE'
    , CASE
        WHEN AVG(g.score) >= 96 THEN e.sal * 0.2
        WHEN AVG(g.score) >= 90 THEN e.sal * 0.15
        WHEN AVG(g.score) >= 80 THEN e.sal * 0.1
        ELSE 0
    END AS 'BONUS'
FROM hr_employees e
JOIN hr_grade g
  ON e.emp_no = g.emp_no
GROUP BY e.emp_no
ORDER BY e.emp_no ASC;