#include <iostream>

using namespace std;

int main()
{
    int arr[3] = {2, 1, 3};
    int *p = arr;
    for (int i = 0;i<7;i++)
    {
        *p = i;
        p++;
    }
    for (int i = 0;i<3;i++)
    {
        cout << arr[i] << endl;
    }
}
