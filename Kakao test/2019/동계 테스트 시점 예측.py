N, M = map(int, input().split())
jido = [list(map(int,input().split())) for _ in range(N)]

def bfs():
    dx, dy = [0,1,0,-1], [1,0,-1,0]
    g = [(0,0)]
    jido[0][0] = 2

    while g:
        x, y = g.pop()
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < N and 0 <= yy < M and jido[xx][yy] == 0:
                jido[xx][yy] = 2
                g.append((xx,yy))

    count = 0

    for i in range(N):
        for j in range(M):
            chk = 0
            if jido[i][j] == 1:
                for k in range(4):
                    xx = i + dx[k]
                    yy = j + dy[k]
                    if 0 <= xx < N and 0 <= yy < M and jido[xx][yy] == 2:
                        chk += 1
                        if chk == 2:
                            jido[i][j] = 0
                            count += 1
                            break
            else: count += 1
    
    if count == N*M: return False
    
    for i in range(N):
        for j in range(M):
            if jido[i][j] == 2:
                jido[i][j] = 0

    return True

ans = 1
while(bfs()):
    ans += 1

print(ans)