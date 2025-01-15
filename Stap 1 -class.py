from enum import Enum 
#https://www.geeksforgeeks.org/python-classes-and-objects/ 

class color(Enum):
    green = 0
    purple = 1
    red = 2

class symbol(Enum): 
    diamond = 0
    oval = 1
    squiggle = 2

class shading(Enum):
    empty = 0
    filled = 1
    shaded = 2

class number(Enum):
    1 = 1
    2 = 2
    3 = 3
        
class card:
    def __init__(self, color, symbol, shading, number):
        self.color = color
        self.symbol = symbol
        self.shading = shading
        self.number = number
        self.list = [self.color, self.symbol, self.shading, self.number]


    def eqcolor(self, other):
        return self.color == other.color
    def eqsymbol(self, other):
        return self.symbol == other.symbol
    def eqshading(self, other):
        return self.shading == other.shading
    def eqnumber(self, other):
        return self.number == other.number
    def imagename(self):
        imcolor = color(int(self.color)).name
        return(imcolor)
    def _eq_(self, other):#==
        if self.eqnumber(self, other) and self.eqcolor(self, other) and self.eqshading(self, other) and self.symbol(self, other) == True:
            card.self = card.other 
kaart = card(1,1,1,1)
print(kaart.imagename)