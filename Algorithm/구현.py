# 구현 유형
# 1. 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
# 2. 실수 연산을 다루고, 특정 소수점 자리까지 출력
# 3. 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
# 4. 적절한 라이브러리를 찾아서 사용해야 하는 문제

#방향 벡터
#상, 하, 좌, 우
dx = [0,0,-1,1] 
dy = [-1,1,0,0]

#우, 하, 좌, 상
dx = [1,0,-1,0]
dy = [0,1,0,-1]

#보는 방향에 따른 방향벡터(좌앞우뒤)
#   4
# 3   1
#   2
move_types = ['L','R','U','D']
sangtae_table = [[0,0,0,0],[4,1,2,3],[1,2,3,4],[2,3,4,1],[3,4,1,2]]
dx = [[0,0,0,0],[-1,0,1,0],[0,1,0,1],[1,0,-1,0],[0,-1,0,1]]
dy = [[0,0,0,0],[0,1,0,-1],[1,0,-1,0],[0,-1,0,1],[-1,0,1,0]]
# xx = x + dx[sangtae[1~4]][1~4] yy = y + dy[sangtae[1~4]][1~4]
a = 10


#시간 문제
N = int(input())
count = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)   
            if '3' in time:
                count += 1
            
print(count)

count = 0
for i in range(N+1):
    for j in range(0,6):
        for k in range(0,10):
            for l in range(0,6):
                for m in range(0,10):
                    if i == 3 or j == 3 or k == 3 or l == 3 or m == 3:
                        count += 1
print(count)


# 문자열 재정렬
ip = list(input())
ip.sort()
hap = 0
for i in range(len(ip)):
    if not ip[0].isalpha():
        hap += int(ip[0])
        ip.pop(0)
    else: break
ip += [str(hap)]
print(str(ip))