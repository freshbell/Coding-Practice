def solution(board):
    answer = 0
    que = [[0,0,0,1,0]]
    N = len(board)
    check = {}
    while que:
        [x1, y1, x2, y2, cnt] = que.pop(0)
        if str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) in check: continue
        check[str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2)] = True
        
        if (x1 + 1 == N and y1 + 1 == N) or (x2 + 1 == N and y2 + 1 == N):
            answer = cnt
            break

        if y2 + 1 < N and board[x1][y1 + 1] == 0 and board[x2][y2 + 1] == 0:
            que.append([x1,y1+1,x2,y2+1,cnt + 1])
        if y1 - 1 >= 0 and board[x1][y1 - 1] == 0 and board[x2][y2 - 1] == 0:
            que.append([x1,y1-1,x2,y2-1,cnt + 1])
        if x2 + 1 < N and board[x1+1][y1] == 0 and board[x2+1][y2] == 0:
            que.append([x1+1,y1,x2+1,y2,cnt + 1])
        if x1 - 1 >= 0 and board[x1-1][y1] == 0 and board[x2-1][y2] == 0:
            que.append([x1-1,y1,x2-1,y2,cnt + 1])

        if x1 == x2:
            if x1 + 1 < N and board[x1+1][y1] == 0 and board[x1+1][y1+1] == 0:
                que.append([x2,y2,x1+1,y1+1,cnt+1])
            if x1 - 1 >= 0 and board[x1-1][y1] == 0 and board[x1-1][y1+1] == 0:
                que.append([x1-1,y1+1,x2,y2,cnt+1])
            if x2 + 1 < N and board[x2+1][y2] == 0 and board[x2+1][y2-1] == 0:
                que.append([x1,y1,x2+1,y2-1,cnt+1])
            if x2 - 1 >= 0 and board[x2-1][y2] == 0 and board[x2-1][y2-1] == 0:
                que.append([x2-1,y2-1,x1,y1,cnt+1])
        elif y1 == y2:
            if y1 + 1 < N and board[x1][y1+1] == 0 and board[x1+1][y1+1] == 0:
                que.append([x2,y2,x1+1,y1+1,cnt+1])
            if y1 - 1 >= 0 and board[x1][y1-1] == 0 and board[x1+1][y1-1] == 0:
                que.append([x1+1,y1-1,x2,y2,cnt+1])
            if y2 + 1 < N and board[x2][y2+1] == 0 and board[x2-1][y2+1] == 0:
                que.append([x1,y1,x2-1,y2+1,cnt+1])
            if y2 - 1 >= 0 and board[x2][y2-1] == 0 and board[x2-1][y2-1] == 0:
                que.append([x2-1,y2-1,x1,y1,cnt+1])
    
    return answer

board = [[0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
print(solution(board))
