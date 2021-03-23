#2진법 인덱스 구조를 활용해 구간 합 문제를 해결

#for i in range(9):
    #print(bin(i),bin(-i))
    #print(i & -i)

# 0 : 0 0 0 0, 1 1 1 1 -> 1 0 0 0 0 => 0
# 1 : 0 0 0 1, 1 1 1 0 -> 1 1 1 1  => 1
# 2 : 0 0 1 0, 1 1 0 1 -> 1 1 1 0 => 2
# 3 : 0 0 1 1, 1 1 0 0 -> 1 1 0 1 => 1
# 4 : 0 1 0 0, 1 0 1 1 -> 1 1 1 0 => 4
# 5 : => 1
# 6 : 0 1 1 0, 1 0 0 1 -> 1 0 1 0 => 2

import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())

arr = [0] * (n+1)
tree = [0] * (n+1)

def prefix_sum(i):
    result = 0
    
    while i > 0:
        result += tree[i]
        i -= (i & -i)

    return result

def update(i, dif):
    while i <= n:
        tree[i] += dif
        i += (i & -i)
    print(tree)

def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)

for i in range(1, n + 1):
    x = int(input())
    arr[i] = x
    update(i,x)

for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c - arr[b])
        arr[b] = c
    else:
        print(interval_sum(b, c))

