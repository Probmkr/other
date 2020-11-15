class second:
    def __init__(self, second):
        self.second = second

    def __add__(self, other: second):
        self.second + other.second

    def __sub__(self, other: second):
        self.second - other.second

    def __mul__(self, other: second):
        self.second * other.second

    def __truediv__(self, other: second):
        self.second / other.second

    def __floordiv__(self, other: second):
        self.second // other.second

    def __mod__(self, other: second):
        self.second % other.second

    def __pow__(self, other: second):
        self.second ** other.second

class minute(second):
    def __init__(self, minute, second):
        second.__init__(self, second)
        self.minute = minute

