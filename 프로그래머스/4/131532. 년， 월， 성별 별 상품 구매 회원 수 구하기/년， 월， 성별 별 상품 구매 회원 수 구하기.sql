-- 코드를 입력하세요
SELECT
      YEAR(os.sales_date) AS 'YEAR'
    , MONTH(os.sales_date) AS 'MONTH'
    , ui.gender
    , COUNT(DISTINCT os.user_id) AS 'users'
FROM online_sale os
JOIN user_info ui
ON os.user_id = ui.user_id
WHERE ui.gender IS NOT NULL
GROUP BY YEAR(os.sales_date), MONTH(os.sales_date), ui.gender
ORDER BY YEAR(os.sales_date) ASC, MONTH(os.sales_date) ASC, ui.gender ASC;