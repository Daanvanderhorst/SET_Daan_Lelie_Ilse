from enum import Enum


class number(Enum):
    num1 = 1
    num2 = 2
    num3 = 3
    def _eq_(self, other):
        return self.number == other.number
        
class symbol(Enum): #hoi Daan
    diamont = 1
    wave = 2
    oval = 3
    def _eq_(self, other):
        return self.symbol == other.symbol
        
class color(Enum):
    red = 1
    green = 2
    purple = 3
    def _eq_(self, other):
        return self.color == other.color

class shading(Enum):#shading comment
    solid = 1
    striped = 2
    empty = 3
    def _eq_(self, other):
        return self.shading == other.shading
    
class card:
    def _init_(self, number, symbol, color, shading):
        self.number = number
        self.symbol = symbol
        self.color = color
        self.shading = shading
    

class set:






    def __gt__(self, number, symbol, color, shading, num1, num2, num3,diamont, wave, oval, red, green, purple, solid, striped, empty):
        
    def _ne_(self, number, symbol, color, shading, num1, num2, num3,diamont, wave, oval, red, green, purple, solid, striped, empty):
    
    def _lt_(self, number, symbol, color, shading, num1, num2, num3,diamont, wave, oval, red, green, purple, solid, striped, empty):



    