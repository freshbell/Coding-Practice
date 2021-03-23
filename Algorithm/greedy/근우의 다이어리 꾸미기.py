ip = eval(input())

count = 1
gap = 11
while True:
    if ip < gap: break
    gap *= 10
    gap += 1
    count += 1

print(count)