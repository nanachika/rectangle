import pygame as pg
def square(x,y,h,w,colors,screen):
    fst_x,fst_y = x,y
    snd_x,snd_y = x + w, y
    tsd_x, tsd_y = x + w, y + h
    fsh_x,fsh_y = x,y + h
    
    pg.draw.line(screen, colors, (fst_x, fst_y), (snd_x,snd_y))
    pg.draw.line(screen, colors, (snd_x, snd_y), (tsd_x,tsd_y))
    pg.draw.line(screen, colors, (tsd_x, tsd_y), (fsh_x,fsh_y))
    pg.draw.line(screen, colors, (fsh_x, fsh_y), (fst_x,fst_y))

