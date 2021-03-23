def solution(new_id):
    wich = 0
    
    new_id = new_id.lower()
    iidd = list(new_id)
    if not new_id.isalpha():
        while True:
            if wich == len(iidd):
                break
            if (iidd[wich] >= 'a' and iidd[wich] <= 'z') or (iidd[wich] >= '0' and iidd[wich] <= '9') or iidd[wich] == '-' or iidd[wich] == '_' or iidd[wich] == '.':
                wich += 1
                continue    
            else:
                iidd.pop(wich)            
            
    wich = 0
    while True:
        if wich < len(iidd)-1 and (iidd[wich] == '.' and iidd[wich+1] == '.'):
            iidd.pop(wich)
            wich-=1
        wich += 1
        if wich == len(iidd):
            break

    if len(iidd) != 0:
        if iidd[0] == '.':
            iidd.pop(0)
        if len(iidd) > 0 and iidd[-1] == '.':
            iidd.pop(-1)
    if len(iidd) == 0:
        iidd.append('a')

    if len(iidd) >= 16:
        iidd = iidd[0:15]
        if iidd[-1] == '.':
            iidd.pop(-1)
    if len(iidd) <= 2:
        last = iidd[-1]
        while True:
            iidd.append(last)
            if len(iidd) == 3:
                break

    answer = "".join(iidd)
    return answer

new_id = "z-+.^."
solution(new_id)