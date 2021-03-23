import collections

# counter이용
def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    return list(answer.keys())[0]

# 해시
def solution3(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))

    for com in completion:
        temp -= hash(com)

    answer = dic[temp]

    return answer

# 내가 푼방식
def solution(participant, completion):
    #answer = ''

    participant.sort()
    completion.sort()

    print(participant)
    print(completion)

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]


participant = ["kiki", "kiki", "eden","eden","A","B","C","E"]
completion = ["eden", "kiki","eden","A","B","C","kiki"]

solution(participant, completion)
solution2(participant,completion)
solution3(participant,completion)