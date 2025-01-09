from enum import Enum 

#https://www.geeksforgeeks.org/python-classes-and-objects/ 

class color(Enum):
    green = 1
    purple = 2
    red = 3

class symbol(Enum): 
    diamont = 1
    oval = 2
    wave = 3


class shading(Enum):
    empty = 1
    solid = 2
    striped = 3


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






    