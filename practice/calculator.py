"""
Создайте функцию, которая принимает в себя
сторону квадрата и возвращает его периметр.
"""


def perimeter(side: int) -> int:
    perimeter = side * 4
    return perimeter


"""
Создайте функцию, которая принимает в себя
радиус круга и возвращает его площадь
"""

import math


def area(radius: int) -> int:
    area = math.pi * radius**2
    return area


# print(area(5)) # => 78.53981633974483

"""
Создайте функцию, которая принимает в себя
длину и ширину прямоугольника и возвращает его площадь
"""


def area_rectangle(length: int, width: int) -> int:
    area = length * width
    return area
