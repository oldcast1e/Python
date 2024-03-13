import turtle as t
colors = ['red','orange','yellow','green']
def dr(c):
    t.color(colors[c])
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()
h = 0
for i in range(4):
    t.setheading(90*i)
    dr(i)