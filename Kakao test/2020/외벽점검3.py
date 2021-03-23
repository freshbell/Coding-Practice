from itertools import permutations, combinations

def check(n,person,permu,weak,chck):
    chk = {}
    cnt = 0
    
    for i in range(len(permu)):
        if i in chk: break
        dis = person[i]

        ver = {}
        rev = {}
        cnt1 = 0
        cnt2 = 0

        #시계방향
        for j in range(permu[i],permu[i]+dis+1):
            wich = j % n
            if chck[wich] == 1 and wich not in chk and wich not in ver:
                ver[wich] = True
                cnt1 += 1
        #반시계방향
        for j in range(permu[i],permu[i]-dis-1,-1):
            wich = j
            if j < 0:
                wich = n + j
            if j < 0:
                wich = n + j
            
            if chck[wich] == 1 and wich not in chk and wich not in rev:
                rev[wich] = True
                cnt2 += 1
        
            
        if cnt1 > cnt2:
            cnt += cnt1
            for k in list(ver.keys()):
                chk[k] = True
        else:
            cnt += cnt2
            for k in list(rev.keys()):
                chk[k] = True

    if len(list(chk.keys())) == len(weak): return len(person)
    return -1

def solution(n, weak, dist):
    answer = -1
    dist.sort(reverse=True)
    chck = [0 for i in range(n)]
    
    for i in weak:
        chck[i] = 1
    for i in range(1,2):#len(dist)+1):
        for j in list(permutations(weak,i)):
            answer = check(n,dist[:i],j,weak,chck)
            if answer != -1: break
        if answer != -1: break
    
    return answer


n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

print(solution(n,weak,dist))
print(list(permutations(weak,len(weak))))
#if j != permu[i] + dist:rev[wich] = True