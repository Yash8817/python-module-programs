from turtle import *
bgcolor('black')
speed(30)
hideturtle()
for i in range(150):
    color('red')
    circle(i)
    color('yellow')
    circle(i * 0.8)
    right(10)
    forward(5)
done()
