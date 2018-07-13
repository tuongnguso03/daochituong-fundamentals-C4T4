while True:
    num = int(input("Enter a Number : "))

    if num <= 0:
        print("Too small.")
    else:
        sum=0
        for i in range(1,num):
            if (num % i) == 0:
                sum+=i
        if sum==num:
            print("{0} is a perfect number.".format(num))
        else:
            print("{0} is not a perfect number.".format(num))      
    print(""">>> =====================================================
    >>> """)             