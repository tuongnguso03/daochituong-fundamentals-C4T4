from turtle import *
speed(-1)
color("red")

for i in range (1,18):
    for k in range (4):
        forward(6*i)
        left(90)
    left(12)
    forward(20)

mainloop()   