from turtle import *
color("red")

left(30)
for i in range (4):
    for k in range (2):
        for l in (1,2):
            forward(100)
            right(l*60)
    left(90)

mainloop()