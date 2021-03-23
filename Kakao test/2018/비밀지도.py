def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        plus = ''
        ans = bin(arr1[i] | arr2[i])[2:]
        if len(ans) != n:
            plus = '0' *  (n-len(ans))
            ans = plus + ans
        ans = ans.replace('1','#')
        ans = ans.replace('0',' ')
        
        answer.append(ans)
    return answer

n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = 	[27, 56, 19, 14, 14, 10]

print(solution(n,arr1,arr2))