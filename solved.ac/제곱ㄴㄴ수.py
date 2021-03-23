mi, mx = map(int,input().split())

i = 1
a = []
dic = {}

for i in range(2,int(mx**(1/2))):
    

while i**2 < mx:
    i += 1
    if i in dic: continue
    a.append(i**2)
    dic[i**2] = 1
    
num = []
for i in a:
    wich = 0
    if i >= mx: break
    for j in range(mi, mx+1):
        if j % i == 0:
            wich = j
            break
    
    for j in range(wich, mx+1, i):
        num.append(j)
    set(num)
    
count = mx - mi + 1 - len(num)

print(count)
#for i in range(mi,mx+1):
    