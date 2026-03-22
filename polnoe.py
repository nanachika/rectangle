import turtle
import fun.square as sq
import fun.circle as sr

def generate(cmd, n):
    fig = []
    if cmd == 'r':
        for i in range(1, n + 1):
            x = int(input(f'x {i}: '))
            y = int(input(f'y {i}: '))
            h = int(input(f'h {i}: '))
            w = int(input(f'w {i}: '))
            color = input('цвет: ')
            rect = ['rect', x, y, h, w, color]
            fig.append(rect)
    elif cmd == 's':
        for i in range(1, n + 1):
            x = int(input(f'x {i}: '))
            y = int(input(f'y {i}: '))
            r = int(input(f'r {i}: '))
            color = input('цвет: ')
            circle = ['circle', x, y, r, color]
            fig.append(circle)
    return fig

def render(data):
    for shape in data:
        if shape[0] == 'rect':
            sq.square(shape[1], shape[2], shape[3], shape[4], shape[5])
        elif shape[0] == 'circle':
            sr.draw_circles(shape[1], shape[2], shape[3], shape[4])
    turtle.done()

def main():
    while True:
        cmd = input('Что хотите нарисовать (r - прямоугольник, s - круг, exit - выход): ')
        if cmd == 'exit':
            break
        elif cmd == 'r':
            n = int(input('Количество прямоугольников: '))
            x = generate(cmd, n)
            render(x)
        elif cmd == 's':
            n = int(input('Количество кругов: '))
            x = generate(cmd, n)
            render(x)


if __name__ == "__main__":
    main()