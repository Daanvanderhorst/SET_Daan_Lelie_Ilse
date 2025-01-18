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

class Card:
    def __init__(self, idnumber, index, rect):
        self.color = idnumber//27
        self.symbol = idnumber%27//9
        self.shading = idnumber%9//3
        self.number = idnumber%3
        self.index = index
        self.rect = rect
        self.selected = False
        self.list = [self.color, self.symbol, self.shading, self.number]
    
    def getimage(self):
        imcolor = Color(self.color).name.lower()
        imsymbol = Symbol(self.symbol).name.lower()
        imshading = Shading(self.shading).name.lower()
        imnumber = self.number + 1
        imagename = f"kaarten\\{imcolor}{imsymbol}{imshading}{imnumber}.gif"
        image = pygame.image.load(imagename)
        image = pygame.transform.scale(image, (100, 150))
        return image
    
    def change_selected(self):
        self.selected = not self.selected
        return self.selected
