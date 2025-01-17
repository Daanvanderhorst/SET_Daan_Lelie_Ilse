from enum import Enum 
import pygame

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

class Card:
    def __init__(self, idnumber, index, rect):
        self.color = Color(idnumber//27)
        self.symbol = Symbol(idnumber%27//9)
        self.shading = Shading(idnumber%9//3)
        self.number = Number(idnumber%3+1)
        self.index = index
        self.rect = rect
        self.selected = False
        self.list = [self.color.value, self.symbol.value, self.shading.value, self.number.value]
    
    def getimage(self):
        imcolor = self.color.name.lower()
        imsymbol = self.symbol.name.lower()
        imshading = self.shading.name.lower()
        imnumber = self.number.value
        imagename = f"kaarten\\{imcolor}{imsymbol}{imshading}{imnumber}.gif"
        image = pygame.image.load(imagename)
        image = pygame.transform.scale(image, (100, 150))
        return image
    
    def change_selected(self):
        self.selected = not self.selected
        return self.selected
