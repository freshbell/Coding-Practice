#최단 경로 탐색 알고리즘
#음의 간선을 포함 X
#다이나믹 프로그래밍을 활용 -> O(N^2)
#우선순위큐 -> O(MlgN)

#다이나믹
def getMinimumIndex():
    index = 0
    minimum = 9999

    for i in range(1, N+1):
        if not chk[i] and minimum > dis[i]:
            minimum = dis[i]
            index = i

    return index

def dikjstra(start):
    dis[start] = 0
    chk[start] = True
    
    for i in range(1, N+1):
        if start == i : continue
        dis[i] = A[start][i]

    for i in range(1, N):
        index = getMinimumIndex()
        chk[index] = True
        for j in range(1, N+1):
            if dis[j] > dis[index] + A[index][j]:
                dis[j] = dis[index] + A[index][j]


N = 10 #노드의 수
dis = [9999] * (N + 1) #거리
chk = [0] * (N + 1) #체크
A = [[]] #그래프 정보
#dikjstra(0)

#우선순위 큐
# 최소 힙

import heapq

def que():
    graph = [[],[(2,2),(5,3),(1,4)],[(3,3),(2,4)],[(3,2),(5,6)],[(3,3),(1,5)],[(1,3),(2,6)],[]]
    
    dijkstra_que(graph,1)

def dijkstra_que(graph,start):
    d = [9999] * 7
    q = []
    
    d[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        print(q,d)
        dist, now = heapq.heappop(q)
        
        if d[now] < dist: continue

        for i in graph[now]:
            cost = dist + i[0]
            if cost < d[i[1]]:
                d[i[1]] = cost
                heapq.heappush(q,(cost,i[1]))
    print(d)

que()