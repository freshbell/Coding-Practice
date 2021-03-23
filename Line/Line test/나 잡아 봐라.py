C, B = map(int, input().split())
gasok = 1
time = 0
C_wich = []
B_wich = []
C_wich.append(C)
B_wich.append([0,B])

while True:
    if C > 200000: break
    time += 1
    C += time
    C_wich.append(C)

while True:
    [time, B] = B_wich.pop(0)
    if C_wich[time] > 200000:
        time = -1
        break
    if C_wich[time] == B: break
    
    if B > 0 : B_wich.append([time+1,B-1])
    if B + 1 <= 200000: B_wich.append([time+1,B+1])
    if B*2 <= 200000: B_wich.append([time+1,B*2])

print(time)