#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); i++)
using namespace std;
using ll = long long;

int main()
{
  int N, T;
  cin >> N >> T;
  int C[N], R[N];
  int max_r[] = {0, 0};
  int max_p[] = {-1, -1};
  bool T_flag = false;
  rep(i, N)
  {
    cin >> C[i];
  }
  rep(i, N)
  {
    cin >> R[i];
  }
  rep(i, N)
  {
    if (C[i] == T)
    {
      T_flag = true;
      max_p[0] = R[i] == (max_r[0] = max(max_r[0], R[i])) ? i : max_p[0];
    }
    else if (!T_flag && C[i] == C[0])
    {
      max_p[1] = R[i] == (max_r[1] = max(max_r[1], R[i])) ? i : max_p[1];
    }
  }
  cout << (T_flag ? max_p[0] + 1 : max_p[1] + 1) << endl;
}