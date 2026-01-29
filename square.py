import random
import turtle
colors = ["red", "blue", "green", "orange", "purple", "pink", "brown", "gray"]
def square(x,y,h,w,colors):
    turtle.color(colors)
    fst_x = x
    fst_y = y
    snd_x = x + w
    snd_y = y
    tsd_x = x + w
    tsd_y = y + h
    fsh_x = x
    fsh_y = y + h
    turtle.up()
    turtle.goto(fst_x, fst_y)
    turtle.down()
    turtle.goto(snd_x, snd_y)
    turtle.goto(tsd_x, tsd_y)
    turtle.goto(fsh_x, fsh_y)
    turtle.goto(fst_x, fst_y)  
def main():
    for i in range(10):
        x = random.randrange(0, 200)
        y = random.randrange(0, 200)
        h = random.randrange(0, 200)
        w = random.randrange(0, 200)
        color = random.choice(colors)
        square(x, y, h, w, color)
        print(f"x={x}, y={y}, h={h}, w={w}, цвет={color}")
