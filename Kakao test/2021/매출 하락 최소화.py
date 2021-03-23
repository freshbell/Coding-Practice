import sys
sys.setrecursionlimit(10**6)

minimum = 9999

def find(d,chk, sales,hap,li,wich):
    global minimum
    if wich == len(li):
        if minimum > hap:
            minimum = hap
    else:
        i = li[wich]
        if chk[i]: find(d,chk,sales,hap,li,wich+1)
        else:
            chk[i] = True
            for j in d[i]:
                hap += sales[j-1]
                if j in d and i != j: chk[j] = True
                find(d,chk,sales,hap,li,wich+1)
                hap -= sales[j-1]
                if j in d and i != j: chk[j] = False
            chk[i] = False

    return 0

def solution(sales, links):
    global minimum
    answer = 0
    d = {}
    chk = {}
    for parent, child in links:
        if parent not in d:
            chk[parent] = False
            d[parent] = []
            d[parent].append(parent)
        d[parent].append(child)

    li = sorted(list(d.keys()))
    find(d,chk, sales,0,li,0)
    answer = minimum
    return answer

sales = [10, 10, 1, 1]
links = [[3,2], [4,3], [1,4]]
solution(sales,links)