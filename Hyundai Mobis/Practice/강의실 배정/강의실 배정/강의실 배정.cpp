#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main()
{
    int i, j;
    int N;
    vector<vector<int>> ip;
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> que;

    // 입력
    cin >> N;
    for (i = 0; i < N; i++) {
        int start, end;
        vector<int> tmp;
        cin >> start >> end;
        tmp.push_back(end);
        tmp.push_back(start);
        ip.push_back(tmp);
        que.push(make_pair(end, start));
    }
    sort(ip.begin(), ip.end());
    
    int count = 0;
    int end = 0;
    for (i = 0; i < N; i++) {
        if (ip[i][0] == end) continue;
        if (end <= ip[i].at(1)) {
            end = ip[i].at(0);
            count += 1;
        }
    }

    cout << count;
}