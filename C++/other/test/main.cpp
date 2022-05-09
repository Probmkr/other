#include<string>
#include<iostream>
#define rep(i, n) for(int i=0; i < (n); i++)
using namespace std;
// using ll = long long;

int main() {
    int *a = nullptr;
    int b = 5;
    a = &b;
    cout << (bool)a << endl;
}
