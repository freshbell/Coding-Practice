def dfs(wich,chk,link):
    chk[wich] += 1
    print(wich,chk)
    for i in sorted(link[wich]):
        if chk[i] > 0: continue
        dfs(i,chk,link)
        chk[wich] += 1
        if chk[wich] > 2:
            chk[i] -= 1
            chk[wich] -= 1

    return
def solution(t):
    answer = 0

    link = [[] for _ in range(len(t)+1)]
    for i in t:
        link[i[0]].append(i[1])
        link[i[1]].append(i[0])
    print(link)
    for i in range(len(t)+1):
        chk = [0 for _ in range(len(t)+1)]
        dfs(i,chk,link)
    return answer

t = [[2,5],[2,0],[3,2],[4,2],[2,1]]
solution(t)