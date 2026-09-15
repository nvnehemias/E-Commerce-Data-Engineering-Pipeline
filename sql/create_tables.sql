
create table if not exists stg_orders (

    order_id int primary key,
    customer_id int,
    product varchar(100),
    price varchar(100),
    quantity varchar(100)

);


create table if not exists orders (

    order_id int primary key,
    customer_id int,
    product varchar(100),
    price numeric(10,2),
    quantity int,
    order_total numeric(10,2)

);
