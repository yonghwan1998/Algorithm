SELECT
    DISTINCT c.car_id
FROM car_rental_company_car c
JOIN car_rental_company_rental_history rh
  ON c.car_id = rh.car_id
WHERE c.car_type = '세단'
  AND rh.start_date LIKE '2022-10%'
ORDER BY c.car_id DESC;