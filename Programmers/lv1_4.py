def solution(answers):
    answer = []
    people = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    num = [5,8,10]
    length = len(answers)
    chk = [0,0,0]
    max = 0
    
    for i in range(3):
        people[i] *= (length//num[i] + 1)
        
        for j in range(length):
            if people[i][j] == answers[j]:
                chk[i] += 1
            
            if max < chk[i]:
                max = chk[i]
    
    for i in range(3):
        if max == chk[i]:
            answer.append(i+1)
    
    return answer

for a, b in enumerate([1,2,3,4,5]):
    print(a,b)

p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

for i, v in enumerate(p):
    print(i,v)