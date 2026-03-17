# Noah Raja
# 3/17/2026
# P4LAB1
# Creating Shapes with Turtle

import turtle
win = turtle.Screen()
win.bgcolor("CadetBlue1")
t = turtle.Turtle()

counts = 0
for side in range(5):
    t.forward(50)
    t.left(90)
t.forward(50)

counts = counts + 1


t.begin_fill()
t.fillcolor("green")

while counts == 1:
    t.left(40)
    t.forward(40)
    t.left(100)
    t.forward(40)
    counts += 1


t.end_fill()

win.mainloop()
