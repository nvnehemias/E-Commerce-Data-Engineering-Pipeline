def validate_quantity(value, column_name):

    try:
        quantity = float(value.get(column_name))
        if quantity <= 0:
            return False 
        else:
            return True
    except ValueError:
        return False
