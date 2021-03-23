def search(board,i,j):
    if i + 1 < len(board) and (j+1 == len(board[i]) or board[i][j+1] != board[i][j]) and (j == 0 or board[i][j-1] != board[i][j]): #최소 가능조건
        if (i+2 < len(board) and j-1 >= 0 and j+1 < len(board[i])) and board[i+1][j] == board[i][j] and board[i+2][j] == board[i][j] and (board[i+1][j-1] == board[i][j] or board[i+1][j+1] == board[i][j]):
            return False
        return True
    return False

def check(board,x,j1,j2):
    for i in range(x,-1,-1):
        if board[i][j1] != 0 or board[i][j2] != 0:
            return False

    return True

def solution(board):
    answer = 0
    i = j = 0

    while True:
        if i == len(board):
                break
        while True:
            if j == len(board[i]):
                j = 0
                break
            if board[i][j] != 0:
                if search(board,i,j) == True:
                    if (j >= 1 and j < len(board[i])-1 and i+1 < len(board)) and board[i+1][j-1] == board[i][j] and board[i+1][j+1] == board[i][j]:
                        if check(board,i,j-1,j+1):
                            board[i][j] = board[i+1][j] = board[i+1][j-1] = board[i+1][j+1] = 0
                            i = -1
                            answer+=1
                            break
                    elif i + 2 < len(board) and board[i+2][j] == board[i][j]:
                        if j+1 < len(board[i]) and board[i+2][j+1] == board[i][j]:
                            if check(board,i+1,j+1,j+1):
                                board[i][j] = board[i+1][j] = board[i+2][j] = board[i+2][j+1] = 0
                                i = -1
                                answer+=1
                                break
                        if j > 0 and board[i+2][j-1] == board[i][j]:
                            if check(board,i+1,j-1,j-1):
                                board[i][j] = board[i+1][j] = board[i+2][j] = board[i+2][j-1] = 0
                                i = -1
                                answer+=1
                                break
                    elif i + 1 < len(board) and board[i+1][j] == board[i][j]:
                        if j+2 < len(board[i]) and board[i+1][j+1] == board[i][j] and board[i+1][j+2] == board[i][j]:
                            if check(board,i,j+1,j+2):
                                board[i][j] = board[i+1][j] = board[i+1][j+1] = board[i+1][j+2] = 0
                                i = -1
                                answer+=1
                                break
                        if j > 1 and board[i+1][j-1] == board[i][j] and board[i+1][j-2] == board[i][j]:
                            if check(board,i,j-1,j-2):
                                board[i][j] = board[i+1][j] = board[i+1][j-1] = board[i+1][j-2] = 0
                                i = -1
                                answer+=1
                                break
                                
            j = j + 1
        i = i + 1
    return answer

board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[1,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,6,0,5],[1,1,0,0,0,0,6,6,6,5]]

board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,2,2,0,0,0,0,0],[0,0,0,2,1,0,0,0,0,0],[0,0,0,2,1,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
board = [[1,2,2,2],[1,1,1,2],[0,3,0],[3,3,3,0]]

board = [[2,0,0],[0,1,0],[1,1,1]]
board = [[0, 2, 0, 0], [1, 2, 0, 4], [1, 2, 2, 4], [1, 1, 4, 4]]
board = [[0,1,0],[1,1,0],[0,1,0]]
print(solution(board))
