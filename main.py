from validate_price import validate_price
from validate_quantity import validate_quantity
from validate_customer import validate_customer

def convert_order(dataset):

    # Empty clean list
    clean_list = []

    # Counters
    total_orders = 0
    successful_orders = 0 
    missing_customers = 0 
    invalid_price= 0 
    invalid_quantity = 0 
    duplicate_orders = 0

    seen = set() 
    for i in dataset:

        total_orders += 1
        
        order_id = i.get("order_id")
        if order_id in seen:
            duplicate_orders += 1 
            continue 
        seen.add(order_id)
        
        if not validate_customer(i,"customer_id"):
            missing_customers += 1 
            continue

        if not validate_price(i,"price"):
            invalid_price += 1 
            continue
        elif validate_price(i,"price"):
            price = float(i["price"])

        if not validate_quantity(i,"quantity"):
            invalid_quantity += 1 
            continue 
        elif validate_quantity(i,"quantity"):
            quantity = int(i["quantity"])
        
        data_dictionary = {

            "order_id": order_id,
            "customer_id": i["customer_id"],
            "product": i["product"],
            "price": price,
            "quantity": quantity,
            "order_total": round(price * quantity,2)

        }

        clean_list.append(data_dictionary)
        successful_orders += 1 
    

    quality_report = {

        "total_orders": total_orders,
        "successful_orders": successful_orders, 
        "missing_customers": missing_customers, 
        "invalid_price": invalid_price,
        "invalid_quantity": invalid_quantity,
        "duplicate_orders": duplicate_orders
    }


    return clean_list, quality_report