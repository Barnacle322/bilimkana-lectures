# Развернутое решение
def add_to_dict(key, value, dictionary):
    if key in dictionary.keys():
        return dictionary[key]
    else:
        dictionary[key] = value
        return dictionary


my_dict = {"Apple": "iPhone", "Samsung": "Galaxy"}
add_to_dict("Xiaomi", "Mi", my_dict)

# Короткое решение
def add_to_dict(key, value, dictionary):
    return dictionary.setdefault(key, value)


my_dict = {"Apple": "iPhone", "Samsung": "Galaxy"}
add_to_dict("Xiaomi", "Mi", my_dict)
add_to_dict("Xiaomi", "Something else", my_dict)
