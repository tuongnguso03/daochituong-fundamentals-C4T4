from random import choice
words=["upper","lower","left","right","range","print","random"]
hint={
    "upper":"Situated above another part",
    "lower":"Situated under another part",
    "left":"On, towards, or relating to the side of a human body or of a thing that is to the west when the person or thing is facing north."
    "right":3,
    "range":4,
    "print":5,
    "random":6
}
total=len(words)
playing=True

while playing == True:
    word=choice(words)
    words.remove(word)
    print("Chars : ",end="")
    chars=list(word)
    for i in range(len(chars)):
        rand_char=choice(chars)
        print (rand_char,end= " ")
        chars.remove(rand_char)
    print()
    
    tries=0
    guessing=True
    while guessing:
        ans=input("Word : ") 
        if ans == word:
            print("Hurray")
            guessing=False
            tries += 1
        else:
            print(":(")
            tries += 1
            if tries==5:
                print("Hint : {0}".format(hint[word]))

    if len(words) == 0:
        print("You Win")
        playing=False      













