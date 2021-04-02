#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>

using namespace std;

int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int N;

int check(int (*jido)[26], int (*chk)[26], int a, int b) {
    queue<pair<int, int>> g;
    g.push(make_pair(a, b));
    chk[a][b] = 1;
    int count = 0;
    while (!g.empty()) {
        count += 1;
        int x = g.front().first;
        int y = g.front().second;
        g.pop();

        for (int i = 0; i < 4; i++) {
            int xx = x + dx[i];
            int yy = y + dy[i];
            if (0 <= xx and xx < N and 0 <= yy and yy < N and chk[xx][yy] == 0 and jido[xx][yy] == 1) {
                chk[xx][yy] = 1;
                g.push(make_pair(xx, yy));
            }
        }
    }
    return count;
}

int main()
{
    int i, j;
    int jido[26][26] = { 0 };
    int chk[26][26] = { 0 };
    int count = 0;
    string ip;
    vector<int> ans;

    cin >> N;
    for (i = 0; i < N; i++) {
        cin >> ip;
        for (j = 0; j < N; j++) {
            jido[i][j] = ip[j] - '0';
        }
    }
    for (i = 0 ; i < N ; i ++)
        for (j = 0 ; j < N ; j ++)
            if (jido[i][j] == 1 and chk[i][j] == 0) {
                count += 1;
                ans.push_back(check(jido, chk, i, j));
            }

    cout << count << endl;
    sort(ans.begin(), ans.end());
    for (i = 0; i < ans.size(); i++)
        cout << ans[i] << endl;
}