# def transform_order(order, price, quantity, length_dictionary):
def transform_order(list_columns, values):

    new_dictionary = {}

    for i in range(len(values)):
        new_dictionary[list_columns[i]] = values[i]

    return new_dictionary
