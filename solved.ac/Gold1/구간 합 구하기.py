import sys

N, M, K = map(int,sys.stdin.readline().split())

tree = [0 for _ in range(N+1)]

def update(i, dif):
    while i <= N:
        tree[i] += dif
        i += (i & -i)

def nujeok():
    gap = [0]
    
    for i in range(1,N+1):
        A = 0
        wich = i
        while wich > 0:
            A += tree[wich]
            wich -= (wich & -wich)
        gap.append(A)
    return gap

num = []
num.append(0)
for i in range(N):
    num.append(eval(sys.stdin.readline()))
    update(i + 1, num[-1])
gap = nujeok()

for i in range(M+K):
    a,b,c = map(int,sys.stdin.readline().split())
    if a == 1: 
        update(b, c - num[b])
        num[b] = c
        gap = nujeok()
    else:
        print(gap[c] - gap[b-1])