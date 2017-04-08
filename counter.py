def some_func(a, b):
    some_func.counter += 1  # Static variable Counter remember number of some_func() calls
    return a + b


some_func.counter = 0
print(some_func(1, 3))
print('Call #',some_func.counter)
print(some_func(2, 4))
print('Call #', some_func.counter)
