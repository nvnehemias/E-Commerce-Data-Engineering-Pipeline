insert into orders (

    order_id
    , customer_id
    , product
    , price
    , quantity

)

values (
    %s
    ,%s 
    ,%s 
    ,%s 
    ,%s 
)

on conflict (order_id) do nothing
;