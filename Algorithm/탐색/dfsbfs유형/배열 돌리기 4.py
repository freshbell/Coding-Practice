from itertools import permutations
from copy import deepcopy

N,M,K = map(int,input().split())
rot_num = [i for i in range(K)]
permu = list(permutations(rot_num))

A = [list(map(int,input().split())) for _ in range(N)]
rcs = [list(map(int,input().split())) for _ in range(K)]

dx, dy = [1,0,-1,0],[0,-1,0,1]

def rotate(A,r,c,s):

    rot = deepcopy(A)
    r, c = r-1, c-1

    for i in range(1,s+1):
        rr, cc = r-i, c+i
        for j in range(4):
            for _ in range(i*2):
                rrr, ccc = rr + dx[j], cc + dy[j]
                rot[rrr][ccc] = A[rr][cc]
                rr, cc = rrr, ccc

    return rot

minimum = 999999
while permu:
    g = list(permu.pop(0))
    rot = deepcopy(A)
    while g:
        [r,c,s] = rcs[g.pop(0)]
        rot = rotate(rot,r,c,s)
    
    for i in range(N):
        hap = 0
        for j in rot[i]:
            hap += j
        minimum = min(minimum,hap)
    
print(minimum)