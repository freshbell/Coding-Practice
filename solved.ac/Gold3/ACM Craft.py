TestCase = eval(input())

for test in range(TestCase):
    N, K = map(int, input().split()) # 건물, 건물규칙
    tree = [[0 for _ in range(N+1)] for _ in range(N+1)]
    time = list(map(int,input().split()))    

    wisang = [0 for _ in range(N+1)]
    for ip in range(K):
        X, Y = map(int, input().split())
        tree[X][Y] = 1
        wisang[Y] += 1

    W = eval(input())

    g = []
    d = [0 for _ in range(N+1)]
    for i in range(N+1):
        if wisang[i] == 0:
            g.append(i)
            d[i] = time[i-1]
            wisang[i] = -1

    while g:
        a = g.pop(0)

        for i in range(1,N+1):
            if tree[a][i] == 1:
                wisang[i] -= 1
                d[i] = max(d[i],d[a] + time[i-1])
                if wisang[i] == 0 :
                    g.append(i)
                    wisang[i] = -1

    print(d[W])