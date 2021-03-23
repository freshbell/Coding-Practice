from collections import deque

moves = [(-1,0),(1,0),(0,-1),(0,1)]

def solution(board, r, c):
    k = 1
    idx = {}
    idx_to_kind = {}
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                idx[(i,j)] = k
                idx_to_kind[k] = board[i][j]
                k += 1
    q = deque([(0,r,c,0,0)]) # bit 0 : existed, 1 : deleted / num of front now (0 : nothing, 1~ : k)

    dp = [ [ [ [ 100000000 for _ in range(13) ] for _ in range(2**13) ] for _ in range(4) ] for _ in range(4) ]
    while q:
        cnt, x, y, bit, front = q.popleft()
        if bit == 2**k-2:
            break
        if board[x][y] != 0:
            if front == 0:
                if cnt+1 < dp[x][y][bit][idx[(x,y)]]:
                    q.append((cnt+1,x,y,bit,idx[(x,y)]))
                    dp[x][y][bit][idx[(x,y)]] = cnt+1
            elif board[x][y] == idx_to_kind[front] and front != idx[(x,y)]:
                bit_cand = bit|2**front|2**idx[(x,y)]
                if cnt+1 < dp[x][y][bit_cand][0]:
                    q.append((cnt+1,x,y,bit_cand,0))
                    dp[x][y][bit_cand][0] = cnt+1

        for mx, my in moves:
            if 0 <= x+mx < 4 and 0 <= y+my < 4:
                if cnt+1 < dp[x+mx][y+my][bit][front]:
                    q.append((cnt+1,x+mx,y+my,bit,front))
                    dp[x+mx][y+my][bit][front] = cnt+1

            moved = False
            for t in [1,2,3]:
                if 0 <= x+t*mx < 4 and 0 <= y+t*my < 4:
                    if board[x+t*mx][y+t*my] != 0 and not bit&2**idx[(x+t*mx,y+t*my)]:
                        if cnt+1 < dp[x+t*mx][y+t*my][bit][front]:
                            q.append((cnt+1,x+t*mx,y+t*my,bit,front))
                            dp[x+t*mx][y+t*my][bit][front] = cnt+1
                        moved = True
                        break
            if not moved:
                for t in [3,2,1]:
                    if 0 <= x+t*mx < 4 and 0 <= y+t*my < 4:
                        if board[x+t*mx][y+t*my] == 0 or bit&2**idx[(x+t*mx,y+t*my)]:
                            if cnt+1 < dp[x+t*mx][y+t*my][bit][front]:
                                q.append((cnt+1,x+t*mx,y+t*my,bit,front))
                                dp[x+t*mx][y+t*my][bit][front] = cnt+1
                            break

    return cnt