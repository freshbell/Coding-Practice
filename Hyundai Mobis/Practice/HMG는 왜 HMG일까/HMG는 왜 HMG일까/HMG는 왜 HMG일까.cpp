#include <iostream>
#include <string>

using namespace std;

int main()
{
    int chk = 0;
    string ip;
    string chul;

    cin >> ip;
    chul = ip[0];
    for (auto n : ip) {
        if (chk == 1) {
            chul += n;
            chk = 0;
        }
        else if (n == '-') chk = 1;   
    }
    cout << chul << endl;
}
