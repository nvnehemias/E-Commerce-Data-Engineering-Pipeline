"""
order1 = {
    "order_id": "1001",
    "customer_id": "C001"
}

order2 = {
    "order_id": "1003",
    "customer_id": None
}

"""

def validate_customer(value, column_name_1):

    if value.get(column_name_1) is None:
        return False
    else:
        return True

"""
print(validate_customer(order1, "customer_id"))
print(validate_customer(order2, "customer_id"))

"""