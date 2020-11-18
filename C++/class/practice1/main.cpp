#include <string>
#include <iostream>

using namespace std;

class daytime {
    int milliseconds;
    int seconds;
    int minutes;
    int hours;
    int days;
public:
    daytime(int, int, int, int, int);
};

daytime::daytime(int milli = 0, int sec = 0, int min = 0, int hour = 0, int day = 0){
    milliseconds = milli;
    seconds = sec;
    minutes = min;
    hours = hour;
    days = day;
}

int main(){
    daytime dt1(0, 0, 0, 12, 1);

}
