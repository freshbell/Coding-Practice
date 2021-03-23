import sys
sys.setrecursionlimit(100001) 

class Node:
    def __init__(self):
        self.cnt = 0
        self.child = {}

class Tree:
    head = []
    head2 = []
    dap = []
    su = 0

    def add(self, word, ch, wich):
       # print(word)
        if ch == 1:
            if len(self.head) <= wich:
                self.head.append(Node())
            cur = self.head[wich]
        else :
            if len(self.head2) <= wich:
                self.head2.append(Node())
            cur = self.head2[wich]
            
        for i in word:
            if i not in cur.child:
                cur.child[i] = Node()

            cur.cnt += 1    
            cur = cur.child[i]
            
        cur.child['*'] = True

    def find(self,query, ch,wich):
        if ch == 1:cur = self.head[wich]
        else:cur = self.head2[wich]
        cnt = 0
        
       # print(cur.child)
        if query[0] == '?':
            query = query[::-1]

        for i in query:
            if i != '?' and i not in cur.child:
                return cnt
            if i == '?':
                cnt = cur.cnt
                break
            else:
                #print(cur.child)
                cur = cur.child[i]
        
        return cnt
            
    def track(self,cur,chk):
        cnt = 0
        if '*' in cur:
            cnt = 1
        else:
            for i in cur.keys():
                cnt += self.track(cur[i],chk + 1)

        return cnt

def solution(words, queries):
    answer = []
    foreback = Tree()
    wich = 0
    wich2 = 0
    howlong = {}
    howlong2 = {}

    for word in words:
        if len(word) not in howlong:
            howlong[len(word)] = wich
            wich += 1
        foreback.add(word,1,howlong[len(word)])

        if len(word) not in howlong2:
            howlong2[len(word)] = wich2
            wich2 += 1
        foreback.add(word[::-1],2,howlong[len(word)])

    for query in queries:

        if (query[0] == '?' and query[-1] == '?') or query[0] != '?':
            if len(query) not in howlong:
                answer.append(0)
            else:
                answer.append(foreback.find(query,1,howlong[len(query)]))
        else:
            if len(query) not in howlong2:
                answer.append(0)
            else:
                answer.append(foreback.find(query,2,howlong[(len(query))]))
    #print(answer)
    return answer

words = ["frodo","froas","fran","asddo"]
queries = ["?????", "??????","???do", "fr???", "fro??", "pro?","?"]
solution(words,queries)