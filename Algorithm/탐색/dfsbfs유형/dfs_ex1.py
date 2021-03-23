def dfs(graph,x,y,cnt,visited):
    if x-1 < 0 or x+1 >= n or y-1 < 0 or y+1 >= m:
        return False
    if x == n and y == m:
        return True

    if graph[x-1][y] == 1 and visited[x-1][y] == 0:
        visited[x-1][y] = 1
        dfs(graph,x-1,y,cnt+1,visited)
        visited[x-1][y] = 0
    if graph[x+1][y] == 1 and visited[x+1][y] == 0:
        visited[x+1][y] = 1
        dfs(graph,x+1,y,cnt+1,visited)
        visited[x+1][y] = 0
    if graph[x][y-1] == 1 and visited[x][y-1] == 0:
        visited[x][y-1] = 1
        dfs(graph,x,y-1,cnt+1,visited)
        visited[x][y-1] = 0
    if graph[x][y+1] == 1 and visited[x][y+1] == 0:
        visited[x][y+1] = 1
        dfs(graph,x,y+1,cnt+1,visited)
        visited[x][y+1] = 0

visited = [[]]
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    visited.append([0]*m)

visited[0][0] = 1
dfs(graph,0,0,1,visited)
