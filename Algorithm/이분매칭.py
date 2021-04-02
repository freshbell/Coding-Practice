import sys
sys.setrecursionlimit(10**6)

N, M = map(int,input().split())
jido = [[] for _ in range(N)]
chk = [False] * (N + 1)
line = [0] * (N + 1)

for i in range(M):
    x, y = map(int, input().split())
    jido[x].append(y)

print(jido)

def dfs(wich):
    for i in jido[wich]:
        if chk[i] == True: continue
        chk[i] = True

        if line[i] == 0 or dfs(line[i]):
            line[i] = wich
            return True
    return False

count = 0
for i in range(1,4):
    chk = [False] * (N + 1)
    if dfs(i): count += 1
    
print(line)
print(count)