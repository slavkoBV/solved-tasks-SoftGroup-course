#!/usr/bin/env python3

def solve_quadratic():

    import math
    import cmath

    def get_coefficient(message, allow_zero):
        coeff = None
        while coeff is None:
            try:
                coeff = float(input(message))
                if not allow_zero and coeff == 0:
                    print('Коефіцієнт a не повинен дорівнювати нулю')
                    coeff = None
            except ValueError as error:
                print(error)
        return coeff

    print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")
    a = get_coefficient('Input a: ', False)
    b = get_coefficient('Input b: ', True)
    c = get_coefficient('Input c: ', True)

    # Roots of equation
    x1 = None
    x2 = None

    discriminant = (b ** 2) - (4 * a * c)
    if discriminant == 0:
        x1 = -(b / (2 * a))
        result = ("x\N{SUBSCRIPT ONE},\N{SUBSCRIPT TWO} = {0}").format(x1)
    else:
        if discriminant > 0:
            root = math.sqrt(discriminant)
        else:
            root = cmath.sqrt(discriminant)
        x1 = (-b + root) / (2 * a)
        x2 = (-b - root) / (2 * a)

        result = ("x\N{SUBSCRIPT ONE} = {0}, x\N{SUBSCRIPT TWO} = {1}").format(x1, x2)

    print(result)

if __name__ == '__main__':
    solve_quadratic()