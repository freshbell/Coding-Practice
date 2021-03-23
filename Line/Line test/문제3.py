def solution(n):
    st = str(n)
    stLen = len(st)

    count = 0
    while stLen > 1:
        count += 1
        rban = lban = stLen // 2
        
        chk = 0
        while st[lban] == '0' or st[rban] == '0':
            chk = 1
            if st[lban] == '0': lban -= 1 
            if st[rban] == '0': rban += 1

        a = st[0:lban]
        b = st[lban:]
        c = st[0:rban]
        d = st[rban:]
        
        if len(a) == 0: a = '0'
        if len(d) == 0: d= '0'

        if len(str(eval(a) + eval(b))) > len(str(eval(c) + eval(d))): st = str(eval(c) + eval(d))
        else: st = str(eval(a) + eval(b))
        stLen = len(st)

    answer = []
    answer.append(count)
    answer.append(eval(st))
    return answer

n = 1190007999
print(solution(n))