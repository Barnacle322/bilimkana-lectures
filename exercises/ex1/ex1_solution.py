# Развернутое решение
def calculator(a: int, b: int) -> int:
    if a * b >= 1000:
        return a + b
    else:
        return a * b


# Короткое решение
def calculator(a: int, b: int) -> int:
    return a + b if a * b >= 1000 else a * b


print(calculator(30, 40))  # -> 70
print(calculator(30, 20))  # -> 600
