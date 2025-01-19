
def checkforset(card1, card2, card3): 
    for i in range(0,4): # for all properties
        if (card1[i] + card2[i] + card3[i])%3 != 0: # check if everything is the same or all different
            return False 
    return True 

def listofsets(cards): 
    sets = [] # where we're going to store the sets
    for i in range(0, len(cards)-2): 
        for j in range(i+1, len(cards)-1): 
            for k in range(j+1, len(cards)): #loops over all combinations of cards
                if checkforset(cards[i].list, cards[j].list, cards[k].list):
                    sets.append((i, j, k)) # add set tuple to list of sets
    return sets # return entire list

def firstset(cards): # stops after 1 set 
    for i in range(0, len(cards)-2):
        for j in range(i+1, len(cards)-1):
            for k in range(j+1, len(cards)):
                if checkforset(cards[i].list, cards[j].list, cards[k].list):
                    return ([k, j, i])
    return[]