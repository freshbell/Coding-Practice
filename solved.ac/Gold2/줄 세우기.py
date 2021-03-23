N, M = map(int,input().split())

d = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    d[B] += 1

line = []
for i in range(1,N+1):
    if d[i] == 0:
        line.append(i)

while line:
    stu = line.pop(0)

    for i in graph[stu]:
        d[i] -= 1
        if d[i] == 0:
            line.append(i)
    
    print(stu, end = ' ')
