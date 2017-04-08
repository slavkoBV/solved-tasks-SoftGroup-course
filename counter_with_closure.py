def some_func(x):
    def counter():
        x[0] += 1
        print(x[0])
    return counter

x = [0]
a = some_func(x)
print(a)
print(a())
print(a())
