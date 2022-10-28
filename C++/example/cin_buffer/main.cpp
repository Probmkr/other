#include <iostream>
#include <iomanip>

using namespace std;

void cinIgnore();

int main()
{
  int opt = -1;
  while (true)
  {
    cout << "enter number: ";
    cin >> opt;
    if (cin.fail()){
      cout << "正確な値を入力してください" << endl;
      cin.clear();
      cinIgnore();
      continue;
    }
    if (opt == -1)
    {
      cout << "終了します" << endl;
      exit(0);
    }
    cout << opt << " が入力されました" << endl;
  }
}

void cinIgnore()
{
  cin.ignore(numeric_limits<streamsize>::max(), '\n');
}
