TestCase = int(input())

for test_case in range(TestCase):
    dic = {}
    name = [[] for _ in range(20001)]
    N = int(input())
    for _ in range(N):
        ip = input()
        if ip not in dic:
            dic[ip] = True
            name[len(ip)].append(ip)

    print("#" + str(test_case))
    for i in name:
        if i != []:
            for j in sorted(i):
                print(j)

    