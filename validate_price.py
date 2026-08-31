"""
valid_order = {
    "price": "899.99"
}

negative_order = {
    "price": "-50.00"
}

bad_order = {
    "price": "invalid"
}
"""

def validate_price(value, column_name):
    try:
        price = float(value.get(column_name))
        if price < 0:
            return False 
        else:
            True
    except ValueError:
        return False
    return True

"""
print(validate_price(valid_order,"price"))
print(validate_price(negative_order,"price"))
print(validate_price(bad_order,"price"))
"""