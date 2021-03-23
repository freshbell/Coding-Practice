N, K = map(int,input().split())
seq = list(map(int,input().split()))

dic = {}

for i in seq:
    if i not in dic: dic[i] = 0
    dic[i] += 1

count = 0
multi = [0 for _ in range(N)]
for i in range(K):
    minimum = 999
    chk = 0
    wich = 0
    for j in range(N):
        if multi[j] == 0:
            multi[j] = seq[i]
            chk = 1
            break
        elif seq[i] == multi[j]:
            chk = 1
            break
    if chk == 0:
        count += 1
        cc = 0
        change = [9999 for _ in range(N)]
        for k in range(i+1,K):
            for l in range(N):
                if multi[l] == seq[k] and change[l] == 9999: 
                    change[l] = k
                    cc += 1
            if cc == N - 1:
                for l in range(N):
                    if change[l] == 9999:
                        wich = l
                        break
            if wich != 0: break
        multi[wich] = seq[i]
        dic[seq[i]] -= 1
print(count)
    