def validate_customer(value, column_name_1):

    if value.get(column_name_1) is None:
        return False
    else:
        return True
