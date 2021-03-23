ans = []
ranking = []

def find(d,table,word,wich,st,name):
    global ans
    if d[wich] == 0 and word in name:
        ans.append(st)
        ranking.append((name,wich))
    else:
        for i in table[wich]:
            ne, name = i
            find(d,table,word,ne,st+"/"+name,name)

def solution(data, word):
    answer = []

    N = len(data)
    table = [[] for _ in range(N+1)]
    d = [0 for _ in range(N+1)]

    for i in data:
        a = list(i.split())
        d[int(a[2])] += 1
        table[int(a[2])].append((int(a[0]),a[1]))

    for i in table[0]:
        ne, name = i
        find(d,table,word,ne,name,name)
    
    if len(ans) < 1: return ["Your search for ("+word+") didn't return any results"]
    
    chul = [0 for _ in range(len(ans))]
    chul_2 = [0 for _ in range(len(ans))]
    chul_3 = [0 for _ in range(len(ans))]
    ck = [[] for _ in range(len(ans))]
    for i in range(len(ranking)):
        name, rank = ranking[i]
        if name == word: 
            chul[i] = 1
            answer.append(ans[i])
        else:
            for j in range(len(name) - len(word) + 1):
                if word == name[j:j+len(word)]:
                    chul_2[i] += 1
                    chul_3[i] = j               
            ck[chul_2[i]-1].append(chul_3[i])
        
    answer = ans
    return answer
    

data = ["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"]
word = "BROWN"
print(solution(data,word))