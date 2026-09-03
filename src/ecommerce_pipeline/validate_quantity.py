def validate_quantity(value, column_name):

    try:
        quantity = int(value.get(column_name))
        if quantity <= 0:
            return False 
        else:
            return True
    except (ValueError,TypeError):
        return False
