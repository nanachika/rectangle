from figure.cirl_fig import Circle
from figure.rect import Rect
import random
import pygame as pg

def main():
    # 1. Обязательно "включаем" модули Pygame перед работой
    pg.init() 

    def generate(n):
        lst = []
        # parent = Rect(100, 100, 300, 200, 'red')
        # child = Rect(150, 150, 50, 50, 'blue')
        # parent.add(child)
        # lst.append(parent)
        for i in range(n):
            vs = random.choice(['0','1'])
            if vs=='1':
                r1 = Rect(random.randint(0,800), random.randint(0,600), random.randint(1,200), random.randint(1,100), 'red')
                r2_w = random.randint(1, r1.w)
                r2_h = random.randint(1, r1.h)
                r2 = Rect(random.randint(r1.x, r1.x + r1.w - r2_w), random.randint(r1.y, r1.y + r1.h - r2_h), r2_w, r2_h, 'pink')                
                lst.append(r1)
                r1.add(r2)

            else:
                s = Circle(random.randint(0,800), random.randint(0,600), random.randint(1,100),'purple')
                lst.append(s)
        return lst

    def render(lst, screen):
        for i in lst:
            i.draw(screen)

    screen = pg.display.set_mode((800, 600))
    # Зададим красивое имя нашему окошку
    pg.display.set_caption("Наше первое окно на Pygame") 
    
    n = random.randint(1, 20)
    x = generate(n)
    FPS = 60
    clock = pg.time.Clock()
    running = True
    while running:

        screen.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                coordinates = event.pos
                px,py = coordinates
                for fig in x:
                    found = False
                    if fig.child:
                        for f in fig.child:
                            if f.inside(px - f.parent.x, py - f.parent.y):
                                found = True
                                gx = random.randint(0,f.parent.w-f.w)
                                gy = random.randint(0,f.parent.h-f.h)
                                f.color = random.choice(['green','pink','blue','orange'])
                                f.run(gx,gy)
                                continue
                    if not found:
                        if fig.inside(px, py):
                            gx = random.randint(0,800)
                            gy = random.randint(0,600)
                            fig.color = random.choice(['green','pink','blue','orange'])
                            fig.run(gx,gy)
                        

                    
        # Твоя отличная отрисовка элементов

        render(x, screen)
        pg.display.flip()
        clock.tick(FPS)
    # 2. Освобождаем память и красиво закрываем окно после выхода из цикла
    pg.quit() 

if __name__ == '__main__':
    main()