# Улучшенный словарь

## Задание

Создайте функцию, которая берет в себя ключ и значение, и добавляет их в словарь. Если ключ уже существует, то функция должна возвращать значение этого ключа.

## Примеры
```python
add_to_dict("a", 1, {}) # Добавляем ключ "a" со значением 1 в пустой словарь
add_to_dict("a", 1, {"a": 3}) # Добавляем ключ "a" со значением 1 в словарь {"a": 3}
```

## Начало кода

```python
from typing import Any, Union

def add_to_dict(key: Any, value: Any, dictionary: dict) -> Union[dict, Any]:
    # Ваш код здесь

my_dict = {"Apple": "iPhone", "Samsung": "Galaxy"}
add_to_dict("Xiaomi", "Mi", my_dict)
```

## Что вам нужно будет

Переменные

```python
my_var = "Hello World"
```

Функции

```python
def my_func(param1: str, param2: int) -> str:
    return param1 + str(param2)
```

Словари

```python
my_dict = {"a": 1, "b": 2}
my_dict["c"] = 3
print(my_dict["a"]) # -> 1
print(my_dict) # -> {"a": 1, "b": 2, "c": 3}
print(my_dict.keys()) # -> ["a", "b", "c"]
```

Условные выражения

```python
if statement == True:
    print("It's true")
elif statement == None:
    print("No idea")
else:
    print("It's false")
```
