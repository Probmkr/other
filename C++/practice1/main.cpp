#include <string>
#include <iostream>

using namespace std;

class daytime
{
    int milliseconds;
    int seconds;
    int minutes;
    int hours;
    int days;

public:
    daytime(int, int, int, int, int);
    void get_day_time(int*);
};

daytime::daytime(int milli, int sec = 0, int min = 0, int hour = 0, int day = 0)
{
    milliseconds = milli;
    seconds = sec;
    minutes = min;
    hours = hour;
    days = day;
}

void daytime::get_day_time(int *daytime)
{
    int array[5] = {milliseconds, seconds, minutes, hours, days};
    for (int i = 0; i < 5; i++){
        *daytime = array[i];
        daytime++;
    }
}

int main()
{
    daytime dt1(0, 0, 0, 12, 1);
    int a[5];
    dt1.get_day_time(a);
    cout << a[1] << ' ' << a[4] << endl;
}
