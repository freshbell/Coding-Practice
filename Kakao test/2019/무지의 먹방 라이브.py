def solution(food_times, k):
    length = len(food_times)
    answer = 0
    minimum = 0
    mini = []
    wich = 0
    chk = 0
    plus = 0
    res_list = []


    while True:
        mini = [food_times[i] for i in range(len(food_times)) if food_times[i] > plus]
        if len(mini) > 0:
            minimum = min(mini)

        if minimum <= plus:
            answer = -2
            break

        if k - ((minimum-plus)*length)  > 0:
            k -= ((minimum-plus)*length) 
            plus += (minimum-plus)
            res_list = list(filter(lambda x: food_times[x] <= plus, range(len(food_times))))
            length = len(food_times) - len(res_list)
        else:
            gil = 0
            for i in range((minimum-plus),0,-1):
                if k - (i * length) >= 0: 
                    k -= (i*length)
                    plus += i
                    break

            for i in range(len(food_times)):
                if food_times[i] > plus:
                    wich = i


            print(wich,k,plus)
            for i in range(wich+1, len(food_times)):
                if food_times[i] > plus:
                    wich = i
                    k -= 1
                if k == 0:
                    answer = wich
                    chk = 1
                    break

            if k != 0:
                answer = -2
                chk = 1
                break
                
        if chk == 1:
            break
       # print(minimum,k)

    return answer+1

food_times = [1,1,1,2]
k = 4
print(solution(food_times,k))