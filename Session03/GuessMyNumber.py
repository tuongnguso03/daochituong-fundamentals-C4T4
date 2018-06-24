from random import randint
num = randint(0,100)
count =1
playing = True
while playing:
    num1 = int(input("Guess my number (0-100) : "))
    if num1 > num:
        print("Too large")
    elif num1 < num:
        print("Too small")
    else:
        print("Yeah, that's right")
        playing = False
    
    count = count +1
    if count == 7:
        print("You lose")
        playing = False         