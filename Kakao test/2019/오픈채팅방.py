def solution(record):
    dic = {}
    answer = []
    record = record[::-1]
    wich = []
    
    for i in record:
        nanugi = i.split(' ')
     
        if nanugi[0] == "Enter":
            if nanugi[1] in dic:
                answer.append(dic[nanugi[1]] + "님이 들어왔습니다.")
            else:
                dic[nanugi[1]] = nanugi[2]
                wich.append(len(answer))
                answer.append(nanugi[1] + " Enter")
        elif nanugi[0] == "Leave":
            if nanugi[1] in dic:
                answer.append(dic[nanugi[1]] + "님이 나갔습니다.")
            else :
                wich.append(len(answer))
                answer.append(nanugi[1] + " Leave")
        else :
            if nanugi[1] not in dic:
                dic[nanugi[1]] = nanugi[2]

    for i in wich:
        nanugi = answer[i].split(' ')
        if nanugi[1] == "Leave":
            answer[i] = dic[nanugi[0]] + "님이 나갔습니다."
        else:
            answer[i] = dic[nanugi[0]] + "님이 들어왔습니다."

    return answer[::-1]

record = ["Enter 1 Muzi", "Change 1 leon", "Leave 1","Enter 1 CC"]
#record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan","Leave uid4567","Change uid1234 Muzi","Enter uid1234 FF","Enter u CC"]

print(solution(record))