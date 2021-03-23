import collections

def solution(str1, str2):
    answer = 0
    A = []
    B = []
    str1 = str1.lower()
    str2 = str2.lower()
    

    for i in range(max(len(str1),len(str2))):
        if len(str1) - 1 > i:
            if str1[i] >= 'a' and str1[i] <= 'z' and str1[i+1] >= 'a' and str1[i+1] <= 'z':
                A.append(str1[i:i+2])
        if len(str2) - 1 > i:
            if str2[i] >= 'a' and str2[i] <= 'z' and str2[i+1] >= 'a' and str2[i+1] <= 'z':
                B.append(str2[i:i+2])

    colA = collections.Counter(A)
    colB = collections.Counter(B)

    if len(colA) == 0 and len(colB) == 0:
        answer = 1 * 65536
    else:
        big = {}
        small = {}
        chk = {}

        if len(str1) < len(str2): 
            big = colB
            small = colA
        else: 
            big = colA
            small = colB

        gyo = 0
        hap = 0
        
        for i in list(big.keys()):
            if i in small:
                chk[i] = True
                if big[i] > small[i]: 
                    gyo += small[i]
                    hap += big[i]
                else: 
                    gyo += big[i]        
                    hap += small[i]
            else:
                hap += big[i]

        for i in list(small.keys()):
            if i not in chk:
                hap += small[i]

        answer = int(gyo/hap*65536)
        
    return answer

str1 = "FRANCE"
str2 = "FReNCH"

solution(str1,str2)