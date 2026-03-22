import turtle
import fun.square as sq
import fun.circle as sr

def generate(cmd, n, fig_list):

    if cmd == 'r':
        for i in range(1, n + 1):
            print(f"Прямоугольник {i}")
            x = int(input('x: '))
            y = int(input('y: '))
            h = int(input('h: '))
            w = int(input('w: '))
            color = input('цвет: ')
            fig_list.append(['rect', x, y, h, w, color])
    elif cmd == 's':
        for i in range(1, n + 1):
            print(f"Круг {i}")
            x = int(input('x: '))
            y = int(input('y: '))
            r = int(input('r: '))
            color = input('цвет: ')
            fig_list.append(['circle', x, y, r, color])


def render(data):
    for shape in data:
        if shape[0] == 'rect':
            sq.square(shape[1], shape[2], shape[3], shape[4], shape[5])
        elif shape[0] == 'circle':
            sr.draw_circles(shape[1], shape[2], shape[3], shape[4])
    turtle.done()

def main():
    all_figures = []
    while True:
        cmd = input('Что добавить? (r - прямоугольник, s - круг, exit - нарисовать всё и выйти): ')
        if cmd == 'exit':
            break
        elif cmd in ('r', 's'):
            n = int(input('Сколько фигур этого типа? '))
            generate(cmd, n, all_figures)
        else:
            print("Неизвестная команда, попробуйте r, s или exit")
    render(all_figures)

if __name__ == "__main__":
    main()