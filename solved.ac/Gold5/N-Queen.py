N = eval(input())
import sys
sys.setrecursionlimit(10**10)

arr = [999 for _ in range(N+1)]
chk = [0 for _ in range(N+1)]
cnt = 0
a = 0
def queen(wich):
    global N, arr, chk, cnt, a
    if a == 1: return
    if wich == N + 1:
        cnt +=1
        for i in range(1,N+1):
            print(arr[i])
        a = 1
        return
    else :
        for i in range(1,N+1):
            if chk[i] == 1: continue
            else:
                cc = 0
                for j in range(1, wich):
                    if arr[wich - j] == i - j or arr[wich - j] == i + j: 
                        cc = 1
                        break
                if arr[wich-1] == i - 1 or arr[wich - 1] == i + 1 or cc == 1: continue
                else:
                    arr[wich] = i
                    chk[i] = 1
                    queen(wich + 1)
                    chk[i] = 0
                    arr[wich] = 999

queen(1)