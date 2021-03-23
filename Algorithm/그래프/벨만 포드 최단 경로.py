# 음수 간선이 포함된 상황에서의 최단 거리 문제

# 음수 간선이 있는경우
# 1. 음수 간선 순환은 없는 경우
# 2. 음수 간선 순환이 있는 경우
# O(VE) 정점의 개수 * 간선의 개수

# 1. 출발 노드를 설정
# 2. 최단 거리 테이블을 초기
# 3. 다음 과정 N-1번 반복
# 3-1. 전체 간선 E개를 하나씩 확인
# 3-2. 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
# 음수 간선 순환이 발생하는지 체크하고 싶다면 -> 3번의 과정을 한 번 더 수행 -> 테이블이 갱신된다면 음수 간선 순환이 존재

INF = int(1e9)

def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                if i == n - 1: return True
    return False

n, m = map(int,input().split())
edges = []
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a,b,c))

start = 1
negative_cycle = bf(start)

if negative_cycle:
    print("-1")
else:
    for i in range(2, n+1):
        if dist[i] == INF: print("-1")
        else: print(dist[i])