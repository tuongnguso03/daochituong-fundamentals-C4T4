num = int(input("Enter a Number : "))

#a
s=0
for i in range (1,num+1):
    s=s+1/i
print("a. S = ",s)

#b
s=0
for i in range (1, num+1):
    p=1
    for k in range(1,i+1):
        p=p*k    
    s=s+1/p 
   
print("b. S = ",s)            
