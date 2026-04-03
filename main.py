from figure.circle import Circle
from figure.rect import Rect
import turtle
import random

def generate(n):
    lst = []
    for i in range(n):
        vs = random.choice(['0','1'])
        if vs=='1':
            r = Rect(random.randint(-100,100), random.randint(-100,100), random.randint(1,100), random.randint(1,200), 'red')
            lst.append(r)
        else:
            s = Circle(random.randint(-100,100), random.randint(-100,100), random.randint(1,100),'purple')
            lst.append(s)
    return lst

def render(d):
    for i in d:
        i.draw()


def main():
    n=random.randint(1,20)
    x = generate(n)
    render(x)

if __name__ == '__main__':
    main()

turtle.done()