#Lowest Common Ancestor

# 시간적 여유가 있을 경우
# DFS를 이용해 모든 노드에 대하여 깊이를 계산
# 한칸씩 올라가면서 값 비교

# 시간적 여유가 없을 경우 
# 다이나믹 프로그래밍을 이용 O(MlogN)
# 2^i 번째 부모에 대한 정보 저장
# 두 높이에 대한 깊이 저장
# 1. dfs로 바로 위의 부모 구하기
# 2. 전체 부모를 구하는 관계 구하기

import sys
sys.setrecursionlimit(int(1e5))

LOG = 21
n = 11
deep = [0] * (n + 1)
chk = [0] * (n + 1)
graph = [[] for _ in range (n+1)]

graph[1].append(3); graph[3].append(1)
graph[4].append(2); graph[2].append(4)
graph[1].append(6); graph[6].append(1)
graph[5].append(4); graph[4].append(5)
graph[2].append(3); graph[3].append(2)
graph[5].append(7); graph[7].append(5)
graph[6].append(8); graph[8].append(6)
graph[8].append(9); graph[9].append(9)
graph[10].append(9); graph[9].append(10)
graph[10].append(11); graph[11].append(10)

parent = [[0] * LOG for _ in range(n+1)]

def dfs(x, depth):
    
    deep[x] = depth
    chk[x] = 1
    for i in graph[x]:
        if chk[i]: continue
        parent[i][0] = x
        dfs(i, depth + 1)

def set_parent():
    dfs(1,0)
    for i in range(1,LOG):
        for j in range(1, n + 1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def find(a,b):
    # b가 뎁스가 큰걸로
    if deep[a] > deep[b]:
        a, b = b, a

    #공통 부모 찾기
    for i in range(LOG-1, -1, -1):
        if deep[b] - deep[a] >= (1<<i):
            b = parent[b][i]
    if a == b: return a

    for i in range(LOG-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            print(i)
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

set_parent()

print(find(7, 11))