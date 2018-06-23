k = 1
n = int(input('Enter the number "n" : '))
if n < 0:
    print ('"n" is a negative number')
else:
    for i in range(1, n+1):
        k = k*i
    print("The factorial of ",n," is ",k)
        