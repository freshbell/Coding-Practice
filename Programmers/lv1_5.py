import collections

def solution(N, stages):
    answer = []
    challengers = len(stages)
    stages.append(N+1)
    challenge = collections.Counter(stages)
    fail = []

    
    for i in range(1,N + 1):
        fail.append([i,challenge[i]/challengers])
        challengers -= challenge[i]
        if challengers == 0:
            challengers = 1
    
    fail.sort(key = lambda x:(x[1],-x[0]))
    fail.reverse()

    for i in range(N):
        answer.append(fail[i][0])

    return answer


solution(5,[2, 1, 2, 6, 2, 4, 3, 3])