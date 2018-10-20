from turtle import *
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
hideturtle()
bgcolor("black")
for x in range(5000000):
    pencolor(colors[x % 3])
    width(1)
    setpos(0-x, 0-x)
    setpos(0+x, 0-x)
    setpos(0+x, 0+x)
    setpos(0-x, 0+x)
    setpos(0-x, 0-x)
