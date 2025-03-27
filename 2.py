from turtle import *
import turtle

speed(0)
shape('turtle')

num3 = [(50, 0), (0,-50), (50,-50), (0,-100)]
num9 = [(50,0), (50,-50,), (0,-50), (0,0), (0,-50), (50,-50), (0,-100)]
num4 = [(0,-50), (50,-50), (50,0), (50,-50), (50,-100)]
num0 = [(0,-100), (50,-100), (50,0), (0,0)]

for i in num3:
    goto(i[0], i[1])
penup()
goto(60, 0)
pendown()

for i in num9:
    goto(i[0]+60, i[1])
penup()
goto(120, 0)
pendown()

for i in num4:
    goto(i[0]+120, i[1])
penup()
goto(180, 0)
pendown()

for i in num0:
    goto(i[0]+180, i[1])
penup()
goto(240, 0)
pendown()

for i in num9:
    goto(i[0]+240, i[1])
penup()
goto(300, 0)
pendown()

for i in num3:
    goto(i[0]+300, i[1])
penup()
goto(360, 0)
pendown()

turtle.mainloop()
