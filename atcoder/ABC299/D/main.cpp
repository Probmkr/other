#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); i++)
using namespace std;
using ll = long long;

int main()
{
  int N, num, prev = 1;
  cin >> N;
  rep(i, 10)
  {
    cout << "? " << N - i - 1 << endl;
    cin >> num;
    if (num != prev)
    {
      cout << "! " << N - i - 1 << endl;
      return 0;
    }
  }
  prev = 0;
  rep(i, 10)
  {
    cout << "? " << i + 2 << endl;
    cin >> num;
    if (num != prev)
    {
      cout << "! " << i + 1 << endl;
      return 0;
    }
  }
}