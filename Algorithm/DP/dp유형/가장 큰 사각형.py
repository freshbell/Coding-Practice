n, m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]
d = [[0 for _ in range(m+1)] for _ in range(n+1)]

maximum = 0

for i in range(1,n+1):
    for j in range(1,m+1):
        d[i][j] = arr[i-1][j-1] + d[i-1][j] + d[i][j-1] - d[i-1][j-1]

print(d)
for size in range(0,min(n,m)):
    for i in range(1,n+1):
        if i + size > n: break
        for j in range(1,m+1):
            if j + size > m: break
            gap = d[i+size][j+size] - d[i+size][j - 1] - d[i - 1][j+size] + d[i - 1][j - 1]
            if gap  == (size+1)**2: maximum = max(maximum,gap)

print(maximum)

#for i in range(1, n+1):
#    for j in range(1, m+1):
#        if arr[i-1][j-1]:
#            d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1
#        maximum = max(maximum, d[i][j])

