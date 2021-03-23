def back(wich, start, select, fixman, weak): # 사람선택, 시작위치, 최대 선택 칸, solution에서 뽑힌 사람, 순열
    hap = 0
    if wich <= len(fixman) - 1:
        for j in range(start, start + select):
            if wich > 0 : # wich가 0이 아니면 전꺼랑 이어서 연결되야 하므로 시작위치 못바꾸게 break
                if j > start: break
            for k in range(select - 1,-1,-1): #최대 선택 칸 ~ 자기자신
                
                hap = weak[j + k] - weak[j] #두 지점간의 거리
                if hap <= fixman[wich] :
                    #print(j+k,j,hap,fixman[wich],wich)
                    if back(wich+1, j + k + 1, select - (k+1),fixman,weak):
                        return True
    elif wich > len(fixman) - 1 and select == 0: return True # 조건 만족하면 return
    
    return False

def solution(n, weak, dist):
    answer = -1
    fix = len(weak) #고쳐야 할 곳
    people = len(dist) #사람 인원
    dist.sort() #dist정렬

    for i in range(fix):
        weak.append(weak[i]+n) #순열
    weak.pop(-1)
    print(weak)
    # dist가 큰 인원으로 1~N까지 뽑기
    for i in range(people-1,-1,-1): 
        if back(0,0,fix,dist[i:people],weak):
            answer = len(dist[i:people])
            break

    return answer


N = 200
weak = [i for i in range(N)]
dist = [200]

print(solution(N,weak,dist))

# 0 35 30 65