# Переменные - Именные ячейки для хранения информации
my_var = 'Hello World'
my_int = 123
my_float = 123.22
my_bool = True

# !!! ТАК ДЕЛАТЬ НЕЛЬЗЯ !!!
# 56sheep = "Hi"
# !var = 123

# КОЛЛЕКЦИИ
# Списки
my_list = ["Адалия", "Гука", "Жанболот"]
# Сеты
my_set = {1,2,3,4,5,6,7,8,9,9}
# Кортежы (Тюплы)
my_tuple = ("3.14, 9.81")
# Словари
my_dict = {"Арстан": 19}
print(my_dict["Арстан"])

# МЕТОДЫ КОЛЛЕКЦИЙ
my_list.append("Элзар")
my_set.add(22)
my_dict["Адалия"] = 16

# СТРОКОВЫЕ МЕТОДЫ
my_str = "привет"
my_name = "Арстан"
new_str = my_str.capitalize()

print(my_str) # => привет
print(new_str) # => Привет

print(my_str + " " + my_name) # Конкатенация