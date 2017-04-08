#!/usr/bin/env python3


def is_prime(number):
    if number > 1:
        i = 2
        while i < number:
            if number % i == 0:
                break
            i += 1
        else:
            return True
        return False
    else:
        return False


if __name__ == '__main__':
    for num in range(0, 100):
        if is_prime(num):
            print(num, end=' ')
