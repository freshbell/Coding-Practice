graph = [[2,5,1,6,1,4,1],[6,1,1,2,2,9,3],[7,2,3,2,1,3,1],[1,1,3,1,7,1,2],[4,1,2,3,4,1,2],[3,3,1,2,3,4,1],[1,5,2,9,4,7,1]]
graph = [[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,2],[1,1,1,1,2,1]]
chk = [[999 for _ in range(len(graph))] for _ in range(len(graph))]
chk[0][0] = 1

for i in range(len(graph)):
    for j in range(len(graph)):
        if chk[i][j] > 0:
            if i + graph[i][j] < len(graph) and chk[i+graph[i][j]][j] > chk[i][j] + 1: 
                chk[i+graph[i][j]][j] = chk[i][j] + 1
            if j + graph[i][j] < len(graph)and chk[i][j+graph[i][j]] > chk[i][j] + 1: 
                chk[i][j+graph[i][j]] = chk[i][j] + 1

print(chk)