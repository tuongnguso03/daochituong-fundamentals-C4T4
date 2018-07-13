from random import randint, choice
import Evaluate

playing=True
points=0 #StartWithALowerLetter

while playing:
    x = randint(1,10)
    operation = choice(["+","-","*","/"])
    y = randint(1,10)
    error=choice([-2,-1,0,0,0,0,1,2])

    res=Evaluate.EVA_01(x,y,operation)

    display=res+error

    print("{0} {1} {2} = {3}".format(x,operation,y,display))   
    ans=input("(Y/N)? ").upper()

    if error == 0:
        trueans = "Y"
    else: trueans = "N"

    if ans == trueans:
        print("Yup.")
        points += 1
    else:
        print("Nope.")   
        playing=False
print("Your score : {0}".format(points))         

