// 지도 자동 구축.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>

using namespace std;
int main()
{
    int i;
    int N = 0;
    int init = 2;
    cin >> N;
    for (i = 1; i <= N; i++) {
        init += (init - 1);
    }
    cout << init*init;
}

// 2 3 5 9 17
// 2+1, 3+2, 5+4, 9+8