#include <string>
#include <iostream>

using namespace std;

int main(){
    int i = -1;
    cout << "enter number > ";
    cin >> i;
    cout << i << endl;
    cin.clear();
    cin.ignore();
    cin >> i;
    cout << i << endl;
}
