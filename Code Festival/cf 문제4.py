N, M = map(int, input().split())

jido = [['0' for _ in range(N+2)]]
for i in range(M):
    gap = list(map(str,input()))
    jido.append(['0'] + gap + ['0'])

def bfs(jido, x, y, M):
    q = []
    q.append([x,y,0])
    chk = [[0 for _ in range(N+2)] for _ in range(M+1)]
    while q:
        [x, y, cnt] = q.pop(0)
        if cnt > 20000: break
        if x == M: 
            return cnt
        if jido[x+1][y] == '.': q.append([x+1,y,cnt])
        if jido[x][y+1] == '.': q.append([x,y+1,cnt+1])
        if jido[x][y-1] == '.': q.append([x,y-1,cnt+1])

    return 9999999

minimum = 9999999
for i in range(1,N+1):
    if jido[1][i] == 'c':
        minimum = min(minimum,bfs(jido,1,i, M))

if minimum == 9999999: print(-1)
else: print(minimum)