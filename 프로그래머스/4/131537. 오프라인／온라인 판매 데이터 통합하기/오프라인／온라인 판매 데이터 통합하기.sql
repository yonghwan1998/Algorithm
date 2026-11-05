SELECT
      sub.sales_date
    , sub.product_id
    , sub.user_id
    , sub.sales_amount
FROM (
    SELECT
          sales_date    AS 'SALES_DATE'
        , product_id    AS 'PRODUCT_ID'
        , user_id       AS 'USER_ID'
        , sales_amount  AS 'SALES_AMOUNT'
    FROM online_sale 

    UNION ALL

    SELECT
          sales_date    AS 'SALES_DATE'
        , product_id    AS 'PRODUCT_ID'
        , NULL          AS 'USER_ID'
        , sales_amount  AS 'SALES_AMOUNT'
    FROM offline_sale
) sub
WHERE sub.sales_date LIKE '2022-03-%'
ORDER BY sub.sales_date ASC, sub.product_id ASC, sub.user_id ASC;