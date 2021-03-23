ip = list(map(int,input()))

zero = 0
one = 0

if ip[0] == 0: zero += 1
else: one += 1
    
for i in range(1,len(ip)):
    if ip[i] == ip[i-1]: continue
    else :
        if ip[i] == 0: zero += 1
        else: one += 1

if zero < one: print(zero)
else: print(one)