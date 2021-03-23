D = eval(input())
d = [1,0,0,0,0,0,0,0]

for i in range(D):
    visit = []
    visit.append((d[1] + d[2])%1000000007)
    visit.append((d[0] + d[2] + d[3])%1000000007)
    visit.append((d[0] + d[1] + d[3] + d[4])%1000000007)
    visit.append((d[1] + d[2] + d[4] + d[5])%1000000007)
    visit.append((d[2] + d[3] + d[5] + d[6])%1000000007)
    visit.append((d[3] + d[4] + d[7])%1000000007)
    visit.append((d[4] + d[7])%1000000007)
    visit.append((d[5] + d[6])%1000000007)
    d = visit

print(d)