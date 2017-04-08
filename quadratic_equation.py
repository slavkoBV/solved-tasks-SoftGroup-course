#!/usr/bin/env python3

import math
import cmath


def quadratic(a, b, c):
    # Roots of equation
    x1 = None
    x2 = None
    if a == 0:
        print('Некоректні вхідні дані. Коефіцієнт a не повинен дорівнювати нулю')
    else:
        discriminant = (b ** 2) - (4 * a * c)
        if discriminant == 0:
            x1 = -(b / (2 * a))
            result = "x\N{SUBSCRIPT ONE},\N{SUBSCRIPT TWO} = {0}".format(x1)
        else:
            if discriminant > 0:
                root = math.sqrt(discriminant)
            else:
                root = cmath.sqrt(discriminant)
            x1 = (-b + root) / (2 * a)
            x2 = (-b - root) / (2 * a)
            result = "x\N{SUBSCRIPT ONE} = {0}, x\N{SUBSCRIPT TWO} = {1}".format(x1, x2)
        print(result)


if __name__ == '__main__':
    quadratic(0, 1, 3)
    quadratic(2, 0, 0)
    quadratic(2, 2, 0)
    quadratic(2, 10, 2)
    quadratic(2, 1, 3)
