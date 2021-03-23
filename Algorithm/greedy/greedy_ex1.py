N, K = map(int, input().split())

count = 0

while N != 1:

    target = (N//K) * K
    count += (N - target)
    N = target
    
    if N < K:
        break

    count += 1
    N //= K

print(count)

