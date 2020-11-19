// don't use alt + shift + f
#include <string>
#include <iostream>

using namespace std;

const int GET = 0;
const int ADD = 1;
const int DAY   = 0b000010;
const int HOUR  = 0b000100;
const int MIN   = 0b001000;
const int SEC   = 0b010000;
const int MILLI = 0b100000;

void init();

int menu();

class daytime
{
    int days;
    int hours;
    int minutes;
    int seconds;
    int milliseconds;

public:
    daytime(int, int, int, int, int);
    daytime();
    void get_day_time(int[]);
    void add_day(int);
    void add_hours(int);
    void add_time(int, int, int, int, int);
};

daytime::daytime(int day, int hour = 0, int min = 0,
                 int sec = 0, int milli = 0)
{
    days = day;
    hours = hour;
    minutes = min;
    seconds = sec;
    milliseconds = milli;
}

daytime::daytime()
{
    days = 0; hours = 0; minutes = 0;
    seconds = 0; milliseconds = 0;
}

void daytime::get_day_time(int receiver[])
{
    int *daytime = receiver;
    int array[5] = {days, hours, minutes, seconds, milliseconds};
    for (int i = 0; i < 5; i++)
    {
        *daytime = array[i];
        daytime++;
    }
}

void daytime::add_day(int day)
{
    days += day;
}

void daytime::add_hours(int hour)
{
    hours += hour;
    if (hours <= 24)
    {
        days += hours / 24;
        hours = hours % 24;
    }
}

void daytime::add_time(int day, int hour = 0,int min = 0,
                       int sec = 0,int milli = 0)
{
    
}

void init(daytime &to)
{
    string word_arr[5] = {"day", "hour", "minute", "second", "millisecond"};
    int time_arr[5];
    for (int i = 0; i < 5; i++)
    {
        cout << "enter " << word_arr[i] << " > ";
        cin >> time_arr[i];
        cin.clear();
        cin.ignore();
    }
    daytime from(time_arr[0], time_arr[1], time_arr[2], time_arr[3], time_arr[4]);
}

int menu()
{
    cout << "two choice [1]get or [2]add";
}

int main()
{
    daytime time();
    return 0;
}
