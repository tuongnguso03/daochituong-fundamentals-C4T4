from random import randint

numbers1=[]

numbers=[]
for i in    range (randint(1,100)):
    numbers.append(randint(-100,100))

while len(numbers)>0:
    numbers1.append(min(numbers))
    numbers.remove(min(numbers))
print(*numbers1,sep=", ")    