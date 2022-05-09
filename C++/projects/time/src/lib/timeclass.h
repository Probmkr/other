#ifndef TIMECLASS_H
#define TIMECLASS_H

class mytime
{
private:
    int secs;
public:
    mytime(int secs);
    int get();
    void set(int secs);
    void print();
};


#endif