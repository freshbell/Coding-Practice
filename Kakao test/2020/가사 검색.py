def solution(words, queries):
    answer = []
    
    for i in queries:
        cnt = 0
        cnt_que = i.count('?')
        len_words = len(i)
        for j in words:
            if len(j) == len(i):
                if i[0] == '?':
                    if i[cnt_que:len_words] == j[cnt_que:len_words]:
                        cnt += 1
                else:
                    if i[0:len_words - cnt_que] == j[0:len_words - cnt_que]:
                        cnt += 1
        answer.append(cnt)

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["?????", "????o", "fr???", "fro???", "pro?"]

print(solution(words,queries))