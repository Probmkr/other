#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); i++)
using namespace std;
using ll = long long;

int main()
{
  string S;
  int N;
  bool bar_flag = false, ast_flag = false;
  cin >> N;
  cin >> S;
  for (int i = 0; i < N; i++)
  {
    bar_flag = bar_flag ^ (S[i] == '|');
    ast_flag = ast_flag ^ (bar_flag && S[i] == '*');
  }
  cout << (ast_flag ? "in" : "out") << endl;
}