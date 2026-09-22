INSERT INTO orders (
    order_id,
    customer_id,
    product,
    price,
    quantity,
    order_total
)
SELECT 
    order_id,
    customer_id,
    product,
    CAST(price AS numeric) AS price,
    CAST(quantity AS int) AS quantity,
    ROUND(
        CAST(price AS numeric) * CAST(quantity AS int),
        2
    ) AS order_total
FROM stg_orders
WHERE customer_id IS NOT NULL
  AND price >= 0
  AND quantity >= 1
ON CONFLICT (order_id) DO NOTHING;