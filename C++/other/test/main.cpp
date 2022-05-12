#include <bits/stdc++.h>
#define rep(i, n) for(int i=0; i < (n); i++)
using namespace std;
using ll = long long;

int main() {
    vector<int> a(5);
    a[0] = 5;
    a[1] = 3;
    a[2] = 2;
    a[3] = 1;
    a[4] = 4;
    rep(i, 5) cout << a[i] << " ";
    cout << endl;
    auto it = find(a.begin(), a.end(), 3);
    cout << *it << " " << it - a.begin() + 1 << endl;
}