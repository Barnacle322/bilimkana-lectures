# Классы

## Задание

Создайте класс пользователя сайта. Подумайте сами какие параметры и методы должны быть.

## Начало кода

```python
class User:
    ...
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

Классы

```python
class Animal:
    name: str
    legs: int
    color: str

    def __init__(self, name, legs, color):
        self.name = name
        self.legs = legs
        self.color = color

    def __repr__(self):
        return self.name
```