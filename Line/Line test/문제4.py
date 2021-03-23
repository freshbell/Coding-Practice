def solution(maze):
    N = len(maze)
    answer = 0
    sangtae = 2 # 1 ~ 4 

    x,y = 0,0
    dx = [[0,0,0,0],[-1,0,1,0],[0,1,0,1],[1,0,-1,0],[0,-1,0,1]]
    dy = [[0,0,0,0],[0,1,0,-1],[1,0,-1,0],[0,-1,0,1],[-1,0,1,0]]
    sangtae_table = [[0,0,0,0],[4,1,2,3],[1,2,3,4],[2,3,4,1],[3,4,1,2]]
    count = 0

    while True:
        print(x,y)
        for i in range(4):
            if 0 <= x + dx[sangtae][i] < N and 0 <= y + dy[sangtae][i] < N and maze[x + dx[sangtae][i]][y + dy[sangtae][i]] == 0:
                x += dx[sangtae][i]
                y += dy[sangtae][i]
                sangtae = sangtae_table[sangtae][i]
                count += 1
                break
        
        if x == N - 1 and y == N - 1:
            break
    print(count)
    return answer

maze = [[0,0,0,0,0,0],[1,1,1,0,1,1],[0,0,0,0,0,0],[1,0,1,1,1,1],[0,0,0,0,0,0],[1,1,0,1,1,0]]
solution(maze)
