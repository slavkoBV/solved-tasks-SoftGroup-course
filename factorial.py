import functools


def factorial(number):
    factor = 1
    if number < 0:
        return None
    for i in range(1, number + 1):
        factor *= i
    return factor


def factorial_2var(number):
    if number < 0:
        return None
    return number * factorial_2var(number - 1) if number > 0 else 1  # recursion


def factorial_3v(number):
    if number < 0:
        return None
    return functools.reduce(lambda x, y: x * y, range(1, number+1)) if number > 0 else 1


print(factorial(0))
print(factorial_2var(0))
print(factorial_3v(0))
