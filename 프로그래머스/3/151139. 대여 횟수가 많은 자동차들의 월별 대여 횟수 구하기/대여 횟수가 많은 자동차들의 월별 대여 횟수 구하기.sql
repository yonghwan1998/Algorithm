-- 코드를 입력하세요
SELECT
      MONTH(start_date) AS 'month'
    , car_id
    , COUNT(*) AS 'records'
FROM car_rental_company_rental_history
WHERE car_id IN (
    SELECT
        car_id
    FROM car_rental_company_rental_history
    WHERE start_date BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY car_id
    HAVING COUNT(*) >= 5
)
  AND start_date BETWEEN '2022-08-01' AND '2022-10-31'
GROUP BY MONTH(start_date), car_id
ORDER BY MONTH(start_date) ASC, car_id DESC;