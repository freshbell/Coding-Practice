N = int(input())
stones = [0] + list(map(int,input().split()))
up = [0] * (N+1)
down = [0] * (N+1)
ans = 0

zero = 0
for i in range(1,N+1):
    stone = stones[i]
    for j in range(0, i+1):
        if stone > stones[j]:
            up[i] = max(up[i],up[j]+1)
    if up[i] == 1:
        zero += 1

if zero == N: ans = 0
else:
    for i in range(2,N+1):
        stone = stones[i]
        for j in range(1, i+1):
            if stone < stones[j]:
                down[i] = max(down[i],up[j] + 1, down[j] + 1)
                ans = max(ans,down[i])

print(ans)