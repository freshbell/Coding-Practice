

def fin(wich,cnt):
    global maximum
    global arr

    if wich == N-1: 
        if maximum < cnt: maximum = cnt
    else:
        for i in range(wich+1, N):
            if arr[wich] < arr[i]:
                fin(i,cnt+1)


N = eval(input())
arr = list(map(int,input().split()))

def dynamic():
    maximum = 1
    global arr

    d = [0 for _ in range(N)]
    for i in range(N):
        d[i] = 1
        for j in range(i):
            if arr[i] < arr[j]:
                d[i] = max(d[i],d[j] + 1)
                if maximum < d[i]: maximum = d[i]

    return maximum

print(dynamic())