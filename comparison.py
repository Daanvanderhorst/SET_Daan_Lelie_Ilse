
def checkforset(card1, card2, card3): #binnen drie kaarten kijken of er een set is
    for i in range(0,4): #je gaat alle verschillende eigenschappen af (4 eigenschappen)
        if (card1.list[i]+card2.list[i]+card3.list[i])%3 != 0: #checken of alles niet hetzelfde of niet verschillend is 
            return False 
    return True #dan is het een set

def listofsets(list): #binnen meerdere kaarten alle sets zoeken
    sets = []  #een lege lijst maken voor sets die we later willen opslaan
    for i in range(0, len(list)-2): 
        for j in range(i+1, len(list)-1): 
            for k in range(j+1, len(list)):
                if checkforset(list[i], list[j], list[k]):
                    sets.append((i+1, j+1, k+1)) #de plus 1 is zodat je niet de index krijg maar echt het nummer van de fysieke kaart
    return sets #een lijst terug met alle sets uit de kaarten 

def firstset(list): #dit vind gewoon een set en dan stopt het 
    for i in range(0, len(list)-2):
        for j in range(i+1, len(list)-1):
            for k in range(j+1, len(list)):
                if checkforset(list[i], list[j], list[k]):
                    return ([k, j, i])