from turtle import *
bgcolor('black')
color('cyan')
speed(200)
right(45)
for i in range(150):
    circle(30)
    if 8 < i < 60:
        left(5)
    if 80 < i < 133:
        right(5)
    if i < 80:
        forward(10)
    else:
        forward(5)
