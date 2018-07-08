print("""Guess your number game.
Just imagine a number from 1 to 100 then press enter.""")
input()
print("""All you have to do is to answer to my guess
"c" if my answer is "C"orect.
"l" if my guess is "L"arger than your number
"s" if my guess is "S"maller than your number

... """)




from random import randint

top=100
bot=1

mid = randint(bot,top)
pl=True
Ans="a"
while pl:
    
    mid = randint(bot,top)
    Ans=input("Is {0} your number ?". format(mid)).lower()
    
    if Ans == "l" :
        top=mid-1
    elif Ans == "s":
        bot=mid+1
    elif Ans == "c":
        print("I knew it !")
        pl=False
    else:
        pl=False    

