// 동계 테스트 시점 예측.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <queue>
#include <map>

using namespace std;

int N, M;
int jido[101][101] = { 0 };
int fill();
int ans = 0;

int main()
{
    int i, j;
    int count = 1;
    cin >> N >> M;
    
    for (i = 0; i < N; i++)
        for (j = 0; j < M; j++)
            cin >> jido[i][j];

    while (fill()) {}
}

int fill() {
    int i, j, k;
    int x, y;
    int xx, yy;
    int count = 0;
    int dx[4] = { 1,0,-1,0 };
    int dy[4] = { 0, -1, 0, 1 };
    ans += 1;
    queue<pair<int, int>> a;
    
    a.push(make_pair(0,0));

    while (a.size() > 0) {
        x = a.front().first;
        y = a.front().second;
        a.pop();
        
        for (i = 0; i < 4; i++) {
            xx = x + dx[i];
            yy = y + dy[i];
            if (!(0 <= xx and xx < N and 0 <= yy and yy < M)) continue;
            if (jido[xx][yy] == 0) {
                jido[xx][yy] = 2;
                a.push(make_pair(xx, yy));
            }
        }
    }

    int one = 0;
    for(i = 0 ; i < N ; i ++)
        for (j = 0; j < M; j++) {
            if (jido[i][j] == 1) {
                int chk = 0;
                for (k = 0; k < 4; k++) {
                    int xx = i + dx[k];
                    int yy = j + dy[k];

                    if (xx >= 0 and xx < N and yy >= 0 and yy < M) {
                        if (jido[xx][yy] == 2) {
                            //chk++;
                            //if (chk == 2) {
                            one += 1;
                             jido[i][j] = 0;
                            break;
                            //}
                        }
                    }
                }
            }
        }

    for (i = 0; i < N; i++)
        for (j = 0; j < M; j++) {
            if (jido[i][j] == 2 or jido[i][j] == 0)
            {
                count += 1;
                jido[i][j] = 0;
            }
        }
    if (count == N * M) {
        cout << ans << endl << one;
        return false;
    }
    else return true;
}