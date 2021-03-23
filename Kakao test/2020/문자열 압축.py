#second
def solution2(s):
    answer = len(s)

    if len(s) == 1:
        return 1

    for i in range(1, len(s)//2 + 1):
        B = ''
        count = 0
        length = 0

        for j in range(0,len(s)//i*i,i):
            A = s[j:j+i]
            
            if A == B:
                count += 1
            else:
                length += i
                if count > 0:
                    length += len(str(count+1))
                count = 0
            B = A

        if count > 0:
            length += len(str(count+1))
        length += (len(s) - len(s)//i*i)
        print(i,length)
        answer = min(answer, length)
            
    return answer

s = "aaaaaaaaaa"
#first
def solution(s):
    test = []
    test2 = []
    chk = 0
    answer = 9999
    add = 0
    count = 0
    length = 0

    if len(s) == 1:
        return 1
    
    for i in range(1,len(s)//2+1):
        add = 0
        length = 0
        count = 0
        test = []
        test2 = []

        for j in range(len(s)//i*i):
            if j < i:
                test.append(s[j])
        #        print(test)
            else:
                if test[add] == s[j]:
                    chk += 1
            test2.append(s[j])
            add += 1

            if add == i :
                add = 0
                if chk == i:
                    count += 1
                else:
                    if count > 0:
                        length += len(str(count + 1))
                    count = 0
                    length += i
                chk = 0
                print(i,j,length)

                test = test2
                test2 = []
                
        if count > 0:
            length += len(str(count + 1))
        
        length += (len(s) - len(s)//i*i)

        if length < answer :
            answer = length

    return answer

#s = "aabc"
print(solution2(s))
