class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_other(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    @property
    def a(self):
        return self.p1.distance_to_other(self.p2)

    @property
    def b(self):
        return self.p2.distance_to_other(self.p3)

    @property
    def c(self):
        return self.p1.distance_to_other(self.p3)

    def is_exist(self):
        return True if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a) else \
            False

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


if __name__ == '__main__':
    point1 = Point(0, 5)
    point2 = Point(1, 20)
    point3 = Point(5, 8)
    t = Triangle(point1, point2, point3)
    print(t.a, t.b, t.c)
    print('Периметр:', t.perimeter)
    print('Площа: ', t.area)
    print('Трикутник існує - ', t.is_exist())
