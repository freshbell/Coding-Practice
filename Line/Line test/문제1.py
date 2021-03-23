
def solution(boxes):
    boxNumber = len(boxes)
    dic = {}

    for i in boxes:
        if i[0] not in dic: dic[i[0]] = 0
        if i[1] not in dic: dic[i[1]] = 0
        dic[i[0]] += 1
        dic[i[1]] += 1

    box = 0
    for i in dic:
        box += dic[i] // 2
        dic[i] %= 2
    print(dic)

    answer = 0
    if box == boxNumber: answer = 0
    else:
        for i in dic:
            if dic[i] != 0:
                answer += 1
                box += 1
            if box == boxNumber: break

    return answer

boxes = [[1,2],[1,2],[1,2],[1,2],[3,4],[4,5],[3,3]]
print(solution(boxes))