# d[i][j] : i에서 j까지 합하는데 필요한 최소 비용
# d[i][k] + d[k+1][j] + sum(A[i] ~ A[j])
# S는 1번부터 i번까지의 누적합

testcase = eval(input())

def process():
    N = eval(input())
    arr = [0] + list(map(int, input().split()))
    nujeok = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        nujeok[i] = nujeok[i-1] + arr[i]

    d = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(2, N+1):
        for j in range(1, N+2-i):
            d[j][j+i-1] = min([d[j][j+k] + d[j+k+1][j+i-1] for k in range(i-1)])  + (nujeok[j+i-1] - nujeok[j-1])


    print(d[1][N])

for i in range(testcase):
    process()