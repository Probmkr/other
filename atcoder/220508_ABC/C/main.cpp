#include <bits/stdc++.h>
#define rep(i, n) for(int i=0; i < (n); i++)
using namespace std;
using ll = long long;

int main() {
    cin.tie(0);
    int n, q, xi;
    cin >> n >> q;
    vector<int> a(n);
    rep (i, n) {
        a[i] = i+1;
    }
    rep (i, q) {
        cin >> xi;
        auto it = find(a.begin(), a.end(), xi);
        auto idx = it - a.begin() + 1;
        // cout << idx << ' ' << *it << endl;
        if (idx < n) {
            int temp = *it;
            *(it) = *(it+1);
            *(it+1) = temp;
        } else {
            int temp = *it;
            *(it) = *(it-1);
            *(it-1) = temp;
        }
    }
    rep (i, n) {
        cout << a[i] << " ";
    }
    cout << endl;
}