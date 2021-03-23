def solution(n, build_frame):
    n += 1
    answer = []
    build = [[0 for i in range(n)] for j in range(n)]

    for i in build_frame:
        y,x,a,b=i

        chk = 0
        #조건 확인
        if b == 1: #설치 조건
            if a == 0: #기둥
                if x == 0: chk = 1
                elif x - 1 >= 0 and (build[x-1][y] == 1 or build[x-1][y] == 3): chk = 1
                elif y - 1 >= 0 and (build[x][y-1] == 2 or build[x][y-1] == 3): chk = 1
            else: #보
                if x-1 >= 0 and (build[x-1][y] == 1 or build[x-1][y] == 3): chk = 1
                elif (x-1 >= 0 and y + 1 < n) and (build[x-1][y+1] == 1 or build[x-1][y+1] == 3): chk = 1
                elif (y-1 >= 0 and y+1 < n) and (build[x][y-1] >= 2) and (build[x][y+1] >= 2): chk = 1
        else: #삭제 조건
            if a == 0: #기둥
                if x+1 < n and (build[x+1][y] == 1): #위에 기둥만
                    if (build[x+1][y-1] >= 2 and (build[x][y-1] == 1 or build[x][y-1] == 3)) or (build[x+1][y] and (build[x][y+1] == 1 or build[x][y+1] == 3)) == 2: chk = 1
                elif x+1 < n and (build[x+1][y] == 2): #위에 보만
                    if y+1 < n and (build[x][y+1] == 1 or build[x][y+1] == 3): chk = 1
                    elif y-1 >= 0 and (build[x+1][y-1] >= 2) and build[x+1][y+1] >= 2: chk = 1
                elif x+1 < n and (build[x+1][y] == 3): #위에 둘다
                    if (build[x+1][y-1] >= 2 and (build[x][y-1] == 1 or build[x][y-1] == 3)) or (build[x+1][y] and (build[x][y+1] == 1 or build[x][y+1] == 3)) == 2:
                        if y+1 < n and (build[x][y+1] == 1 or build[x][y+1] == 3): chk = 1
                        elif y-1 >= 0 and (build[x+1][y-1] >= 2) and build[x+1][y+1] >= 2: chk = 1
            else: #보
                if (y-1 >= 0 and y+1 < n) and (build[x][y-1] >= 2) and (build[x][y+1] >= 2): #양쪽에 보
                    if (x-1 >= 0 and y-1 >=0 and y+1 < n) and (build[x-1][y-1] == 1 or build[x-1][y-1] == 3) and ((build[x-1][y+1] == 1 or build[x-1][y+1] == 3)): chk = 1
                    elif (x-1 >= 0 and y-1 >=0 and y+2 < n) and (build[x-1][y-1] == 1 or build[x-1][y-1] == 3) and (build[x-1][y+2] == 1 or build[x-1][y+2] == 3): chk = 1
                elif (y-1>=0) and (build[x][y-1] >= 2): #왼쪽만 보
                    if (x-1>=0 and y-1>=0) and ((build[x-1][y-1] == 1 or build[x-1][y-1] == 3) or (build[x-1][y] == 1 or build[x-1][y] == 3)): chk = 1
                elif (y+1 < n) and (build[x][y+1] >= 2): #오른쪽만 보
                    if (x-1>=0 and y + 1 < n) and (build[x-1][y+1] == 1 or build[x-1][y+1] == 3): chk = 1
                    if (x-1>=0 and y + 2 < n ) and (build[x-1][y+2] == 1 or build[x-1][y+2] == 3): chk = 1
                elif (y+1 < n and x-1 >= 0) and (build[x][y+1] == 1 or build[x][y+1] == 3) and (build[x-1][y+1] == 1 or build[x-1][y+1] == 3): chk = 1 #오른쪽 위 기둥
                elif (y+1 < n and y-1 >= 0 and x-1 >= 0) and (build[x][y] == 1 or build[x][y] == 3) and (build[x][y-1] >= 2): chk = 1 #바로 위 기둥
                
        if chk == 1:
            if b == 1: #설치
                if a == 0: #기둥
                    build[x][y] += 1
                else: # 보
                    build[x][y] += 2
            else: # 삭제
                if a == 0:
                    build[x][y] -= 1
                else:
                    build[x][y] -= 2

    for i in range(n):
        for j in range(n):
            if build[i][j] == 1:
                answer.append([j,i,0])
            elif build[i][j] == 2:
                answer.append([j,i,1])
            elif build[i][j] == 3:
                answer.append([j,i,0])
                answer.append([j,i,1])

    answer.sort()
    return answer

n = 8
build_frame = 	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1],[2,1,0,1],[2,0,0,1],[1,1,1,0],[2,2,1,1],[3,1,0,1],[2,1,0,0],[5,0,0,1],[6,0,0,1],[4,1,1,1],[5,1,1,1],[4,0,0,0],[5,0,0,0],[4,1,1,0]]
print(solution(n,build_frame))

a= {}
a["[1,2,3]"] = 1
a["3,4,5"] = 2

b = a.keys()
print(b)