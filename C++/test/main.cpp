#include <string>
#include <iostream>

using namespace std;

int test1()
{
    int i = -1;
    cout << "enter number > ";
    cin >> i;
    cout << i << endl;
    cin.clear();
    cin.ignore();
    cin >> i;
    cout << i << endl;
    return 0;
}

void test2(int *num)
{
    *num = 11;
}

int main()
{
    int num = 2;
    test2(&num);
    cout << num << endl;
}
