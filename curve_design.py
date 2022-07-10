import turtle
from math import cos, sin
from time import sleep
import random
import time

window = turtle.Screen()
window.bgcolor("black")

myPen = turtle.Turtle()
myPen.shape('circle')
myPen.shapesize(2)
window.tracer(0)
myPen.speed(0)
myPen.pensize(3)
myPen.color("lime")
myPen.penup()
A = 690
B = 320
t = 0
a,b,c,d,e,f = 80,80,1,80,1,2
myPen.fillcolor('gold2')
myPen.begin_fill()
for i in range (0,6300):
    t += 0.001
    x = sin(a*t) * (cos(b*t)*sin(e*t)**1)
    y = cos(c*t) - (cos(d*t)*sin(f*t)**1)
    myPen.goto(A*x,B*y)
    myPen.pendown()
    myPen.getscreen().update()
myPen.end_fill()
myPen.ht()
turtle.done()
time.sleep()