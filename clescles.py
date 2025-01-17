from enum import Enum 

class Color(Enum):
    GREEN = 0
    PURPLE = 1
    RED = 2

class Symbol(Enum): 
    DIAMOND = 0
    OVAL = 1
    SQUIGGLE = 2

class Shading(Enum):
    EMPTY = 0
    FILLED = 1
    SHADED = 2
        
class Number(Enum):
    num1 = 1
    num2 = 2
    num3 = 3

class card:
    def __init__(self, idnumber):
        self.color = Color(idnumber//27)
        self.symbol = Symbol(idnumber%27//9)
        self.shading = Shading(idnumber%9//3)
        self.number = Number(idnumber%3+1)
        self.list = [self.color, self.symbol, self.shading, self.number]

    def imagename(self):
        imcolor = self.color.name.lower()
        imsymbol = self.symbol.name.lower()
        imshading = self.shading.name.lower()
        imnumber = self.number.value
        return f"kaarten\\{imcolor}{imsymbol}{imshading}{imnumber}.gif"
    
 

