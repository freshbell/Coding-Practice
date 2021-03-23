N = eval(input())
number = list(map(int,input().split()))
d = [0 for _ in range(N)]

for i in range(N):
    d[i] = number[i]
    for j in range(i):
        if number[i] > number[j]:
            d[i] = max(d[i],d[j] + number[i])
    maximum = max(maximum,d[i])

print(maximum)