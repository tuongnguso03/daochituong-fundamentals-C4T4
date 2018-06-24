num = int(input("Enter a Number : "))

if num < 0:
    print("Too small.")
elif num < 2:
    print(num," is a square number but not a prime number.")

else:
    
    #Sqare test:
    if float(int(num**0.5)) == num**0.5:
        print(num," is a square number.")
    else:
        print(num," is not a square number.")   
    
    #Prime test
    for i in range(2,int(num**0.5)+1):
        if (num % i) == 0:
           print(num, "is not a prime number")
           break
        elif i == int(num**0.5):
            print(num, "is a prime number")   
        
