def solution(n, t, m, timetable):
    answer = ''

    start = 540
    crew_time = []
    bus_time = []
    chk_jungwon = {}
    chk_wich = {}

    for i in range(1,n+1):
        chk_jungwon[start] = 0
        bus_time.append(start)
        start += t

    for i in timetable:
        crew_time.append(int(i[0:2])*60 + int(i[3:5]))

    crew_time.sort()

    wich = 0
    for i in crew_time:
        for j in bus_time:
            if i <= j and chk_jungwon[j] < m:
                chk_jungwon[j] += 1
                chk_wich[wich] = j
                wich += 1
                break

    for i in bus_time[::-1]:
        if chk_jungwon[i] < m:
            answer = i
            break
        else:
            answer = crew_time[list(chk_wich.keys())[-1]]-1
            break
    
    dap = ""
    if int(answer/60) < 10:
        dap += "0" + str(int(answer/60)) + ":"
    else:
        dap += str(int(answer/60)) + ":"

    if int(answer%60) < 10:
        dap += "0" + str(int(answer%60))
    else:
        dap += str(int(answer%60))
    answer = dap
    return answer

n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03","08:04"]
print(solution(n,t,m,timetable))