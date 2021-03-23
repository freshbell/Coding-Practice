INF = int(1e9)

n = int(input()) # 노드의 개수
m = int(input()) # 간선의 개수
graph = [[0 if i == j else INF for j in range(n+1)] for i in range(n+1)]
graph[0][0] = INF

for _ in range(m):
    cur, nex, gap = map(int,input().split())
    graph[cur][nex] = gap
    
print(graph)
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])