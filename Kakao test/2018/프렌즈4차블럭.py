def down(m, n, board):
    for i in range(m-1,0,-1):
        for j in range(n):
            if board[i][j] == "0":
                for k in range(i-1,-1,-1):
                    if board[k][j] != "0":
                        board[i][j] = board[k][j]
                        board[k][j] = "0"
                        break

import collections
def search(m,n,board):
    chk = [[0 for i in range(n)] for j in range(m)]
    ck = 0
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == board[i][j+1] and board[i+1][j+1] == board[i][j] and board[i+1][j] == board[i][j] and board[i][j] != "0":
                chk[i][j] = chk[i][j+1] = chk[i+1][j+1] = chk[i+1][j] = 1

    for i in range(m):
        for j in range(n):
            if chk[i][j] == 1:
                board[i][j] = "0"
                ck += 1

    return ck

def solution(m, n, board):
    answer = 0
    erase = 0
    for i in range(m):
        board[i] = list(board[i])

    while True:
        erase = search(m,n,board)
        if erase == 0: break
        down(m,n,board)
        answer += erase
        
    return answer

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m,n,board))