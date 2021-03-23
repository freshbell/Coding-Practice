def solution(n, weak, dist):
    answer = 0

    length = []
    johap = [[0 for j in range(len(weak))] for i in range(len(weak)-1)]
    people = node = len(weak) - 1
    jjak = len(dist)/2
    minimum = 9999

    for i in range(len(weak)):
        if i == len(weak) - 1:
            length.append(n - weak[i] + weak[0])
        else: length.append(weak[i+1] - weak[i])

    for i in range(1,len(weak)):
        for j in range(len(weak)):
            for k in range(j, j+i):
                johap[i-1][j] += length[k%len(length)]
    print(johap)
    while node > 0:
        for j in range(len(weak)):
            if minimum > johap[people-1][j]:
                minimum = johap[people-1][j]
                johap[people-1][j] = 9999
        #print(minimum,dist[-1])
        if minimum <= dist[-1]:
            node -= people
            dist.pop(-1)
            answer += 1
        else:
            people -= 1

        if answer > jjak:
            answer = jjak
            break

        if node == 0:
            break
        

    #print(answer)
    return answer

n = 12	
weak = [1, 3, 4, 9, 10]	
dist = [1, 2, 3, 4]

solution(n,weak,dist)
