def rotate(key):
    N = len(key)
    rot = [[0 for i in range(N)] for i in range(N)]

    for i in range(N):
        for j in range(N):
            rot[N - j - 1][i] = key[i][j]
    return rot

def check(key,table,M,x,y):
    N = len(key)
    hap = True

    for i in range(N):
        for j in range(N):
            table[i + x][j + y] = key[i][j] + table[i+x][j+y]

    for i in range(N-1,N + M - 1):
        for j in range(N-1,N + M - 1):
            if table[i][j] == 0 or table[i][j] > 1:
                hap = False

    for i in range(N):
        for j in range(N):
            table[i + x][j + y] = table[i+x][j+y] - key[i][j]

    return hap

def solution(key,lock):
    answer = True
    N  = len(key)
    M = len(lock)
    table = [[0 for i in range(M + 2*(N-1))] for i in range(M + 2*(N-1))]
    
    for i in range(4):
        for j in range(M):
            for k in range(M):
                table[N-1+j][N-1+k] = lock[j][k]

        for j in range(N+M-1):
            for k in range(N+M-1):
                if check(key,table,M,j,k):
                    return True  

        key = rotate(key)
    return False

key = [[0,1],[0,1]]
lock = [[1,1,1],[1,0,0],[1,1,1]]
print(solution(key,lock))