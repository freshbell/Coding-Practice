que = []
chk = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
maximum = 0

def find(y1,x1,y2,x2,board,cnt):
    if board[x1][y1] == board[x2][y2] and x1 != x2 and y1 != y2:
        if maximum < cnt:
            maximum = cnt
    else:
        for i in range(x1-1,-1,-1):
            if board[y1][i] != 0:
                chk[y1][i] = 1
                find(y1,i,y2,x2,board,cnt+1)
                chk[y1][i] = 0
            if i == 0:
                chk[y1][0] = 1
                find(y1,0,y2,x2,board,cnt+1)
                chk[y1][0] = 1
        for i in range(x1+1,4):
            if board[y1][i] != 0:
                chk[y1][i] = 1
                find(y1,i,y2,x2,board,cnt+1)
                chk[y1][i] = 0
            if i == 3:
                chk[y1][3] = 1
                find(y1,3,y2,x2,board,cnt+1)
                chk[y1][3] = 0
        for i in range(y1-1,-1,-1):
            if board[i][x1] != 0:
                chk[i][x1] = 1
                find(i,x1,y2,x2,board,cnt+1)
                chk[i][x1] = 0
            if i == 0:
                chk[0][x1] = 1
                find(0,x1,y2,x2,board,cnt+1)
                chk[0][x1] = 0
        for i in range(y1+1,4):
            if board[i][x1] != 0:
                chk[i][x1] = 1
                find(i,x1,y2,x2,board,cnt+1)
                chk[i][x1] = 0
            if i == 3:
                chk[i][x1] = 1
                find(3,x1,y2,x2,board,cnt+1)
                chk[i][x1] = 1
        if y1 > 0 and chk[y1-1][x1] == 0: 
            chk[y1-1][x1] = 1
            find(y1-1,x1,y2,x2,board,cnt+1)
            chk[y1-1][x1] = 0
        if y1 < 3 and chk[y1+1][x1] == 0: 
            chk[y1+1][x1] = 1
            find(y1+1,x1,y2,x2,board,cnt+1)
            chk[y1+1][x1] = 0
        if x1 > 0 and chk[y1][x1-1] == 0: 
            chk[y1][x1-1] = 1
            find(y1,x1-1,y2,x2,board,cnt+1)
            chk[y1][x1-1] = 0
        if x1 < 3 and chk[y1][x1+1]: 
            chk[y1][x1+1] = 1
            find(y1,x1+1,y2,x2,board,cnt+1)
            chk[y1][x1+1] = 0

def solution(board, r, c):
    answer = 0
    find(0,0,0,0,board,0)
    print(maximum)

    return answer

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0
print(solution(board,r,c))
