#include <iostream>
#include <fstream>

using namespace std;

void cinIgnore();

int main(int argc, char *argv[])
{
  string fileName = argv[1];
  char ch;
  cout << "右の画像を開きます" << fileName << endl;
  ifstream ifs(fileName, ios::binary | ios::in);
  if (!ifs)
  {
    cout << "画像を開くことに失敗しました" << endl;
    exit(1);
  }
  else
  {
    cout << "画像を開くことに成功しました" << endl;
  }

  while (true)
  {
    int opt = -1;
    cout << "したい作業を選択してください" << endl <<
    "[0] 終了  [1] 全て出力" << endl;
    cin >> opt;
    if (cin.fail() && !((opt < 0) || (opt > 2)))
    {
      cout << "正確な数値を入力してください" << endl;
      cinIgnore();
    }
  }
}

void cinIgnore() {
  cin.clear();
  cin.ignore(numeric_limits<streamsize>::max(), '\n');
}
