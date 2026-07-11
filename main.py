from figure.cirl_fig import Circle
from figure.rect import Rect
import random
import pygame as pg

def main():
    # 1. Обязательно "включаем" модули Pygame перед работой
    pg.init() 

    def generate(n):
        lst = []
        for i in range(n):
            vs = random.choice(['0','1'])
            if vs=='1':
                r = Rect(random.randint(0,800), random.randint(0,600), random.randint(1,100), random.randint(1,200), 'red')
                lst.append(r)
            else:
                s = Circle(random.randint(0,800), random.randint(0,600), random.randint(1,100),'purple')
                lst.append(s)
        return lst

    def render(d, screen):
        for i in d:
            i.draw(screen)

    screen = pg.display.set_mode((800, 600))
    # Зададим красивое имя нашему окошку
    pg.display.set_caption("Наше первое окно на Pygame") 
    
    n = random.randint(1, 20)
    x = generate(n)
    
    flag_w = True
    while flag_w:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                flag_w = False
                
        # Твоя отличная отрисовка элементов
        render(x, screen)
        pg.display.flip()

    # 2. Освобождаем память и красиво закрываем окно после выхода из цикла
    pg.quit() 

if __name__ == '__main__':
    main()