"""
Напишите функцию, которая принимает в себя строку 
и возвращает ее в обратном порядке

Но если строка содержит букву 'a', то возвращаемая строка
должна содержать только символы до буквы 'a'
"""


def reverse_string(string: str) -> str:
    if "a" in string:
        formatted = string.split("a")  # ['t','es','t1']
        return formatted[0]
    else:
        reverse = string[::-1]
        return reverse


print(reverse_string("taesat1"))  # => t
print(reverse_string("Hello, World!"))  # => !dlroW ,olleH
