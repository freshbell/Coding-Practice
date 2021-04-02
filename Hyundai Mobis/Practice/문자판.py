from copy import deepcopy

dx, dy = [1,0,-1,0], [0,1,0,-1]
ans = 0

N, M, K = map(int, input().split())
pan = [list(input()) for _ in range(N)]
pan_chk = [[0 for _ in range(M)] for _ in range(N)]
want = list(input())

for i in range(N):
    for j in range(M):
        if want[0] == pan[i][j]: pan_chk[i][j] = 1

for wich in range(1,len(want)):
    pan_chk2 = deepcopy(pan_chk)
    pan_chk = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if pan[i][j] == want[wich]:
                hap = 0
                for l in range(1,K+1):
                    for m in range(4):
                        xx = i + dx[m] * l
                        yy = j + dy[m] * l
                        if not (0 <= xx < N and 0 <= yy < M): continue
                        hap += pan_chk2[xx][yy]
                pan_chk[i][j] = hap
                if wich == len(want) - 1: ans += hap

print(ans)
'''

for i in range(N):
    for j in range(M):
        if pan[i][j] == want[0]:
            g = []
            g.append((i,j,0))
            while g:
                x,y,wich = g.pop(0)
                if wich == len(want) - 1: ans += 1
                elif wich < len(want) - 1:
                    for l in range(1,K+1):
                        for m in range(4):
                            xx = x + dx[m] * l
                            yy = y + dy[m] * l

                            if not (0 <= xx < N and 0 <= yy < M): continue
                            if pan[xx][yy] == want[wich + 1]: g.append((xx,yy,wich+1))
print(ans)
'''