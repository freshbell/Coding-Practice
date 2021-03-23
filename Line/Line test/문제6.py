def solution(companies, applicants):
    answer = []
    company = []
    applicant = []
    match = {}

    for i in companies:
        company.append(i.split(" "))
        company[-1][2] = eval(company[-1][2])
        match[company[-1][0]] = []

    for i in applicants:
        applicant.append(i.split(" "))
        applicant[-1][2] = eval(applicant[-1][2])
        applicant[-1][1] = list(applicant[-1][1][0:applicant[-1][2]])
        match[applicant[-1][1][0]].append(applicant[-1][0])
        applicant[-1][1].pop(0)
        
    print(applicant)
    #while True:


    
    return answer

companies = ["A fabdec 2", "B cebdfa 2", "C ecfadb 2"]
applicants = ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]
print(solution(companies, applicants))