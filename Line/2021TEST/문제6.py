# 각 플래그에 따른 규칙을 딕셔너리에 저장하기 위한 함수
def rule_dic(flag_rules):
    rules = {}

    for i in flag_rules:
        rules_split = list(i.split())
        rules[rules_split[0]] = rules_split[1]

    return rules

# commands의 규칙들이 제대로 입력되었는지 체크하기 위한 함수
def rule_chk(command, rules):
    flag_count = {}
    wich = 1 # command에서 program을 제외하고 제일 먼저 확인하기 위한 위치
    
    while wich < len(command): # command의 크기보다 작을 때까지 실행
        flag = command[wich] 
        if flag not in rules: return False # flag가 rules에 없다면 존재하지 않는 규칙 -> False 반환
        else: 
            rule = rules[flag] # flag에 따른 규칙
            
            if flag not in flag_counts: flag_counts[flag] = True
            else: return False

            # 각 규칙에 따라 command확인 + "STRINGS, NUMBERS" 추가
            if rule == "STRING":
                if not command[wich+1].isalpha(): return False
                wich += 2
            elif rule == "NUMBER":
                if not command[wich+1].isdigit(): return False
                wich += 2
            elif rule == "STRINGS":
                while wich < len(command):
                    wich += 1
                    if command[wich] in rules: break
                    if not command[wich].isalpha(): return False
            elif rule == "NUMBERS":
                while wich < len(command):
                    wich += 1
                    if command[wich] in rules: break
                    if not command[wich].isdigit(): return False
            elif rule == "NULL": wich += 1

    return True

def solution(program, flag_rules, commands):
    answer = []

    rules = rule_dic(flag_rules) # 각 플래그에 따른 규칙을 딕셔너리에 저장하기 위한 함수 호출

    for i in range(len(commands)):
        commands[i] = list(commands[i].split()) # 문자열을 리스트 형식으로 변환
        
        if program != commands[i][0]: answer.append(False) # commands에 program을 제대로 입력했는지 확인
        else: answer.append(rule_chk(commands[i],rules)) # program이 제대로 입력되었다면 commands의 규칙들이 제대로 입력되었는지 체크하기 위한 함수 호출

    return answer
    
program = "line"
flag_rules = ["-s STRING", "-n NUMBER", "-e NULL"]
commands =["line -s 123 -n HI", "line fun"]
print(solution(program, flag_rules, commands))