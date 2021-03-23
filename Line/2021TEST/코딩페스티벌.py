N = int(input())
mapping = []
for _ in range(N):
    mapping.append(list(map(int,input())))

ans = [0 for _ in range(N)]
total = 0
for i in range(1, N+1):
    cnt = 0
    for j in range(N+1-i):
        for k in range(N+1-i):
            count = 0
            for l in range(j,j+i):
                for m in range(k,k+i):
                    if mapping[l][m] == 1:
                        count += 1
            if count == (i) * (i): cnt += 1
    ans[i-1] = cnt
    total += cnt

print("total: " + str(total))
for i in range(len(ans)):
    if ans[i] == 0: break
    print("size["+str(i+1)+"]: "+str(ans[i]))

