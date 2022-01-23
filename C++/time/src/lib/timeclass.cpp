#include "timeclass.h"
#include <iostream>
#include <string>

using namespace std;

mytime::mytime(int secs)
{
    this->secs = secs;
}

int mytime::get()
{
    return this->secs;
}

void mytime::set(int secs)
{
    this->secs = secs;
}

void mytime::print()
{
    cout << this->secs << "secs" << endl;
}