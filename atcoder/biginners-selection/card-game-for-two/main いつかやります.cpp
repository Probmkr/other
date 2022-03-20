#include<bits/stdc++.h>
#define rep(i, n) for(int i=0; i < (n); i++)
using namespace std;
using ll = long long;

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  rep(i, n) cin >> a[i];
  sort(a.begin(), a.end(), [](int a, int b){
    return a > b;
  });

  int alice = 0, bob = 0;
  for(int i=0; i<n; i+=2) {
    alice+=a[i];
  }
  for(int i=1; i<n; i+=2) {
    bob+=a[i];
  }
  cout << alice - bob << endl;
}