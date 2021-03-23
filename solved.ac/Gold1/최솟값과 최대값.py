N, M = map(int,input().split())

#d = [[0,100001] for _ in range(N+1)]
#def update(i, gap):
#    while i <= N + 1:
#        if d[i][0] < gap: d[i][0] = gap
#        if d[i][1] > gap: d[i][1] = gap
#        i += (i & -i)

#number = [[] for _ in range(N+1)]
for i in range(N):
    gap = eval(input())
    #number[0].append([gap,gap])

#for i in range(N):
#    for j in range(len(number[i])-1):
#        number[i+1].append([max(number[i][j][0],number[i][j+1][0]),min(number[i][j][1],number[i][j+1][1])])

for i in range(M):
    A, B = map(int,input().split())
#    print(number[B-A][A-1][1],number[B-A][A-1][0])

