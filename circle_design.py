import turtle

t=turtle.Screen()             
t.bgcolor("black")          
                                        
ball=turtle.Turtle()
ball.speed(100)
ball.color("cyan")

for i in range(200):
    ball.circle(317)
    ball.left(6)           
    ball.fd(6)                     
    ball.right(1)
    
t.mainloop()   
