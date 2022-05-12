#include <bits/stdc++.h>
#define rep(i, n) for(int i=0; i < (n); i++)
using namespace std;
using ll = long long;

int main() {
    int h, w, r, c, cnt = 0;
    cin >> h >> w >> r >> c;
    if (r > 1) cnt++;
    if (r < h) cnt++;
    if (c > 1) cnt++;
    if (c < w) cnt++;
    cout << cnt << endl;
}