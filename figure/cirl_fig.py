from figure.fig import Figure
from fun.circle import draw_circles

class Circle(Figure):
    def __init__(self,x,y,r,color):
        self.r = r
        self.color = color
        self.run(x,y)

    def draw(self, screen):
        draw_circles(self.x,self.y,self.r,self.color,screen)
    
    def inside(self, px, py):
        dx = px - self.x
        dy = py - self.y
        c = (dx**2) + (dy **2)
        return c<=(self.r**2)
    
    def run(self, gx, gy):
        if gx-self.r<0:
            gx = 0+self.r
        if gx+self.r>800:
            gx = 800-self.r
        if gy + self.r > 600:
            gy = 600 - self.r
        if gy-self.r<0:
            gy = 0+self.r
        self.x = gx
        self.y = gy