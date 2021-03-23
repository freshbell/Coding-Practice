#1. 진입차수가 0인 정점을 큐에 삽입
#2 큐에서 원소를 꺼내 연결된 모든 간선을 제거
#3 간선 제거 이후에 진입차수가 0이 된 정점을 큐에 삽입
INF = int(1e9)
N = int(input()) # 노드 개수
M = int(input()) # 간선 개수
d = [0 for _ in range(N + 1)]
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    cur, nex = map(int,input().split())
    graph[cur][nex] = 1
    d[nex] += 1

g = []
for i in range(1,N+1):
    if d[i] == 0:
        g.append(i)

ans = []
while g:
    now = g.pop(0)
    ans.append(now)

    for i in range(N+1):
        if graph[now][i] == 1:
            d[i] -= 1
            if d[i] == 0: g.append(i)

print(ans)