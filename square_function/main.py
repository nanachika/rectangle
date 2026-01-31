import random
import square
colors = ["red", "blue", "green", "orange", "purple", "pink", "brown", "gray"]
def main():
    for i in range(10):
        x = random.randrange(0, 200)
        y = random.randrange(0, 200)
        h = random.randrange(0, 200)
        w = random.randrange(0, 200)
        color = random.choice(colors)
        square.square(x, y, h, w, color)
        print(f"x={x}, y={y}, h={h}, w={w}, цвет={color}")
if __name__ == "__main__":
    main()