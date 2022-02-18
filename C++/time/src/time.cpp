#include <iostream>
#include <string>
#include "../include/include.h"

using namespace std;

int main(int argc, char *argv[])
{
    mytime time1(100);
    time1.print();
    cout << "Now, time1's value is " << time1.get() << endl;

    return 0;
}