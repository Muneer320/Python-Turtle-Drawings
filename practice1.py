from turtle import *

speed(10)
while True:
    circle(80)
    forward(50)
    # right(40)
    left(20)
    if abs(pos()) < 1:
        break
