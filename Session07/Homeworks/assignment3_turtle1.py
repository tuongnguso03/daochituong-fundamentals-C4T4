from turtle import *
def draw_square(length,clrs):
    color(clrs)
    for i in range (4):
        forward(length)
        left(90)
speed(0)
#draw_square(100,"blue") 
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()       
