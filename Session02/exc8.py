hang=int(input("So hang ?"))
cot=int(input("So cot ?"))

for i in range (hang):
    for k in range (cot):
        if (i+k)%2 == 0:
            print("*", end=" ")
        else: 
            print("0", end=" ")
    print(" ")


