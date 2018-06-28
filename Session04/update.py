Fvrt=["this","that","those"]

print("Hi there, heres your favorite things so far :")

print("*"*20)
for num,name in enumerate(Fvrt):
    
    print(num+1,name,sep=". ")
print("*"*20)

pos=int(input("Position you want to update ? "))
Fvrt[pos-1]= input("Your replacing Favorite ? ")

print("*"*20)
for num,name in enumerate(Fvrt):
    
    print(num+1,name,sep=". ")
print("*"*20)