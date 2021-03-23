
array = list(map(int, input()))

hap = 0
chk = 0

for i in array:
    if i <= 1 or hap <= 1:
        hap += i
    else :
        hap *= i

print(hap)