items=["T-shirt","Sweater"]
commands=["C","R","U","D"]

Wrkng=True
while Wrkng: 
    Asking=True
    while Asking:
        
        command=input("Welcome to our shop, what do you want (C,R,U,D) ?: ").upper()
        if command in commands:
            Asking=False
        
        else:
            print("Please type in the right command.")

    if command == "C":
        
        c=input("Enter new item : ")
        items.append(c)
    
    elif command == "U":
        
        asking2=True
        while asking2:
            u_pos=int(input("Update position ? "))
            if u_pos>0 and u_pos<=len(items):
                asking2=False
            else:
                print("Invalid number.")  
        
        items[u_pos-1]=input("New item ?: ")    
    
    elif command == "D":
        
        asking2=True
        while asking2:
            d_pos=int(input("Delete position ? "))
            if d_pos>0 and d_pos<=len(items):
                asking2=False
            else:
                print("Invalid number.")        
        
        items.pop(d_pos-1)   

    print("Our items: ",end=" ")
    print(*items, sep=", ")
    rslt=input("Type anything + enter to continue, or press enter to end.")
    if rslt == "":
        Wrkng=False
    
print("Bye")