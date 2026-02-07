def medium(x,y,h,w):
    center_x = int(x+w/2)
    center_y = int(y+h/2)
    return center_x, center_y
def second_square(x,y,h,w):
    x2 = x - w/2
    y2 = y - h/2
    return x2,y2