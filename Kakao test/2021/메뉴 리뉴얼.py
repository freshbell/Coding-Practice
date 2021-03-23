from itertools import combinations

def solution(orders, course):
    answer = []
    menu = {}
    maximum = {}

    for i in course:
        maximum[i] = 0

    for i in orders:
        for j in course:
            for k in combinations(i,j):
                johap = list(k)
                johap.sort()
                if ''.join(johap) not in menu: menu[''.join(johap)] = 1
                else: menu[''.join(johap)]+=1
                if maximum[j] < menu[''.join(johap)]:
                    maximum[j] = menu[''.join(johap)]
    
    for i in list(menu.keys()):
        if menu[i] == maximum[len(i)] and menu[i] != 1:
            answer.append(i)
    answer.sort()
    return answer

orders = 	["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,4]
print(solution(orders, course))

