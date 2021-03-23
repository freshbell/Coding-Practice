from copy import deepcopy

N = eval(input())
pan = []
maximum = 0

for i in range(N):
    line = list(map(int,input().split()))
    pan.append(line)
    maxim = max(line)
    maximum = max(maximum,maxim)

g = []
g.append((pan,0))

def convert(now):
    global maximum
    conv = deepcopy(now)

    for i in range(N):
        for j in range(N):
            if conv[j][i] == 0:
                for k in range(i+1,N):
                    if conv[j][k] != 0:
                        conv[j][i] = conv[j][k]
                        conv[j][k] = 0
                        break
    
    for i in range(N-1):
        for j in range(N):
            if conv[j][i] == conv[j][i+1]:
                conv[j][i] *= 2
                conv[j][i+1] = 0
                for k in range(i+1,N-1):
                    conv[j][k] = conv[j][k+1]
                    conv[j][k+1] = 0

            maximum = max(maximum,conv[j][i])

    return conv

def rotate_pan(now):
    rotate = deepcopy(now)

    for i in range(N):
        for j in range(N):
            rotate[j][N-1-i] = now[i][j]

    return rotate

while g:
    now, count = g.pop(0)
    if count == 5: break

    for i in range(4):
        conv = convert(now)
        g.append((conv,count+1))
        now = rotate_pan(now)
        

print(maximum)