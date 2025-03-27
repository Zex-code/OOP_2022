import turtle
from random import *

turtle.shape('classic')
turtle.speed(0)

for x in range(1000):
    a = randint(-360, 360)
    turtle.right(a)
    turtle.forward(10)

turtle.mainloop()
