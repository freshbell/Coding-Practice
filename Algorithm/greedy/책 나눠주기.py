Test = eval(input())

for i in range(Test):
    N, M = map(int,input().split())
    people = []
    for _ in range(M):
        li = list(map(int,input().split()))
        people.append([li[1] - li[0]] + li)
        people.sort()
    
    chk = [0 for _ in range(N+1)]
    chk_su = [0 for _ in range(N+1)]
    for j in people:
        for k in range(j[1], j[2] + 1):
            chk_su[k] += 1

    count = 0
    for [minus,a,b] in people:
        wich = -1
        minimum = 99999
        for j in range(a, b+1):
            if chk[j] == 0:
                if minimum > chk_su[j]:
                    minimum = chk_su[j]
                    wich = j
        if wich != -1:
            chk[wich] = 1
            count += 1

    print(count)