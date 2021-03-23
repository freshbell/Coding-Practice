import collections

def solution(word, pages):
    answer = 0
    wich = 0
    dic = {}
    kan = 0
    body = []
    wi = []
    link = []
    search = []
    site = []
    ans = []
    word = word.lower()
    for i in range(len(pages)):
        pages[i] = pages[i].lower()

        for j in range(pages[i].find("content")+9,len(pages[i])):
            if pages[i][j] == '"':
                wich = j
                break
        
        dic[pages[i][135:wich]] = kan
        site.append(pages[i][135:wich])
        kan += 1

    for i in range(len(pages)):
        body = []
        wi = []
        wi.append(pages[i].find("body")+6)
        temp = pages[i]
        pages[i] = pages[i].replace("."," ")
        pages[i] = pages[i].replace("%"," ")
        pages[i] = pages[i].replace("!"," ")
        pages[i] = pages[i].replace("@"," ")
        pages[i] = pages[i].replace("#"," ")
        pages[i] = pages[i].replace("$"," ")
        pages[i] = pages[i].replace("^"," ")
        pages[i] = pages[i].replace("&"," ")
        pages[i] = pages[i].replace("*"," ")
        pages[i] = pages[i].replace("("," ")
        pages[i] = pages[i].replace(")"," ")
        pages[i] = pages[i].replace(","," ")
        pages[i] = pages[i].replace(";"," ")
        pages[i] = pages[i].replace(":"," ")
        pages[i] = pages[i].replace("0"," ")
        pages[i] = pages[i].replace("1"," ")
        pages[i] = pages[i].replace("2"," ")
        pages[i] = pages[i].replace("3"," ")
        pages[i] = pages[i].replace("4"," ")
        pages[i] = pages[i].replace("5"," ")
        pages[i] = pages[i].replace("6"," ")
        pages[i] = pages[i].replace("7"," ")
        pages[i] = pages[i].replace("8"," ")
        pages[i] = pages[i].replace("9"," ")
        pages[i] = pages[i].replace("\t"," ")


        for j in range(pages[i].find("body")+6,pages[i].find("</body>")):
            if pages[i][j] == ">" and pages[i][j-1] == "a":
                wi.append(j+2)
            if pages[i][j] == "<" and pages[i][j+1] == "a":
                wi.append(j-1)
        
        for j in range(0,len(wi)-1,2):
            body.append(pages[i][wi[j]:wi[j+1]].split(" "))
        
        link.append(len(body))
        
        search.append(0)
        for j in range(len(body)):
            search[i] += collections.Counter(body[j])[word]
        pages[i] = temp

    ans = [0 for i in range(len(pages))]
    for i in range(len(pages)):
        
        ans[i] += search[i]
        print(ans,search[i])
        for j in range(len(site)):
            if i == j: continue
            if site[j] in pages[i]:
                ans[j] += search[i] / link[i]

    print(ans)

    maximum = max(ans)
    for i in range(len(pages)):
        if ans[i] == maximum:
            answer = i
            break
    return answer

word = "Muzi"
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution(word, pages))