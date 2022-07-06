import typing


class second:
    def __init__(self, second: int):
        self._second = second

    def __add__(self, other):
        return second(self._second + other._second)

    def __sub__(self, other):
        return second(self._second - other._second)

    def __mul__(self, other):
        return second(self._second * other._second)

    def __truediv__(self, other):
        return second(self._second / other._second)

    def __floordiv__(self, other):
        return second(self._second // other._second)

    def __mod__(self, other):
        return second(self._second % other._second)

    def __pow__(self, other):
        return second(self._second ** other._second)

    def __lt__(self, other):
        return self._second < other._second

    def __le__(self, other):
        return self._second <= other._second

    def __eq__(self, other):
        return self._second == other._second

    def __ne__(self, other):
        return self._second != other._second

    def __gt__(self, other):
        return self._second > other._second

    def __ge__(self, other):
        return self._second >= other._second

    def __str__(self):
        return str(self._second)

    def add_sec(self, second: int):
        self._second += second


class minute(second):
    def __init__(self, minute: int):
        second.__init__(self, minute * 60)

    def add_min(self, minute: int):
        second.add_sec(self, minute * 60)


class hour(minute):
    def __init__(self, hour: int):
        minute.__init__(self, hour * 60)

    def add_hour(self, hour: int):
        minute.add_min(self, hour * 60)


class time(hour):
    def __init__(self, hours=0, minutes=0, seconds=0):
        self._second = hours * 3600 + minutes * 60 + seconds
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def add_sec(self, seconds):
        hour.add_sec(self, seconds)
        self._seconds += seconds
        if self._seconds >= 60:
            self._minutes += seconds // 60
            self._seconds %= 60

    def add_min(self, minutes):
        hour.add_min(self, minutes)
        self._minutes += minutes
        if self._minutes >= 60:
            self._hours //= 60
            self._minutes += minutes % 60

    def add_hour(self, hours):
        hour.add_hour(self, hours)
        self._hours += hours

    def __str__(self):
        return f'{self._hours:02}:{self._minutes:02}:{self._seconds:02}'

    def get_time(self) -> dict:
        time_dict = {'hour': self._hours,
                     'minute': self._minutes,
                     'second': self._seconds}
        return time_dict

    def get_hms(self, t_type='hms') -> list:
        time_list = []
        if 'h' in t_type:
            time_list.append(self._hours)
        if 'm' in t_type:
            time_list.append(self._minutes)
        if 's' in t_type:
            time_list.append(self._seconds)
        return time_list
    
    def get_all_second(self) -> int:
        return self._second
    
    def set_time(self, hours=0, minutes=0, seconds=0):
        self.__init__(hours, minutes, seconds)


if __name__ == '__main__':
    TIME = time(0, 10, 30)
    print(TIME)
    TIME.add_hour(30)
    print(TIME)
    TIME.add_sec(70)
    print(TIME)
    print(TIME.get_hms('hm'))
    print(TIME.get_hms('sh'))
    print(TIME.get_time())
    print(TIME.get_all_second())
    TIME.set_time(1,10,10)
    print(TIME)
    print(TIME + time(seconds=30))
