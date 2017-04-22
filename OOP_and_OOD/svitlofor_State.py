import time
import enum


class SysClock:
    @staticmethod
    def get_current_time():
        return round(time.time() * 1000)

    def get_passed_time(self, start_time):
        return self.get_current_time() - start_time

    def is_time_passed(self, start_time, time_interval):
        passed_time = self.get_passed_time(start_time)
        if passed_time >= time_interval:
            return True
        return False


class Color(enum.Enum):
    RED = 0
    REDYELLOW = 1
    GREEN = 2
    BLINKGREEN = 3
    YELLOW = 4


class TrafficLight:
    def __init__(self):
        self.color = Color.RED
        sys_clock = SysClock()
        self.start_time = sys_clock.get_current_time()

    def event_handler(self, time_interval):
        if self.color == Color.RED and clock.is_time_passed(self.start_time, time_interval):
            self.color = Color.REDYELLOW
            print(self.color)
            self.start_time = clock.get_current_time()
        if self.color == Color.REDYELLOW and clock.is_time_passed(self.start_time, time_interval):
            self.color = Color.GREEN
            print(self.color)
            self.start_time = clock.get_current_time()
        if self.color == Color.GREEN and clock.is_time_passed(self.start_time, time_interval):
            self.color = Color.BLINKGREEN
            print(self.color)
            self.start_time = clock.get_current_time()
        if self.color == Color.BLINKGREEN and clock.is_time_passed(self.start_time, time_interval):
            self.color = Color.YELLOW
            print(self.color)
            self.start_time = clock.get_current_time()
        if self.color == Color.YELLOW and clock.is_time_passed(self.start_time, time_interval):
            self.color = Color.RED
            print(self.color)
            self.start_time = clock.get_current_time()


if __name__ == '__main__':
    clock = SysClock()
    interval = 1000
    svitlofor = TrafficLight()
    while True:
        svitlofor.event_handler(interval)
