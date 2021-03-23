def solution(n, s, a, b, fares):
    d = [[9999 for i in range(n+1)] for i in range(n+1)]

    for x,y,length in fares:
        d[x][y] = length
        d[y][x] = length

    for i in range(1,n+1):
            d[i][i] = 0

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    minimum = d[s][a] + d[s][b]
    for i in range(1,n+1):
        if minimum > d[s][i] + d[i][a] + d[i][b]:
            minimum = d[s][i] + d[i][a] + d[i][b]
    print(d)
    answer = minimum
    return answer

n = 7
s = 3
a = 4
b = 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
print(solution(n,s,a,b,fares))