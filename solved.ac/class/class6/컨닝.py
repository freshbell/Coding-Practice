Testcase = eval(input())

for i in range(Testcase):
    N,M = map(int,input().split())
    room = []
    d = [0 for _ in range(M)]

    for i in range(N):
        room.append(list(input()))
        for j in range(M):
            if room[-1][j] == '.':
                d[j] += 1
    chk = [0 for _ in range(M)]

    hap = 0
    for i in range(0,M,2):
        hap += d[i]
    maximum = hap
    hap = 0
    for i in range(1,M,2):
        hap += d[i]

    if maximum < hap: maximum = hap
    
    print(maximum)
