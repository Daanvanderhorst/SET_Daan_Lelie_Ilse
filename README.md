# SET_Daan_Lelie_Ilse
final project programming in mathematics

def generatecards():
   allthecards = []
   allthecards.append(random.randrange(0, 81, 1))
   for i in range(0, 30):
      q = random.randrange(0, 81, 1)
      alreadyused=True
      for j in range(len(allthecards)):
         if allthecards[i]==q:
            alreadyused=False
      if alreadyused:
         allthecards.append(q)
   return(allthecards)