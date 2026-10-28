SELECT
    cart_id
FROM (
    SELECT
        DISTINCT cart_id
    FROM cart_products
    WHERE name  = 'Milk'
    UNION ALL
    SELECT
    
        DISTINCT cart_id
    FROM cart_products 
    WHERE name  = 'Yogurt'
) combined_data
GROUP BY combined_data.cart_id
HAVING COUNT(cart_id) >= 2
ORDER BY cart_id ASC;