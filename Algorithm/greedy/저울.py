#hap = 0
#exi = {}

#for i in chu:
#    exi[i] = True
#    hap += i

#def dfs(chu,want,hap,wich):
#    if hap == want: return True

#    for i in range(wich + 1, len(chu)):
#        if want >= hap + chu[i]:
#            chk = dfs(chu,want,hap+chu[i],i)
#            if chk: return True

#    return False

#for i in range(1,hap+1):

#    if i in exi: continue
#    else:
#        if not dfs(chu,i,0,-1):
#            print(i)
#            break


#N = eval(input())

#chu = list(map(int, input().split()))
#chu.sort()

#ganeung = {}
#ganeung[0] = True
#maximum = chu[0]
#chk = 0

#for i in chu:
#    for j in list(ganeung.keys()):
#        if i + j not in ganeung:
#            if i+j > maximum + 1:
#                print(maximum + 1)
#                chk = 1
#                break
#            ganeung[i+j] = True
#            maximum = max(maximum,i+j)
#    if chk==1: break


N = eval(input())

chu = list(map(int, input().split()))
chu.sort()
ans = 0

for i in chu:
    if i <= ans + 1:
        ans += i
    else: break

print(ans+1)