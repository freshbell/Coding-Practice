def solution(table, languages, preference):
    answer = []
    gye = [0 for _ in range(5)]
    jikgoon = []

    for i in range(len(languages)):
        for j in range(len(table)):
            a = list(table[j].split())
            if i == 0:
                jikgoon.append(a[0])
            if languages[i] in a:
                for k in range(len(a)):
                    if languages[i] == a[k]:
                        gye[j] += preference[i] * (6-k)
    maximum = max(gye)
    for i in range(len(gye)):
        if maximum == gye[i]:
            answer.append(jikgoon[i])
            
    answer.sort()        
    return answer[0]

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]
print(solution(table,languages,preference))