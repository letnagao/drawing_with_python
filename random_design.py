import colorsys
from turtle import pencolor


import turtle as t
import colorsys

t.tracer(5)
t.pensize(2)
h=0.5
t.bgcolor("black")

for i in range(300):
    c=colorsys.hsv_to_rgb(h,1,1)
    h += 0.004
    t.pencolor(c)
    t.fd(i)
    t.rt(120)
    t.fd(i)
    t.rt(30)
    t.fd(i)
    t.rt(360)
    t.fd(i)
    t.rt(120)

t.done()