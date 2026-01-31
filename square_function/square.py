import turtle
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
 