import turtle
turtle.bgcolor('purple')

turtle.shape("circle")
finn=turtle.clone()
finn.color('yellow')
finn.goto(0,150)
finn.goto(-75,150)
finn.color('white')
finn.goto(-75,0)
jj=turtle.clone()
jj.shape('arrow')
jj.pensize(10)
jj.color('green')
jj.goto(0,-150)
jj.goto(75,-150)
jj.color('blue')
jj.goto(75,0)
turtle.mainloop()
def up() :
    turtle.goto(x,y+10)
    onkey
