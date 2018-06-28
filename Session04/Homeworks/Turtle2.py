from turtle import *
color("blue")
speed(0)
for i in range (36):
    for k in range (4):
        forward(5+5*i)
        left(90)
    left(360/24)

mainloop()    