insert into orders (
    order_id
    , customer_id
    , product
    , price
    , quantity
    , order_total
)

select
    order_id
    , customer_id
    , product
    , cast(price as numeric) as price
    , cast(quantity as int) as quantity
    , ROUND(
        cast(price as numeric) * cast(quantity as int),
        2
    ) as order_total
from stg_orders
where 1=1
    and customer_id is not null 
    and price >= 0
    and quantity >= 1
on conflict (order_id) do nothing
;