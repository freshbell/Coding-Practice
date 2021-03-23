def find(mooyo,chk,i,j,munja):
    count = 1
    g = [[i,j]]
    chk[i][j] = 1
    while g:
        [i,j] = g.pop(0)
        if i-1>=0 and mooyo[i-1][j] == munja and chk[i-1][j] == 0:
            g.append([i-1,j])
            chk[i-1][j] = 1
            count += 1
        if i+1 < len(mooyo) and mooyo[i+1][j] == munja and chk[i+1][j] == 0:
            g.append([i+1,j])
            chk[i+1][j] = 1
            count += 1
        if j-1 >= 0 and mooyo[i][j-1] == munja and chk[i][j-1] == 0:
            g.append([i,j-1])
            chk[i][j-1] = 1
            count += 1
        if j+1 < len(mooyo[0]) and mooyo[i][j+1] == munja and chk[i][j+1] == 0:
            g.append([i,j+1])
            chk[i][j+1] = 1
            count += 1
    return count

def erase(mooyo,chk):
    for i in range(len(mooyo)):
        for j in range(len(mooyo[0])):
            if chk[i][j] == 1:
                mooyo[i][j] = '0'

def down(mooyo,N,M):
    for i in range(N-1,-1,-1):
        for j in range(M-1,-1,-1):
            if mooyo[i][j] == '0':
                for k in range(i-1,-1,-1):
                    if mooyo[k][j] != '0':
                        mooyo[i][j] = mooyo[k][j]
                        mooyo[k][j] = '0'
                        break

    return 0

N, K = map(int, input().split())

mooyo = []
for i in range(N):
    mooyo.append(list(input()))

M = len(mooyo[0])
chk = [[0 for _ in range(M)] for _ in range(N)]

while True:
    cc = 0
    for i in range(N-1,-1,-1):
        for j in range(M-1,-1,-1):
            if mooyo[i][j] != '0':
                if find(mooyo,chk,i,j,mooyo[i][j]) >= K:
                    erase(mooyo,chk)
                    cc = 1
                chk = [[0 for _ in range(M)] for _ in range(N)]
    if cc == 0: break
    down(mooyo,N,M)
for i in mooyo: 
    for j in i: print(j,end='')
    print()