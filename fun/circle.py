import pygame as pg

def draw_circles(x, y, r,color,screen):
    pg.draw.circle(screen, color, (x, y), r, 2)

