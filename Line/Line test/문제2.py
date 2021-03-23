def solution(ball, order):
    answer = []
    dic = {}

    for i in order:
        if ball[0] == i:
            ball.pop(0)
            answer.append(i)
            while len(ball) > 0 and ball[0] in dic:
                answer.append(ball[0])
                ball.pop(0)
        elif ball[-1] == i:
            ball.pop(-1)
            answer.append(i)
            while len(ball) > 0 and  ball[-1] in dic:
                answer.append(ball[-1])
                ball.pop(-1)
        else:
            dic[i] = True
        
    return answer

ball = [11,2,9,13,24]
order = [9,2,13,24,11]
print(solution(ball, order))