print("a.") #a.

print("I.") #I.
for i in range(20):
    print(i,end=" ")

print("II.") #II.
k = int(input("Enter a number : "))
for i in range(k):
    print(i,end=" ")

print("b") #b.

print("I.") #I.
for i in range (10):
    print("1 0",end=" ")
print(" ")

print("II.") #II.
k = int(input("Enter the total number of 1's and 0's : "))
for i in range(k):
    if i%2 == 0:
        print("1", end=(" "))
    else:
        print("0", end=(" "))
print(" ")

print("c.") #c.

print("I.") #I.
for i in range (1,10):
    for k in range(1,10):
        print(i*k,"\t", end=" ")
    print(" ")

print("II.") #II.
n = int(input("Enter a number : "))
for i in range (1,n+1):
    for k in range(1,n+1):
        print(i*k,"\t", end=" ")
    print(" ")