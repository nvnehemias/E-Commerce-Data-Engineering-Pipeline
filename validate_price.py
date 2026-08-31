def validate_price(value, column_name):
    try:
        price = float(value.get(column_name))
        if price < 0:
            return False 
        else:
            return True
    except ValueError:
        return False
