import heapq

n = 7
m = 14
ip = [[0,1,1.3],[0,2,1.1],[0,3,1.24],[3,4,1.17],[3,5,1.24],[3,1,2],[1,2,1.31],[1,2,1.26],[1,4,1.11],[1,5,1.37],[5,4,1.24],[4,6,1.77],[5,6,1.11],[2,6,1.2]]


heap = []
table = [[999 if i != j else 1 for i in range(n)] for j in range(n)]


for i in ip:
    table[i[0]][i[1]] = i[2]
    table[i[1]][i[0]] = i[2]
    
for i in range(len(table[0])):
    if table[0][i] == 1 or table[0][i] == 999: continue
    heapq.heappush(heap,[table[0][i],i])

while heap:
    cost, wich = heapq.heappop(heap)

    if table[0][wich] < cost: continue
    
    for i in range(7):
        next_cost = cost * table[wich][i]
        if next_cost < table[0][i]:
            table[0][i] = next_cost
            heapq.heappush(heap,[next_cost,i])

print(table)
