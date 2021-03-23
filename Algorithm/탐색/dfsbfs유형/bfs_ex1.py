from collections import deque

def bfs(graph,x,y):
    queue = deque([[x,y]])
    graph[x][y] = 1
    
    while queue:
        [x,y] = queue.popleft()
        print(x,y)
        if graph[x-1][y] == 0 and x-1>=0:
            graph[x-1][y] = 1
            queue.append([x-1,y])
        if x+1 <= 3 and graph[x+1][y] == 0:
            graph[x+1][y] = 1
            queue.append([x+1,y])
        if graph[x][y-1] == 0 and y-1>=0:
            graph[x][y-1] = 1
            queue.append([x,y-1])
        if y+1<=4 and graph[x][y+1] == 0:
            graph[x][y+1] = 1
            queue.append([x,y+1])


graph = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,1,1,1,1],
    [0,1,0,1,0]
]
count = 0

for i in [0,1,2,3]:
    for j in [0,1,2,3,4]:
        if graph[i][j] == 0:
            bfs(graph,i,j)
            count = count + 1


print(count)
