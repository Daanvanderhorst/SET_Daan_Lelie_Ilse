from enum import Enum 

#https://www.geeksforgeeks.org/python-classes-and-objects/ 

class color(Enum):
    red = 1
    green = 2
    purple = 3

class symbol(Enum): 
    diamont = 1
    wave = 2
    oval = 3

class shading(Enum):
    solid = 1
    striped = 2
    empty = 3

class number(Enum):
    num1 = 1
    num2 = 2
    num3 = 3
        
class card:
    def _init_(self, number, symbol, color, shading):
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
    
    def _eq_(self, other):#==
        if self.eqnumber(self, other) and self.eqcolor(self, other) and self.eqshading(self, other) and self.symbol(self, other) == True:
            card.self = card.other 


class set:
    def _init_(self, cards):
        self.cards = cards 






    