import random
import fun.square as square
import turtle

n = int(input('Количество внутренних прямоугольников: '))
colors = ["red", "blue", "green", "orange", "purple", "pink", "brown", "gray"]

def main():
    # Первый (самый внешний) прямоугольник
    x = random.randrange(0, 200)
    y = random.randrange(0, 200)
    h1 = random.randrange(20, 200)
    w1 = random.randrange(20, 200)
    color1 = random.choice(colors)
    square.square(x, y, h1, w1, color1)

    # Размеры первого внутреннего
    h2 = random.randrange(10, h1)
    w2 = random.randrange(10, w1)
    # Цвет для внутренних
    color2 = random.choice([c for c in colors if c != color1])

    for i in range(n):
        # Координаты для текущего внутреннего (относительно текущего внешнего)
        x2 = x + (w1 - w2) / 2
        y2 = y + (h1 - h2) / 2
        # Рисуем
        square.square(x2, y2, h2, w2, color2)

        # Этот прямоугольник становится внешним для следующего
        x, y = x2, y2
        h1, w1 = h2, w2

        # Уменьшаем размеры для следующего внутреннего
        h2 = h2 * (1 - random.randrange(10, 20) / 100)
        w2 = w2 * (1 - random.randrange(10, 20) / 100)

    turtle.done()

if __name__ == "__main__":
    main()