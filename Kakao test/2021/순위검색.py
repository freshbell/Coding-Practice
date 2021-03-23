def solution2(info, query):
    answer = []
    
    for i in query:
        que = i.split(' ')
        cnt = 0
        for j in info:
            inj = j.split(' ')
            if (inj[0] == que[0] or que[0] == '-') and (inj[1] == que[2] or que[2] == '-') and (inj[2] == que[4] or que[4] == '-') and (inj[3] == que[6] or que[6] == '-') and (int(inj[4]) >= int(que[7])):
                cnt += 1
        answer.append(cnt)

    return answer


        
def solution(info, query):
    johap = {}

    for i in info:
        inf = i.split(" ")
        
        for j in range(16):
            hap = ""
            bi = list(bin(j))
            bi.pop(0)
            bi.pop(0)
            bi = ''.join(bi)
            bi = bi.rjust(4,"0")
            
            
            if bi[0] == '0': hap+="-"
            else: hap += inf[0]
            
            if bi[1] == '0': hap += "-"
            else: hap += inf[1]

            if bi[2] == '0': hap+="-"
            else: hap +=inf[2]

            if bi[3] == '0': hap+="-"
            else: hap +=inf[3]

            if hap not in johap: johap[hap] = []
            johap[hap].append(int(inf[4]))
            
    ans = []            
    answer = []
    for i in query:
        que = i.split(" ")
        hap = que[0] + que[2] + que[4] + que[6]
        ans = johap[hap]
        ans.sort()
        for j in range(len(ans)):
            if ans[j] >= int(que[7]):
                answer.append(len(ans) - j)
                break
    return answer



info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))


