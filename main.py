from validate_price import validate_price
from validate_quantity import validate_quantity
from validate_customer import validate_customer
from transform_order import transform_order
from pathlib import Path
import logging
import json 
import os 

def convert_order(dataset):

    # Assigning Lists
    clean_list = []
    new_columns = ["order_id","customer_id","product","price","quantity","order_total"]

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
        price = float(i["price"])

        if not validate_quantity(i,"quantity"):
            invalid_quantity += 1 
            continue 
        quantity = int(i["quantity"])

        
        new_values = [order_id, i["customer_id"], i["product"], price, quantity, round(price*quantity,2)]
        clean_list.append(transform_order(new_columns,new_values))
        
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


# Obtaining file path
base_dir = Path(__file__).parent
raw_data_path = base_dir / "data" / "raw"
proc_data_path = base_dir / "data" / "processed" / "cleaned_"

# Finding all files with .json 
json_files = list(raw_data_path.glob("*.json"))

# Looping through all files and loading data
for file_path in json_files:
    print(f"Loading file: {file_path.name}")
    with open(file_path,"r",encoding = 'utf-8') as file:
        data = json.load(file)

        cleaned_orders, report = convert_order(data)
        print(report)
        
    with open(f"{proc_data_path}{file_path.name}","w", encoding = "utf-8") as file:
        json.dump(cleaned_orders, file, indent = 4)

