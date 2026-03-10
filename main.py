import random
import fun.square as square
import turtle

n = int(input('Количество внутренних прямоугольников: '))
colors = ["red", "blue", "green", "orange", "purple", "pink", "brown", "gray"]

def main():
    x = random.randrange(0, 200)
    y = random.randrange(0, 200)
    h = random.randrange(20, 200)
    w = random.randrange(20, 200)
    color1 = random.choice(colors)
    square.square(x, y, h, w, color1)
    for i in range(n):
        color2 = random.choice(colors)
        x_i = x + i * (w / n)
        y_i = y
        # Рисуем
        square.square(x_i, y_i, h, w/n, color2)

    turtle.done()

if __name__ == "__main__":
    main()