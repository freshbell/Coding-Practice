from itertools import combinations

def check(arr,wich):
    chk = {}
    
    for i in arr:
        st = ""
        for j in wich:
            st += str(i[j-1]) + " "

        if st in chk:
            return False
        else:
            chk[st] = 1
    
    return True

def solution(relation):
    answer = 0
    comb = [i for i in range(1,len(relation[0])+1)]
    arr = []
    find = []

    for i in range(1,len(relation[0])+1):
        for j in combinations(comb,i):
            co = []
            for k in range(len(j)):
                co.append(j[k])
            arr.append(co)
    
    for i in range(len(arr)):
        chk = 0
        st = ""
        
        for j in find:
            cnt = 0
            for k in arr[i]:
                if str(k) in j:
                    cnt += 1
            if cnt == len(j):
                chk = 1
                break

        if chk == 0:
            for j in arr[i]:
                st += str(j)
            if check(relation,arr[i]):
                answer += 1
                find.append(st)
            
    return answer

relation = [["b", "2","a","a","b"], ["b", "2","7","1","b"], ["1", "0","a","a","8"],["7","5","a","a","9"],["3","0","a","f","9"]]
print(solution(relation))