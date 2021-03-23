def solution(board):
    answer = 0

    wich = []
    wich.append([0,0,0,1,0])
    chk = {}

    while True:
        if len(wich) == 0:
            break
        x1,y1,x2,y2,cnt = wich.pop(0)
        hap = "{" + str(x1) + str(y1) + str(x2) + str(y2) +"}"
        if hap not in chk:
            chk[hap] = True
            #상하좌우
            if y1 + 1 < len(board[0]) and y2 + 1 < len(board[0]) and board[x1][y1+1] == 0 and board[x2][y2+1] == 0:
                wich.append([x1,y1+1,x2,y2+1,cnt+1])
            if x1 + 1 < len(board) and x2 + 1 < len(board) and board[x1+1][y1] == 0 and board[x2+1][y2] == 0:
                wich.append([x1+1,y1,x2+1,y2,cnt+1])
            if y1 - 1 >= 0 and y2 - 1 >= 0 and board[x1][y1-1] == 0 and board[x2][y2-1] == 0:
                wich.append([x1,y1-1,x2,y2-1,cnt+1])
            if x1 - 1 >= 0 and x2 - 1 >= 0 and board[x1-1][y1] == 0 and board[x2-1][y2] == 0:
                wich.append([x1-1,y1,x2-1,y2,cnt+1])        

            #회전(가로)
            if x1 == x2 and y1 < y2:
                if x1 - 1 >= 0 and y1 + 1 < len(board[0]) and board[x1-1][y1] == 0 and board[x1-1][y1+1] == 0:
                    wich.append([x1-1,y1+1,x2,y2,cnt+1])
                if x1 + 1 < len(board) and y1 + 1 < len(board[0]) and board[x1+1][y1] == 0 and board[x1+1][y1+1] == 0:
                    wich.append([x1+1,y1+1,x2,y2,cnt+1])
                if x2 - 1 >= 0 and y2 - 1 >= 0 and board[x2-1][y2] == 0 and board[x2-1][y2-1] == 0:
                    wich.append([x1,y1,x2-1,y2-1,cnt+1])
                if x2 + 1 < len(board) and y2 - 1 >= 0 and board[x2+1][y2] == 0 and board[x2+1][y2-1] == 0:
                    wich.append([x1,y1,x2+1,y2-1,cnt+1])

            #회전(가로)
            if x1 == x2 and y1 > y2:
                if x2 - 1 >= 0 and y2 + 1 < len(board[0]) and board[x2-1][y2] == 0 and board[x2-1][y2+1] == 0:
                    wich.append([x1,y1,x2-1,y2+1,cnt+1])
                if x2 + 1 < len(board) and y2 + 1 < len(board[0]) and board[x2+1][y2] == 0 and board[x2+1][y2+1] == 0:
                    wich.append([x1,y1,x2+1,y2+1,cnt+1])
                if x1 - 1 >= 0 and y1 - 1 >= 0 and board[x1-1][y1] == 0 and board[x1-1][y1-1] == 0:
                    wich.append([x1-1,y1-1,x2,y2,cnt+1])
                if x1 + 1 < len(board) and y1 - 1 >= 0 and board[x1+1][y1] == 0 and board[x1+1][y1-1] == 0:
                    wich.append([x1+1,y1-1,x2,y2,cnt+1])
                
            #회전(세로)
            if y1 == y2 and x1 > x2:
                if y2 + 1 < len(board[0]) and x2 + 1 < len(board) and board[x2][y2+1] == 0 and board[x2+1][y2+1] == 0:
                    wich.append([x1,y1,x2+1,y2+1,cnt+1])
                if y2 - 1 >= 0 and x2 + 1 < len(board) and board[x2][y2-1] == 0 and board[x2+1][y2-1] == 0:
                    wich.append([x1,y1,x2+1,y2-1,cnt+1])
                if y1 + 1 < len(board[0]) and x1 - 1 >= 0 and board[x1][y1+1] == 0 and board[x1-1][y1+1] == 0:
                    wich.append([x1-1,y1+1,x2,y2,cnt+1])
                if y1 - 1 >= 0 and x1 - 1 >= 0 and board[x1][y1-1] == 0 and board[x1-1][y1-1] == 0:
                    wich.append([x1-1,y1-1,x2,y2,cnt+1])

            #회전(세로)
            if y1 == y2 and x1 < x2:
                if y1 + 1 < len(board[0]) and x1 + 1 < len(board) and board[x1][y1+1] == 0 and board[x1+1][y1+1] == 0:
                    wich.append([x1+1,y1+1,x2,y2,cnt+1])
                if y1 - 1 >= 0 and x1 + 1 < len(board) and board[x1][y1-1] == 0 and board[x1+1][y1-1] == 0:
                    wich.append([x1+1,y1-1,x2,y2,cnt+1])
                if y2 + 1 < len(board[0]) and x2 - 1 >= 0 and board[x2][y2+1] == 0 and board[x2-1][y2+1] == 0:
                    wich.append([x1,y1,x2-1,y2+1,cnt+1])
                if y2 - 1 >= 0 and x2 - 1 >= 0 and board[x2][y2-1] == 0 and board[x2-1][y2-1] == 0:
                    wich.append([x1,y1,x2-1,y2-1,cnt+1])
                    
        if ((x1 == len(board) - 1 and y1 == len(board[0]) - 1) or (x2 == len(board) - 1 and y2 == len(board[0]) - 1)):
            answer = cnt
            break
    
    return  answer

board = [[0,0,1],[0,0,1],[0,1,0],[0,0,0],[0,0,0]]
print(solution(board))