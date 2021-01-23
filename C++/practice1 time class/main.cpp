// don't use alt + shift + f
#include <string>
#include <iostream>
#include <cstdio>

using namespace std;

const int GET = 0;
const int ADD = 1;
const int DAY   = 0b000010;
const int HOUR  = 0b000100;
const int MIN   = 0b001000;
const int SEC   = 0b010000;
const int MILLI = 0b100000;
const int ALL   = 0b111110;

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
    void get_day_time(int[]) const;
    string get_str() const; // 続きはここから
    void add_day(int);
    void add_hour(int);
    void add_min(int);
    void add_sec(int);
    void add_milli(int);
    void add_time(int, int, int, int, int);
};

void init(daytime *);

int menu();

int menu_selected_0();

int menu_selected_1();

daytime::daytime(int day, int hour = 0, int min = 0,
                 int sec = 0, int milli = 0)
{
    this->days         = day;
    this->hours        = hour;
    this->minutes      = min;
    this->seconds      = sec;
    this->milliseconds = milli;
}

daytime::daytime()
{
    this->days = 0; this->hours = 0; this->minutes = 0;
    this->seconds = 0; this->milliseconds = 0;
}

void daytime::get_day_time(int receiver[]) const
{
    int *daytime = receiver;
    int array[5] = {this->days, this->hours, this->minutes,
                    this->seconds, this->milliseconds};
    for (int i = 0; i < 5; i++)
    {
        *daytime = array[i];
        daytime++;
    }
}

string daytime::get_str() const
{
    return to_string(this->days) + ':' + to_string(this->hours) + ':' + to_string(this->minutes) + ':' + to_string(this->seconds) + ':' + to_string(this->milliseconds);
}

void daytime::add_day(int day)
{
    this->days += day;
}

void daytime::add_hour(int hour)
{
    this->hours += hour;
    if (this->hours <= 24)
    {
        this->days += this->hours / 24;
        this->hours %= 24;
    }
}

void daytime::add_min(int min)
{
    this->minutes += min;
    if (this->minutes >= 60)
    {
        this->hours += this->minutes / 60;
        this->minutes %= 60;
    }
}

void daytime::add_sec(int sec)
{
    this->seconds += sec;
    if (this->seconds >= 60)
    {
        this->minutes += this->seconds / 60;
        this->seconds %= 60;
    }
}

void daytime::add_milli(int milli)
{
    this->milliseconds += milli;
    if (this->milliseconds >= 1000)
    {
        this->seconds += this->milliseconds / 1000;
        this->milliseconds %= 1000;
    }
}

void daytime::add_time(int day, int hour = 0,int min = 0,
                       int sec = 0,int milli = 0)
{
    this->add_day(day);
    this->add_hour(hour);
    this->add_min(min);
    this->add_sec(sec);
    this->add_milli(milli);
}

void init(daytime *to) // for intiate
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
    *to = from;
}

int menu()
{
    int ans = 0;
    int bin = 0;
    while (ans < 0 && ans > 1)
    {
        cout << "two choice [0]get or [1]add > ";
        cin >> ans;
        cin.clear();
        cin.ignore();
    }
    switch (ans)
    {
    case GET:
        menu_selected_0();
        break;

    case ADD:
        menu_selected_1();
        break;

    default:
        break;
    }
}

int menu_selected_0()
{
    int ans = 0;
    cout << "what type of time do you want ?\n\
[0]DAY  [1]HOUR [2]MINUTES [3]SECOND [4]MILLISECOND\n\
 > ";
    cin >> ans;
    int bin = 0;
    switch (ans)
    {
    case 0:
        bin += DAY;
        break;

    case 1:
        bin += HOUR;
        break;

    case 2:
        bin += MIN;
        break;

    case 3:
        bin += SEC;
        break;

    case 4:
        bin += MILLI;
        break;

    case 5:
        bin += ALL;

    default:
        break;
    }
    return bin;
}

int main()
{
    daytime time;
    init(&time);
    int arr[5];
    time.get_day_time(arr);
    for (int i = 0; i < 5; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl << time.get_str();
    return 0;
}
