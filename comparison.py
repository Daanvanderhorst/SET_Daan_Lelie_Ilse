
def checkforset(card1, card2, card3): #binnen drie kaarten kijken of er een set is
    for i in range(0,4): #je gaat alle verschillende eigenschappen af (4 eigenschappen)
        if (card1[i] + card2[i] + card3[i])%3 != 0: #checken of alles niet hetzelfde of niet verschillend is 
            return False 
    return True #dan is het een set

def listofsets(cards): #binnen meerdere kaarten alle sets zoeken
    sets = []  #een lege lijst maken voor sets die we later willen opslaan
    for i in range(0, len(cards)-2): 
        for j in range(i+1, len(cards)-1): 
            for k in range(j+1, len(cards)):
                if checkforset(cards[i].list, cards[j].list, cards[k].list):
                    sets.append((i, j, k)) #de plus 1 is zodat je niet de index krijg maar echt het nummer van de fysieke kaart
    return sets #een lijst terug met alle sets uit de kaarten 

def firstset(cards): #dit vind gewoon een set en dan stopt het 
    for i in range(0, len(cards)-2):
        for j in range(i+1, len(cards)-1):
            for k in range(j+1, len(cards)):
                if checkforset(cards[i].list, cards[j].list, cards[k].list):
                    return ([k, j, i])