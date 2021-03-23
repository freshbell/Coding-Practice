Test = eval(input())

for i in range(Test):
    N, M = map(int,input().split())
    people = []
    for _ in range(M):
        li = list(map(int,input().split()))
        people.append([li[1],li[0]])
    people.sort()

    count = 0
    chk = [0 for _ in range(N+1)]
    for [b,a] in people:
        for j in range(a, b+1):
            if chk[j] == 0:
                chk[j] = 1
                count += 1
                break
    
    print(count)