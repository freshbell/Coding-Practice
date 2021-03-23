Testcase = eval(input())

for i in range(Testcase):
    enemy = []
    guyeok, W = map(int,input().split())
    enemy.append(list(map(int,input().split())))
    enemy.append(list(map(int,input().split())))
    
    chk = [0 for _ in range(guyeok*2)]

    hap = 0
    orders = []
    chk = [0 for _ in range(guyeok*2)]
    for i in range(guyeok):
        hap = enemy[0][i] + enemy[0][(i+1)%guyeok]
        if guyeok > 1 and hap <= W: orders.append([hap,i,(i+1)%guyeok])
        hap = enemy[1][i] + enemy[1][(i+1)%guyeok]
        if guyeok > 1 and hap <= W: orders.append([hap,i + guyeok,(i+1)%guyeok + guyeok])
        hap = enemy[0][i] + enemy[1][i]
        if hap <= W: orders.append([hap,i,i + guyeok])

    orders.sort(reverse=True)
    cnt = 0

    for i in orders:
        if chk[i[1]-1] == 0 and chk[i[2]-1] == 0:
            chk[i[1]-1] = 1
            chk[i[2]-1] = 1
            cnt += 1
    print(cnt+(guyeok-cnt)*2)
