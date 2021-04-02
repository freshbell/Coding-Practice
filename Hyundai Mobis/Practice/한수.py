N = int(input())

if N >= 100: ans = 99
else: ans = N

if N <= 110 : print(ans)
else:
    ans += 1
    for i in range(112,N+1):
        gap = i
        for j in range(len(str(i)) - 1,0,-1):
            div = 10 ** j
            A = gap // div
            gap %= div
            B = gap // (div // 10)
            if j == len(str(i)) - 1: bigyo = A - B
            else:
                if bigyo != A - B:
                    ans -= 1
                    break
        ans += 1

    print(ans)