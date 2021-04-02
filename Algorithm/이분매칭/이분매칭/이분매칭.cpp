#include <iostream>
#include <vector>
#define MAX 10001

using namespace std;

vector<int> a[MAX];
int d[MAX];
bool c[MAX];
int n, k;

// 매칭에 성공한 경우 True, 실패한 경우 False
bool dfs(int x) {
    for (int i = 0; i < a[x].size(); i++) {
        int t = a[x][i];
        // 이미 처리한 노드는 더 이상 볼 필요가 없음
        if (c[t]) continue;
        c[t] = true;
        // 비어있거나 점유 노드에 더 들어갈 공간이 있는 경우
        if (d[t] == 0 || dfs(d[t])) {
            d[t] = x;
            return true;
        }
    }
    return false;
}

int main()
{
    int i;
    int x, y;
    int count = 0;

    cin >> n >> k;
    for(i = 0; i < k ; i ++) {
        cin >> x >> y;
        a[x].push_back(y);
    }
    
    for (int i = 1; i <= n; i++) {
        fill(c, c + MAX, false);
        if (dfs(i)) count++;
    }
    cout << count << endl;
    return 0;
}
    /*
    ///printf("%d개의 매칭이 이루어졌습니다.\n", count);
    for (int i = 1; i < MAX; i++) {
        if (d[i] != 0) {
            printf("%d -> %d\n", d[i], i);
        }
    }
    */
 
