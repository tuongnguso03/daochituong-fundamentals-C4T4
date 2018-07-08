from turtle import *
color("blue")

for i in range (24):
    for k in range (4):
        forward(100)
        left(90)
    left(360/24)

mainloop()         