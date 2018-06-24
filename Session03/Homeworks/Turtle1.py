from turtle import *
h=3
for i in ("red","blue","brown","yellow","gray"):
    
    for k in range(h):
        color(i)
        forward(100)
        left(360/h)
    h=h+1    

mainloop()