from random import randint
moodpoint = randint(0,100)
print("Hello I'm Mr. Moody")
if moodpoint < 30:
    print("I feel sad")
elif moodpoint < 60:
    print("I feel OK")
else:
    print("Oh Yeah")    