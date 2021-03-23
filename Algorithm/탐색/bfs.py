#queue 자료구조

#큐(queue) 구현을 위해 deque 라이브러리 사용
#queue = deque()

#queue.append(5)
#queue.append(2)
#queue.append(3)
#queue.append(7)
#queue.popleft()
#queue.append(1)
#queue.append(4)
#queue.popleft()

#print(queue)
#queue.reverse()
#print(queue)

from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v,end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph,1,visited)