import turtle

def draw_circles(x, y, r,color):
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y-r)
    turtle.pendown()
    turtle.circle(r)

