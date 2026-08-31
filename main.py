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

        # adding 1 to every itteration of for loop
        total_orders += 1

        if i['order_id'] in seen:
            duplicate_orders += 1 
            continue 
        seen.add(i['order_id'])
            
        
        
        if i['customer_id'] is None:

            # adding 1 to every itteration when a customer is missing
            missing_customers += 1
            print(f"{i['order_id']} is missing a customer")
            continue
        
        else:
            print(f"{i['order_id']} has a customer")

        

        try:
            price = float(i["price"])
            print(f"Price: {price}")
            if price < 0:
                invalid_price += 1 
                continue
        except ValueError:
            invalid_price += 1
            continue 

        try:
            quantity = int(i["quantity"])
            print(f"Quantity: {quantity}")
            if quantity <= 0:
                invalid_quantity += 1 
                continue
        except ValueError:
            invalid_quantity += 1 
            continue 

            
            
                        

        data_dictionary = {

            "order_id": i["order_id"],
            "customer_id": i["customer_id"],
            "product": i["product"],
            "price": price,
            "quantity": quantity,
            "order_total": price * quantity

        }
        clean_list.append(data_dictionary)

        # adding 1 to every sucessfully processed order
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
        
