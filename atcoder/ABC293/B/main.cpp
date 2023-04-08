#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); i++)
using namespace std;
using ll = long long;

string join(const vector<string> &v, const char *delim = 0)
{
  string s;
  if (!v.empty())
  {
    s += v[0];
    for (decltype(v.size()) i = 1, c = v.size(); i < c; ++i)
    {
      if (delim)
        s += delim;
      s += v[i];
    }
  }
  return s;
}

int main()
{
  int n;
  cin >> n;
  vector<bool> calls(n);
  vector<string> called;
  int call;
  for (int i = 0; i < n; i++)
  {
    cin >> call;
    if (!calls[i])
      calls[call - 1] = true;
  }
  int count = 0;
  for (int i = 0; i < n; i++)
  {
    if (!calls[i])
    {
      count++;
      called.push_back(to_string(i + 1));
    }
  }
  cout << count << endl
       << join(called, " ");
}