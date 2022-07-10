import turtle

t=turtle.Turtle()
t.speed(0)
sc=turtle.Screen()
sc.bgcolor("black")
clrlist=['red',
        'purple',
        'blue',
        'green',
        'yellow',
        'purple']

for i in range(220):
    t.color(clrlist[i%6])
    t.pen(i/100+1)
    t.forward(i)
    t.left(59)
turtle.mainloop()