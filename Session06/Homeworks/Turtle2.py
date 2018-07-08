from turtle import *
speed(0)
for i in range(4,10):
    for k in range (i):
        if (k+i)%2==1:
        
            color("red")
        else:
            color("blue")
        left(-360/i)
        forward(-100)
        
mainloop()        