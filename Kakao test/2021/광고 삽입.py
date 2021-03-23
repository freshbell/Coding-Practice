def solution(play_time, adv_time, logs):
    answer = ''
    play = play_time.split(":")
    play = int(play[0])*3600 + int(play[1])*60 + int(play[2])
    table = [0 for _ in range(play+1)]
    
    adv = adv_time.split(":")
    adv = int(adv[0])*3600 + int(adv[1])*60 + int(adv[2])

    for i in logs:
        time = i.split("-")
        start = time[0].split(":")
        start = int(start[0])*3600 + int(start[1])*60 + int(start[2])

        end = time[1].split(":")
        end = int(end[0])*3600 + int(end[1])*60 + int(end[2])

        table[start] += 1
        table[end] -= 1


    for i in range(1,play+1):
        table[i] += table[i-1]

    cnt = 0
    for i in range(0,adv):
        cnt += table[i]
    maximum = cnt
    wich = 0
    
    for i in range(1,play - adv + 1):
        cnt = cnt - table[i-1] + table[i+adv - 1]
        if maximum < cnt:
            maximum = cnt
            wich = i
    
    answer = str(int(wich/3600)).rjust(2,"0")
    answer += ":" + str(int(int(wich%3600)/60)).rjust(2,"0")
    answer += ":" + str(int(int(wich%3600)%60)).rjust(2,"0")
    return answer

play_time = "99:59:59"
adv_time = 	"25:00:00"
logs = 	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
print(solution(play_time,adv_time,logs))