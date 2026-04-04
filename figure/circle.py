from figure.fig import Figure
from fun.circle import draw_circles

class Circle(Figure):
    def __init__(self,x,y,r,color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
    

    def draw(self):
        draw_circles(self.x,self.y,self.r,self.color)