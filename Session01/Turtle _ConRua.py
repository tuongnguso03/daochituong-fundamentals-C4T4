from turtle import *
speed(-1)
shape("triangle")

color("blue")
left(45)

for i in  range(360): 
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    right(359)


mainloop()