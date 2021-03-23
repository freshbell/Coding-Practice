import heapq
from copy import deepcopy

K, N = map(int, input().split())
sosu = list(map(int,input().split()))
sosu2 = deepcopy(sosu)
heapq.heapify(sosu2)

chk = {}
#for i in sosu:
#    chk[i] = True

count = 0
while count < N:
    su = heapq.heappop(sosu2)
    if su in chk: continue
    chk[su] = True
    count += 1

    for i in sosu:
        if su * i in chk: continue
        
        heapq.heappush(sosu2,i*su)

print(su)



#count = 0

#def fin(sosu,wich,gop,want):
#    if gop == want: return True
#    for i in range(wich,len(sosu)):
##        if sosu[i] * gop <= want:
#            chk = fin(sosu,wich,sosu[i]*gop,want)
#            if chk == True: return True
#    return False

#su = 0
#count = 0

#while True:
#    su += 1
#    for j in range(len(sosu)):
#        if su % sosu[j] == 0:
#            if fin(sosu,j,1,su): 
#                count += 1
#                break
#    if count == N: break

#print(su)
