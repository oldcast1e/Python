import turtle as t
import time


def dr(i):
    t.color(col[i])
    t.begin_fill()
    for i in range(3):   
        t.forward(100)
        t.left(120)
    t.end_fill()

col = ['red','yellow','orange','green']   
for i in range(4):   
    dr(i)
    t.penup()
    t.forward(100)
    t.pendown()
    time.sleep(3)
