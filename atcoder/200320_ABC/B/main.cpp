#include<string>
#include<iostream>
#include<map>
#define rep(i, n) for(int i=0; i < (n); i++)
using namespace std;
using ll = long long;

int main() {
  int n, dir = 0;
  map<string, int> xy;
  xy["x"] = 0;
  xy["y"] = 0;
  string t;
  cin >> n;
  cin >> t;
  for (int i=0; i<t.length(); i++) {
    if (t[i] == 'S') {
      int ad_dir = dir % 4;
      switch (ad_dir)
      {
      case 0:
        xy["x"]++;
        break;
      case 1:
        xy["y"]++;
        break;
      case 2:
        xy["x"]--;
        break;
      case 3:
        xy["y"]--;
        break;
      default:
        exit(1);
        break;
      }
    } else if (t[i] == 'R') {
      dir++;
    }
  }
  cout << xy["x"] << ' ' << xy["y"] << endl;
}