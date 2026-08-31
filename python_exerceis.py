def convert_order(dataset):

    # Empty clean list
    clean_list = []

    # Counters
    total_orders = 0
    successful_orders = 0 
    missing_customers = 0 
    invalid_price= 0 
    invalid_quantity = 0 
    
    for i in dataset:

        # adding 1 to every itteration of for loop
        total_orders += 1

        if i['customer_id'] is None:

            # adding 1 to every itteration when a customer is missing
            missing_customers += 1
            print(f "{i['order_id']} is missing a customer")
            continue
        
        else:

            # adding 1 to every order that has a a customer 
            successful_orders += 1 
            print(f"{i['order_id']} has a customer")

        try:
            
            price = float(i["price"])
            quantity = int(i["quantity"])
            print(f"Price: {price}")
            print(f"Quantity: {quantity}")
            

        except ValueError:
            print("Something failed")
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
    return clean_list   
        
