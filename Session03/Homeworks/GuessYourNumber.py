top=101
bot=0
jung=50
playing=True
_=input('''Guess your number game.
Now think of a number from 1 to 100, then press Enter.
''')
print('''All you have to do is to answer my questions.
"c" if my answer is correct.
"s" if my anwer is "s"maller than your number.
"l" if my guess is "l"arger than your number. 
''')
while playing:
    ans = input("Is {0} your number ? ".format(jung))
    if ans == "l":
        top=jung
        jung = (top+bot)//2
    elif ans == "s":
        bot=jung
        jung = (top+bot)//2
    else:
        print("I knew it !")
        playing=False
