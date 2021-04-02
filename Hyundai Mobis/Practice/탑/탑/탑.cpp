#include <iostream>
#include <stack>

using namespace std;

int main()
{
    int i;
    int N;
    int ip;
    int ans;
    int max = 0;
    stack<pair<int, int>> arr;

    cin >> N;
    for (i = 0; i < N; i++) {
        cin >> ip;
        ans = 0;
        if (max >= ip) {
            while (arr.size() > 0) {
                if (ip > arr.top().first) arr.pop();
                else {
                    ans = arr.top().second + 1;
                    break;
                }
            }
        }
        else max = ip;

        cout << ans << " ";
        arr.push(make_pair(ip, i));
    }

    return 0;
}