class Observed:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)


# Model #################################################################

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_other(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Triangle(Observed):
    def __init__(self, p1, p2, p3):
        super().__init__()
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def update_points(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.notify_observers()

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
        return round((self.a + self.b + self.c), 2)

    @property
    def area(self):
        p = self.perimeter / 2
        return round(((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5), 2)


# Controller #######################################

class Controller:
    def __init__(self):
        p1 = Point(0, 0)
        p2 = Point(0, 0)
        p3 = Point(0, 0)
        self.model = Triangle(p1, p2, p3)
        self.view = View()
        self.model.add_observer(self.view)

    def run(self):
        coord = self.view.inp()
        if coord is not None:
            self.model.update_points(Point(*coord[0]), Point(*coord[1]), Point(*coord[2]))


# View ###########################################

class View:
    def __init__(self):
        self.data = None
        self.points = None

    def inp(self):
        self.points = []
        try:
            for i in range(3):
                self.data = list(map(float, input('Input coordinates of {0} point: x, y: '.format(i + 1)).split(',')))
                self.points.append(self.data)
            return self.points
        except ValueError:
            print('Invalid input data')

    @staticmethod
    def update(model):
        if model.perimeter and model.area:
            print('Perimeter:', model.perimeter)
            print('Area:', model.area)
        else:
            print('Triangle does not exist')


##############################################

def main():
    contr = Controller()
    contr.run()


if __name__ == '__main__':
    main()
