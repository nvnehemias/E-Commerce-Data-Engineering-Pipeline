def convert_order(dataset):
    clean_list = []
    for i in dataset:

        if i['customer_id'] is None:
                    print(f'{i['order_id']} is missing a customer')
        else:
            print(f'{i['order_id']} has a customer')

        try:
            price = float(i["price"])
            quantity = int(i["quantity"])
            print(f"Price: {price}")
            print(f"Quantity: {quantity}")
            

        except ValueError:
            print("Something failed")
            continue

        data_dictionary = {

            "order_id": i["order_id"]
            "customer_id": i["customer_id"]
            "product": i["product"]
            "price": price
            "quantity": quantity
            "order_total": price * quantity

        }
        clean_list.append(data_dictionary)
    return clean_list   
        
