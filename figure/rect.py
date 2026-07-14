from figure.fig import Figure
from fun.square import square
import pygame as pg
class Rect(Figure):  
    def __init__(self, x, y, w, h, color):
        self.parent = None
        self.w = w
        self.h = h
        self.color = color
        self.child = []
        self.run(x, y) # Сразу ограничиваем координаты при создании
        

    def add(self, figure):
        f_x,f_y = figure.x,figure.y 
        f_x -= self.x
        f_y -= self.y
        figure.x,figure.y = f_x, f_y
        self.child.append(figure)
        figure.parent = self
        
    def draw(self, screen):
        square(self.x, self.y, self.h, self.w, self.color, screen)
        for i in self.child:
            square(self.x+i.x,self.y + i.y,i.h,i.w,i.color,screen)
    
    def inside(self, px, py):
        return (self.x <= px <= self.x + self.w) and (self.y <= py <= self.y + self.h)
    
    def run(self, gx, gy):
        if self.parent is None:
            if self.w+gx>800:
                gx = 800-self.w

            if self.h+gy>600:
                gy = 600-self.h

            self.x = gx
            self.y = gy
        else:
            if self.w+gx>self.parent.w:
                gx = self.parent.w-self.w

            if self.h+gy>self.parent.h:
                gy = self.parent.h-self.h

            self.x = gx
            self.y = gy