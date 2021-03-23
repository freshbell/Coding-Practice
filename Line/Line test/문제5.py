def solution(cards):
    answer = 0

    player_hap = [0]
    dealer_hap = [0]

    chk = 0
    two = 0

    for i in cards:
        chk += 1
        if chk <= 4:
            if not chk%2 == 0: 
                #player.append(i)
                if i == 1:
                    for j in range(len(player_hap)):
                        player_hap.append(player_hap[0] + 1)
                        player_hap.append(player_hap[0] + 10)
                        player_hap.pop(0)
                else:
                    print(player_hap)
                    gap = i
                    if gap > 10: gap = 10
                    for j in range(len(player_hap)):
                        player_hap[j] += gap
            else:
                if chk == 4: two = i
                #dealer.append(i)
                if i == 1:
                    for j in range(len(dealer_hap)):
                        dealer_hap.append(dealer_hap[j] + 1)
                        dealer_hap.append(dealer_hap[j] + 10)
                else:
                    gap = i
                    if gap > 10: gap = 10
                    for j in range(len(dealer_hap)):
                        dealer_hap[j] += gap
        for j in range(len(player_hap)):
            if player_hap[j] == 21: continue
            if player_hap[j] < 17: player_hap[j] + i

        
        

cards = [1,2,1,4]
solution(cards)          
#12, 7, 11, 6, 2, 12
#1, 4, 10, 6, 9, 1, 8, 13
# 10, 13, 10, 1, 2, 3, 4, 5, 6,7
# 3, 3, 3, 3, 3, 3, 3, 3, 3, 3
