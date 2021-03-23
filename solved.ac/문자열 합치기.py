import heapq

arr = [2,2,4]

heap = []

for i in arr:
    heapq.heappush(heap,i)

summ = 0
while True:
    hap = heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap,hap)
    summ += hap

    if len(heap) == 1:
        break

print(summ)
