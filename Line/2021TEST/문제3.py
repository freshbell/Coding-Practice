def solution(enter, leave):
    answer = []
    room = []
    count = [0 for _ in range(len(enter))]

    while leave:
        if len(enter) > 0: room.append(enter.pop(0))
        if len(room) > 1: 
            for i in room:
                count[i-1] += 1
        count[room[-1]-1] = len(room) - 1

        while True:
            chk = True
            for i in range(len(room)):
                if leave[0] == room[i]:
                    leave.pop(0)
                    room.pop(i)
                    chk = False
                    break
            if chk == True: break
    answer = count
    return answer

enter = [3,1,4,2]
leave = [1,2,4,3]
print(solution(enter, leave))