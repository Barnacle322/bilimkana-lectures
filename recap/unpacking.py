a, b, c = 5, 6, 2_908_463


student_list = [
    ("Арстан", 19, "male"),
    ("Гука", 15, "female"),
    ("Адалия", 16, "female"),
    ("Эржан", 16, "male", "работает"),
    ("Каныкей", 16, "female"),
    ("Диля", 16, "male")
]


for name, age, gender, *args in student_list:
    print(f'Имя: {name}, возраст: {age}, пол: {gender}')
    print(args) # Распечатает что-то если было переданно больше чем 3 параметра



def printer(name: str, age: int, gender: str, *args, **kwargs):
    print(name) # -> Арстан
    print(age) # -> 19
    print(gender) # -> male
    print(args) # -> ('учитель')
    print(kwargs) # -> {'job': 'учитель'}


printer("Арстан", 19, "male", "работает", job="учитель")