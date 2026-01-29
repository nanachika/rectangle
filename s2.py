import random
import turtle
colors = ["red", "blue", "green", "orange", "purple", "pink", "brown", "gray"]
def square(x,y,h,w,colors):
    turtle.color(colors)
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    for i in range(2):
        turtle.fd(w)
        turtle.rt(90)
        turtle.fd(h)
        turtle.rt(90)
def main():
    for i in range(10):
        x = random.randrange(0, 200)
        y = random.randrange(0, 200)
        h = random.randrange(0, 200)
        w = random.randrange(0, 200)
        color = random.choice(colors)
        square(x, y, h, w, color)
        print(f"x={x}, y={y}, h={h}, w={w}, цвет={color}")
turtle.mainloop()
