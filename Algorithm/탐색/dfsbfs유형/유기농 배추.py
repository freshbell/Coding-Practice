T = eval(input())

def fill(baechu, x, y):
    g = []
    g.append([x,y])
    while g:
        [i,  j] = g.pop(0)
        if i-1 >= 0 and baechu[i-1][j] == 1:
            baechu[i-1][j] = 0
            g.append([i-1,j])
        if j-1 >= 0 and baechu[i][j-1] == 1:
            baechu[i][j-1] = 0
            g.append([i,j-1])
        if i+1 < len(baechu) and baechu[i+1][j] == 1:
            baechu[i+1][j] = 0
            g.append([i+1,j])
        if j+1 < len(baechu[0]) and baechu[i][j+1] == 1:
            baechu[i][j+1] = 0
            g.append([i,j+1])

import sys
sys.setrecursionlimit(100000)
baechu = [[]]
def dfs(i, j):
    global baechu
    baechu[i][j] = 0
    print(baechu)
    if i-1 >= 0 and baechu[i-1][j] == 1: dfs(i-1,j)
    if j-1 >= 0 and baechu[i][j-1] == 1: dfs(i,j-1)
    if i+1 < len(baechu) and baechu[i+1][j] == 1: dfs(i+1,j)
    if j+1 < len(baechu[0]) and baechu[i][j+1] == 1: dfs(i,j+1)

for _ in range(T):
    M, N, K = map(int,input().split())
    baechu = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K):
        X, Y = map(int,input().split())
        baechu[Y][X] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if baechu[i][j] == 1:
                count += 1
                dfs(i, j)
    print(count)