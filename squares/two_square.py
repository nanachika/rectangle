import random
import square
import turtle
import medium
import cordinat_second_square
colors = ["red", "blue", "green", "orange", "purple", "pink", "brown", "gray"]
def main():
    x = random.randrange(0, 200)
    y = random.randrange(0, 200)
    h1= random.randrange(0, 200)
    h2 = random.randrange(10, h1)
    w1 = random.randrange(0, 200)
    w2 = random.randrange(10, w1)
    color1 = random.choice(colors)
    color2 = random.choice([c for c in colors if c != color1])  # другой цвет
    square.square(x, y, h1, w1, color1)
    cx, cy = medium.medium(x, y, h1, w1)
    x2,y2 = cordinat_second_square.second_square(cx,cy,h2,w2)
    square.square(x2, y2, h2, w2, color2)
    print(f"x={x}, y={y}, h={h1}, w={w1}, цвет={color1}")
    print(f"x={x2}, y={y2}, h={h2}, w={w2}, цвет={color2}")
    turtle.done()
if __name__ == "__main__":
    main()