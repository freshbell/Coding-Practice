def solution(inp_str):
    answer = []
    special = "~!@#$%^&*"
    di = {}
    yeon = 0
    same = {}

    if not 8 <= len(inp_str) <= 15:answer.append(1)
    for i in range(len(inp_str)):
        if not ('A' <= inp_str[i] <= 'Z' or 'a' <= inp_str[i] <= 'z' or '0' <= inp_str[i] <= '9' or inp_str[i] in special): di[2] = True
        if 'A' <= inp_str[i] <= 'Z': di[31] = True
        if 'a' <= inp_str[i] <= 'z': di[32] = True
        if '0' <= inp_str[i] <= '9': di[33] = True
        if inp_str[i] in special: di[34] = True

        if i + 1 < len(inp_str) and inp_str[i] == inp_str[i+1]: yeon += 1
        else: yeon = 0
        if yeon >= 3: di[4] = True

        if inp_str[i] not in same: same[inp_str[i]] = 0
        same[inp_str[i]] += 1
        if same[inp_str[i]] >= 5: di[5] = True

    if 2 in di: answer.append(2)
    chk = 0
    for i in range(31, 35):
        if i in di: chk += 1
    if chk < 3: answer.append(3)
    if 4 in di: answer.append(4)
    if 5 in di: answer.append(5)
    if answer == []: answer.append(0)
    return answer

inp_str = "UUUUUUUUUUUUUUUU"
print(solution(inp_str))