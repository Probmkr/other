#include <bits/stdc++.h>
#define rep(i, n) for(int i=0; i < (n); i++)
using namespace std;
using ll = long long;

int main() {
    int n, a, b;
    int ii = 0, kk = 0;
    char color[2] = {'.', '#'};
    cin.tie(0);
    cin >> n >> a >> b;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < a; j++) {
            for (int k = 0; k < n; k++) {
                for (int l = 0; l < b; l++) {
                    cout << color[(ii + kk) % 2];
                }
                kk++;
            }
            cout << endl;
            kk = 0;
        }
        ii++;
    }
}