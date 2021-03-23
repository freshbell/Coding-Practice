def solution(board, moves):
    array = []
    answer = 0
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                array.append(board[j][i-1])
                board[j][i-1] = 0

                if len(array) > 1:
                    if array[-1] == array[-2]:
                        array.pop(-1)
                        array.pop(-1)
                        answer += 2
                    
                break
    
    return answer


#test case
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))