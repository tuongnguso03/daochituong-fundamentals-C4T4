Fvrt=["this","that","those"]

print("Hi there, heres your favorite things so far :")
print("*"*20)
#print(*Fvrt, sep = ", ")
for num,name in enumerate(Fvrt):
    #print(str(num+1)+", "+name)
    print(num+1,name,sep=". ")
print("*"*20)

newfvrt = input ("Name one thing you want to add ? ") #input the thing
Fvrt.append(newfvrt) #add the thing to the líst

#print(*Fvrt,sep = ", ")
for num,name in enumerate(Fvrt):
    print(num+1,", ",name)