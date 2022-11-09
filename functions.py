# ФУНКЦИИ

def doubler(number: int) -> int:
    new_number = number * 2
    return new_number


def tripler(number: int) -> int:
    new_number = number * 3
    return new_number


def quadrupler(number: int) -> int:
    new_number = number * 4
    return new_number


def calculate(number: int, coefficient: int) -> int:
    new_number = (number * coefficient / 2) + 25 
    return new_number


print(calculate(5, 6))
print(((5 * 6)/2) + 25)