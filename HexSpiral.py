import turtle
colors = ['violet','indigo','blue','green','yellow','orange','red']

t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%7])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)