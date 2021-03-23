def rotate(key):
    N = len(key)
    x=0; y=0
    temp = [[0 for i in range(N)] for j in range(N)]

    rotate = [[0,1],[-1,0]]

    for i in range(N):
        for j in range(N):
            x = rotate[0][0] * i + rotate[0][1] * j
            y = rotate[1][0] * i + rotate[1][1] * j
            temp[i][j] = key[x][y+1]

    return temp

def move(key,wich):
    N = len(key)
    
    if wich == 1:
        for i in range(N - 1):
            key[i] = key[i+1]
        key[N-1] = [0 for i in range(N)]
    elif wich == 2:
        for i in range(N):
            for j in range(N - 1):
                key[i][j] = key[i][j+1]
                key[i][j+1] = 0
    elif wich == 3:
        for i in range(N-1,0,-1):
            key[i] = key[i-1]
        key[0] = [0 for i in range(N)]
    elif wich == 4:
        for i in range(N):
            for j in range(N-1,0,-1):
                key[i][j] = key[i][j-1]
                key[i][j-1] = 0
    
    return key

def process(key,lock,edong):
    N = len(key)

    if check(key,lock):
        return True

    if edong[0] < 4:
        edong[0] += 1
        print(key)
        print(edong)
        process(rotate(key),lock,edong)
        print(key)
        edong[0] -= 1
    if edong[1] < N -1:
        edong[1] += 1
        process(move(key,1),lock,edong)
        edong[0] -= 1
    if edong[2] < N -1:
        edong[2] += 1
        process(move(key,2),lock,edong)
        edong[0] -= 1
    if edong[3] < N -1:
        edong[3] += 1
        process(move(key,3),lock,edong)
        edong[0] -= 1
    if edong[4] < N -1:
        edong[4] += 1
        process(move(key,4),lock,edong)
        edong[0] -= 1

    return False
        

def check(key,lock):
    for i in range(len(key)):
        key[i] = list(map(lambda x:1 if x == 0 else 0,key[i]))

    for i in range(len(lock) - len(key) + 1):
        for j in range(len(lock) - len(key) + 1):
            if lock[i:i+len(key)][j:j+len(key)] == key[i:i+len(key)][j:j+len(key)]:
                return True

    for i in range(len(key)):
        key[i] = list(map(lambda x:1 if x == 0 else 0,key[i]))

    return False


def solution(key, lock):
    answer = True
    answer = process(key,lock,[0,0,0,0,0])
    print(answer)
    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
temp = 0