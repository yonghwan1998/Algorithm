-- 코드를 입력하세요
SELECT
      b.category AS 'CATEGORY'
    , SUM(bs.sales) AS 'TOTAL_SALES'
FROM book b
INNER JOIN book_sales bs
ON b.book_id = bs.book_id
WHERE bs.sales_date LIKE '2022-01%'
GROUP BY b.category
ORDER BY b.category ASC;