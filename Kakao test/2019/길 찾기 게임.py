class Node:
    def __init__(self):
        self.x = 0
        self.left = 0
        self.right = 0
        self.parent = 0
    
def insert(node,head,i):
    wich = head

    while True: 
        if node[wich].x > i[0]: #left
            if node[wich].left not in node:
                node[i[2]] = Node()
                node[i[2]].x = i[0]
                node[i[2]].parent = wich
                node[wich].left = i[2]
                break
            wich = node[wich].left
        else:
            if node[wich].right not in node:
                node[i[2]] = Node()
                node[i[2]].x = i[0]
                node[i[2]].parent = wich
                node[wich].right = i[2]
                break
            wich = node[wich].right

    return node

def backward(node,head):
    ans = []
    chk = {}
    wich = head
    chk[wich] = 0
    
    while True:
        if wich == 0: break #종료 조건
        chk[wich] += 1

        if node[wich].left != 0 and chk[wich] == 1:
            wich = node[wich].left
            chk[wich] = 0
        elif node[wich].right != 0 and chk[wich] <= 2:
            chk[wich] = 2
            wich = node[wich].right
            chk[wich] = 0
        elif (node[wich].left == 0 and node[wich].right == 0) or chk[wich] == 3:
            ans.append(wich)
            wich = node[wich].parent

    return ans

def forward(node,head):
    ans = []
    chk = {}
    wich = head
    chk[wich] = 0
    
    while True:
        if wich == 0: break #종료 조건
        if chk[wich] == 0:
            ans.append(wich)
        chk[wich] += 1

        if node[wich].left != 0 and chk[wich] == 1:
            wich = node[wich].left
            chk[wich] = 0
        elif node[wich].right != 0 and chk[wich] <= 2:
            chk[wich] = 2
            wich = node[wich].right
            chk[wich] = 0
        elif (node[wich].left == 0 and node[wich].right == 0) or chk[wich] == 3:
            wich = node[wich].parent

    return ans

def ward(node,head):
    fore = []
    back = []
    ans = []

    chk = {}
    wich = head
    chk[wich] = 0
    
    while True:
        if wich == 0: break #종료 조건
        if chk[wich] == 0:
            fore.append(wich)
        chk[wich] += 1

        if node[wich].left != 0 and chk[wich] == 1:
            wich = node[wich].left
            chk[wich] = 0
        elif node[wich].right != 0 and chk[wich] <= 2:
            chk[wich] = 2
            wich = node[wich].right
            chk[wich] = 0
        elif (node[wich].left == 0 and node[wich].right == 0) or chk[wich] == 3:
            back.append(wich)
            wich = node[wich].parent
    ans.append(fore)
    ans.append(back)
    return ans

def solution(nodeinfo):
    answer = []
    node = {}
    y = {}

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
        y[nodeinfo[i][1]] = True
    
    y = sorted(list(y.keys()),key=lambda x:x,reverse=True)
    nodeinfo = sorted(nodeinfo,key=lambda x:(x[1],x[0]),reverse=True)
    #print(nodeinfo)
    
    head = nodeinfo[0][2]
    node[head] = Node()
    node[head].x = nodeinfo[0][0]

    for i in nodeinfo[1:]:
        node = insert(node,head,i)
    
    answer = ward(node,head)
    return answer

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))