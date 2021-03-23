def solution(dartResult):
    answer = 0
    jumsu = []
    wich = -1

    dartResult = list(dartResult)

    for wi in range(len(dartResult)):
        i = dartResult[wi]
        if i >= '0' and i <= '9':
            if i == '1' and dartResult[wi+1] == '0':
                wich+=1
                jumsu.append(10)
            elif i == '0' and dartResult[wi-1] == '1': continue
            else :
                wich += 1
                jumsu.append(int(i))
        elif i == 'S': continue            
        elif i == 'D': jumsu[wich] **= 2
        elif i == 'T': jumsu[wich] **= 3
        elif i == '*': 
            jumsu[wich] *= 2
            if wich != 0: 
                jumsu[wich-1] *= 2
        elif i == '#': jumsu[wich] *= -1

    print(jumsu)
    for i in jumsu:
        answer += i

    return answer

dartResult = '1D2S#10S'
solution(dartResult)