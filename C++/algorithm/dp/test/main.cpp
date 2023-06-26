#include <bits/stdc++.h>
using namespace std;

// 入力
int n, W;
int weight[110], value[110];

// DPテーブル
int dp[110][10010];

void line() {
  cout << "---------------------------------" << endl;
}

int main()
{
  cin >> n >> W;
  for (int i = 0; i < n; ++i)
    cin >> weight[i] >> value[i];

  // DP初期条件: dp[0][w] = 0
  for (int w = 0; w <= W; ++w)
    dp[0][w] = 0;

  // DPループ
  for (int i = 0; i < n; ++i)
  {
    cout << "\ti = " << i << endl;
    for (int w = 0; w <= W; ++w)
    {
      cout << "\tw = " << w << endl;
      cout << "if (" << w << " >= " << weight[i] << ")" << endl;
      if (w >= weight[i])
      {
        dp[i + 1][w] = max(dp[i][w - weight[i]] + value[i], dp[i][w]);
      }
      else
      {
        dp[i + 1][w] = dp[i][w];
      }
    }
  }
  line();

  cout << "     w  v" << endl;
  for (int i = 0; i < n; ++i) {
    cout << setw(3) << right << i+1;
    cout << setw(3) << right << weight[i];
    cout << setw(3) << right << value[i];
    cout << endl;
  }
  line();

  cout << "   ";
  for (int w = 0; w <= W; ++w)
  {
    cout << setw(3) << right << w;
  }
  cout << endl;
  for (int i = 0; i <= n; ++i)
  {
    cout << setw(3) << right << i;
    for (int w = 0; w <= W; ++w)
    {
      cout << setw(3) << right << dp[i][w];
    }
    cout << endl;
  }
}
