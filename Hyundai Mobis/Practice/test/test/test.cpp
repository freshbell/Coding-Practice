#include <iostream>
#include <vector>
#include <map>
using namespace std;

vector<int> solution(vector<vector<int> > v) {
    int i;
    vector<int> ans;
    map<int, int> x;
    map<int, int> y;

    for (i = 0; i < v.size(); i++) {
        if (x.find(v[i].at(0)) == x.end()) {
            x.insert(make_pair(v[i].at(0), 1));
        }
        else
            x[v[i].at(0)] += 1;
        if (y.find(v[i].at(1)) == y.end()) {
            y.insert(make_pair(v[i].at(1), 1));
        }
        else
            y[v[i].at(1)] += 1;
    }

    for (auto a : x) {
        if (a.second == 1)
        {
            ans.push_back(a.second);
            break;
        }
    }
    for (auto a : y) {
        if (a.second == 1)
        {
            ans.push_back(a.second);
            break;
        }
    }

     return ans;
}
int main()
{
    vector<vector<int>> v;
    vector<int> tmp1;
    map<int, int> chk;
    chk.insert(make_pair(0, 0));
    tmp1.push_back(1);
    tmp1.push_back(4);
    v.push_back(tmp1);
    tmp1.pop_back();
    tmp1.pop_back();
    tmp1.push_back(3);
    tmp1.push_back(4);
    v.push_back(tmp1);
    tmp1.pop_back();
    tmp1.pop_back();
    tmp1.push_back(3);
    tmp1.push_back(10);
    v.push_back(tmp1);
    tmp1.pop_back();
    tmp1.pop_back();
    solution(v);
}

// 프로그램 실행: <Ctrl+F5> 또는 [디버그] > [디버깅하지 않고 시작] 메뉴
// 프로그램 디버그: <F5> 키 또는 [디버그] > [디버깅 시작] 메뉴

// 시작을 위한 팁: 
//   1. [솔루션 탐색기] 창을 사용하여 파일을 추가/관리합니다.
//   2. [팀 탐색기] 창을 사용하여 소스 제어에 연결합니다.
//   3. [출력] 창을 사용하여 빌드 출력 및 기타 메시지를 확인합니다.
//   4. [오류 목록] 창을 사용하여 오류를 봅니다.
//   5. [프로젝트] > [새 항목 추가]로 이동하여 새 코드 파일을 만들거나, [프로젝트] > [기존 항목 추가]로 이동하여 기존 코드 파일을 프로젝트에 추가합니다.
//   6. 나중에 이 프로젝트를 다시 열려면 [파일] > [열기] > [프로젝트]로 이동하고 .sln 파일을 선택합니다.
