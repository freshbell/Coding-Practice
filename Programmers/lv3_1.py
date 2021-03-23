#참고
def solution3(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))





def match(p):
    count = 0
    chk = True

    for i in p:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            chk = False
            break
    
    if count > 0:
        chk = False
    return chk

def divide(p):
    rSen = ''
    wSen = ''
    count = 0

    for i in range(len(p)):
        if p[i] == '(':
            rSen += p[i]
            count += 1
        else:
            rSen += p[i]
            count -= 1

        if count == 0:
            wSen = p[i+1:]
            break

    return rSen,wSen



def right(u,v):
    #print(u,v)
    gap = ''
    if match(u):
        if not v =="":
            rSen, wSen = divide(v)
            gap = right(rSen,wSen)
        return u + gap
    else:
        add = "("
        rSen, wSen = divide(v)
        add += right(rSen,wSen)
        add += ")"
        for j in range(1,len(u) - 1):
            if u[j] == "(":
                add+=")"
            else:
                add+="("
        
        return add
    

def solution(p):
    if p == '':
        return ''

    chk = match(p)
    if chk :
        return p
    else:
        u,v = divide(p)
        return right(u,v)

#p = ")()()("
#print(solution(p))



def solution2(p):
    answer = ''
    
    right = []
    wrong = []
    count = 0

    if p == '':
        return ''

    for i in p:
        if i == '(':
            if count < 0:
                wrong.append(i)
            else:
                answer += i
            count += 1
        else:
            if count <= 0:
                wrong.append(i)
            else :
                answer += i
            count -= 1

        if count == 0:
            for i in range(len(wrong)):
                answer += wrong.pop()


    return answer
