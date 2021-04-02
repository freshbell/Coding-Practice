N = int(input())
up = list(map(int,input().split()))

minimum = up[0]
maximum_size = 0

for i in range(1,N):
    if up[i] > up[i-1]: maximum_size = max(maximum_size, up[i] - minimum)
    else: minimum = up[i]

print(maximum_size)
    