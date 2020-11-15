import typing


class second:
    def __init__(self, second: int):
        self.second = second

    def __add__(self, other):
        return second(self.second + other.second)

    def __sub__(self, other):
        return second(self.second - other.second)

    def __mul__(self, other):
        return second(self.second * other.second)

    def __truediv__(self, other):
        return second(self.second / other.second)

    def __floordiv__(self, other):
        return second(self.second // other.second)

    def __mod__(self, other):
        return second(self.second % other.second)

    def __pow__(self, other):
        return second(self.second ** other.second)

    def __str__(self):
        return str(self.second)

    def add_sec(self, second: int):
        self.second += second


class minute(second):
    def __init__(self, minute: int):
        second.__init__(self, minute * 60)
        self.minute = minute

    def add_min(self, minute: int):
        self.add_sec(minute*60)
        self.minute += minute


if __name__ == '__main__':
    time = minute(3)
    print(time)
    time.add_sec(34)
    print(time)
    time.add_min(3)
    print(time)
    print(second(18) + second(45))
    print(second(18) + minute(5))
    print(minute(2) + second(10))
