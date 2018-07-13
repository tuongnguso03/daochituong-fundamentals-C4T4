x = int(input("x = "))
operation=input("Operation (+,-,*,/) : ")
y = int(input("y = "))
#input
if operation == "+":
    res = x+y
elif operation == "-":
    res= x - y
elif operation == "*":
    res= x*y
elif operation == "/":
    res= x/y 
#calculations
print("*"*20)
print("{0} {1} {2} = {3}".
    format(x,operation,y,res))       
print("*"*20)            
#output