print("Welcome to Hextech Ultimate... uh... something.")
usrnm = input ("Username : ")
psswrd = input ("Password : ")
print("Register Complete")
usrnm2 = input ("Username : ")
if usrnm2 == usrnm:
    psswrd2 = input("Password : ")
    if psswrd2 == psswrd:
        print("Welcome, ",usrnm)
    else:
        print("Password incorrect.")
else:
    print("Username incorrect")        
