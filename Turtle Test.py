# https://docs.python.org/3/library/turtle.html
import turtle
import random
"""
turtle.begin_fill()
turtle.speed(100000000000000000000000000000000000000000000000000000000)
while True:
    turtle.forward(random.randint(0,10))
    turtle.right(random.randint(-90,90))
"""
"""
turtle.forward(100)
turtle.right(15)
turtle.forward(100)
turtle.left(30)
turtle.forward(100)
turtle.left(180)
turtle.forward(200)
turtle.right(15)
turtle.forward(20)
"""

# stuff from online 
turtle.color('blue', 'yellow')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
turtle.done()


"""
ideas
-kids make there own shapes
-use random module
-use easy kattikus problems - make it fun
- elementry DO NOT DO PYTHON
-
"""
