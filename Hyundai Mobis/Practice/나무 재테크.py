N, M, K = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(N)]
jido = [[5 for _ in range(len(A[0]))] for _ in range(N)]

dx, dy = [-1,-1,-1,0,0,1,1,1], [-1,0,1,-1,1,-1,0,1]

tree = []

for _ in range(M):
    X, Y, Z = map(int,input().split())
    tree.append((Z,X-1,Y-1))

for i in range(1, K+1):
    tree.sort()
    death = []
    for j in range(len(tree)):
        Z, X, Y = tree.pop(0)
        if jido[X][Y] >= Z:
            jido[X][Y] -= Z
            if (Z + 1) % 5 == 0:
                for k in range(8):
                    if 0 <= X + dx[k] < N and 0 <= Y + dy[k] < len(A[0]): tree.append((1,X+dx[k],Y+dy[k]))
            tree.append((Z+1,X,Y))
        else: death.append((Z,X,Y))

    while death:
        Z, X, Y = death.pop(0)
        jido[X][Y] += Z // 2

    for j in range(N):
        for k in range(len(A[0])):
            jido[j][k] += A[j][k]

print(len(tree))
