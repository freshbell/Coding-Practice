N, M = map(int, input().split())
d = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N):
    arr = list(map(int,input().split()))
    for j in range(len(arr)):
        d[i+1][j+1] = d[i+1][j] + d[i][j+1] - d[i][j] + arr[j]

print(d)        
K = eval(input())
for j in range(K):
    i,j,x,y = map(int,input().split())

    print(d[x][y] - d[x][j-1] - d[i-1][y] + d[i-1][j-1])
