# O(logN)

# 재귀적 구현
def binary_search_re(array, target, start, end):
    if start > end: return None
    mid = (start + end) // 2
    if array[mid] == target: return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
    
# 반복문 구현
def binary_search_while(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target: return mid
        elif array[mid] > target: end = mid - 1
        else: start = mid + 1

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None: print("원소가 존재하지 않습니다.")
else: print(result + 1)

# bisect 사용법
from bisect import bisect_left
a = [1,2,4,8,16,32]
print(bisect_left(a,4))
print(a)

# 파라메트릭 서치(Parametric Search)
# 최적화 문제를 결정 문제로 바꾸어 해결하는 기법

