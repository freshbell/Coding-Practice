# 파라메트릭 서치(Parametric Search)
# 최적화 문제를 결정 문제로 바꾸어 해결하는 기법
# 이진 탐색을 이용

#Ex1 떡 자르기
#N, M = map(int,input().split())
#arr = list(map(int,input().split()))

left = 0
right = -1# max(arr)

result = 0
while left <= right:
    mid = (left + right) // 2
    
    hap = 0
    for i in arr:
        if i > mid: hap += (i - mid)

    if hap < M: 
        right = mid - 1
    else: 
        result = mid
        left = mid + 1

#print(result)

#Ex2 특정 수의 개수 구하기
from bisect import bisect_left, bisect_right

N, M = map(int,input().split())
arr = list(map(int,input().split()))

left = bisect_left(arr,M)
right = bisect_right(arr,M) 

print(right - left)