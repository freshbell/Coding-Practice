Test = int(input())

for case in range(Test):
    month, day, week = map(int,input().split())

    next_day = day
    line = 0
    for i in range(1, month + 1):
        line += next_day // week
        if next_day % week > 0:
            if i != month: line += 2
            else: line += 1
            next_day = day - (week - next_day % week)
        else:
            next_day = day

    print("Case #" + str(case+1) +": " + str(line))
