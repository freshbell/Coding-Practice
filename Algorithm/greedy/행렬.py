N, M = map(int, input().split())
A = [list(map(int,input())) for _ in range(N)]
B = [list(map(int,input())) for _ in range(N)]

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            cnt += 1
            for k in range(i,i+3):
                for l in range(j,j+3):
                    A[k][l] ^= 1

if A == B: print(cnt)
else: print(-1)