// 징검다리.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int i, j;
    int N;
    int x;
    int ans = 0;
    vector<int> stones;
    vector<int> d;
    stones.push_back(0);
    d.push_back(0);

    cin >> N;
    for (i = 0; i < N; i++) {
        cin >> x;
        stones.push_back(x);
        d.push_back(0);
    }

    for (i = 1; i <= N; i++) {
        int stone = stones[i];
        for (j = 0; j < i; j++) {
            if (stone > stones[j]){
                d[i] = max(d[i], d[j] + 1);
                ans = max(ans, d[i]);
            }
        }
    }

    cout << ans;
}