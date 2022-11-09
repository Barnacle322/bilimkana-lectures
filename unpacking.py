a, b, c = 5, 6, 2_908_463


student_list = [
    ("Арстан", 19, "male"),
    ("Гука", 15, "female"),
    ("Адалия", 16, "female"),
    ("Эржан", 16, "male", "gay", "альтушка"),
    ("Каныкей", 15, "female"),
    ("Диля", 16, "male")
]


# for name, age, gender, *args in student_list:
#     print(f'Имя: {name}, возраст: {age}, пол: {gender}')
#     print(args)



def printer(name: str, age: int, gender: str, *args, **kwargs):
    print(name)
    print(age)
    print(gender)
    print(args)
    print(kwargs)


printer("Арстан", 19, "Ламинат", "гей", job="adult movie actor", dicksize = "1cm")