from itertools import permutations, combinations
small = [int(input()) for _ in range(9)]
answer = []
small.sort()

h_list = list(combinations(small, 7))
for i in range(len(h_list)):
    if sum(h_list[i]) == 100:
        print(*sorted(list(h_list[i])), sep='\n')
        break
'''
johap = [1,1,1,1,1,1,1,0,0]
for i in list(permutations(johap)):
    hap = 0
    for j in range(0,9):
        if i[j] == 1: hap += small[j]
        if hap > 100: break

    if hap == 100:
        for j in range(0,9):
            if i[j] == 1: print(small[j])
        break
''''''
def dfs(wich,hap, count):
    if hap == 100 and count == 7:
        return True
    elif hap < 100:
        for i in range(wich + 1, len(small)):
            if dfs(i,hap + small[i],count+1):
                print(small[i])
                return True
    return False

dfs(-1,0, 0)
'''