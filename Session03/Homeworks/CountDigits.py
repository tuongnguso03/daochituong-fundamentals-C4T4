num = int(input("Enter a Number : "))
digits = 0
while (10**digits < num < 10**(digits+1)) == False:
    digits = digits + 1
print(num," has ",digits+1," digits.")    

