from figure.fig import Figure
from fun.square import square
from typing import override

class Rect(Figure):  
    def __init__(self, x, y, h, w, color):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.color = color
    @override
    def draw(self):   
        square(self.x, self.y, self.h, self.w, self.color)