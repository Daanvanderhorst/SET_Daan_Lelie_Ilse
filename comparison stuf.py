p = 1
def checkforset(set1, set2, set3):
    for i in range(1,5):
        if (set1[i]+set2[i]+set3[i])%3!=0:
            return False
    return True

def listofsets(list):
    sets = []
    for i in range(0, len(list)-2):
        for j in range(i+1, len(list)-1):
            for k in range(j+1, len(list)):
                if checkforset(list[i], list[j], list[k]):
                    sets.append((i+1, j+1, k+1))
    return sets

def firstset(list):
    for i in range(0, len(list)-2):
        for j in range(i+1, len(list)-1):
            for k in range(j+1, len(list)):
                if checkforset(list[i], list[j], list[k]):
                    return (i+1, j+1, k+1)