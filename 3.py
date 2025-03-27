from turtle import *
import turtle

shape('turtle')

inp = open('input.txt', 'r')
line = inp.readline().strip()
s = line.split()

num3 = [(int(s[i]), int(s[i+1])) for i in range(0, 7, 2)]
num9 = [(int(s[i]), int(s[i+1])) for i in range(8, 21, 2)]
num4 = [(int(s[i]), int(s[i+1])) for i in range(22, 31, 2)]
num0 = [(int(s[i]), int(s[i+1])) for i in range(32, 39, 2)]

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
pendown()

turtle.mainloop()
