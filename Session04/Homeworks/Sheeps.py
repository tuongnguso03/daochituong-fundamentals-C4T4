from random import randint
def RandomGenerator():
    numbers=[]
    
    for i in    range (randint(6,10)): #đẻ ngẫu nhiên
        numbers.append(randint(1,300))
    
    return numbers

def MonthPass(numbers):
    
    for i in range(len(numbers)):
        numbers[i]=numbers[i]+50
    
    return numbers    

def Sheer(numbers):
    
    numbers[numbers.index(max(numbers))]=8
    
    return numbers

def Sell(numbers):
    
    size=0
    
    for i in range(len(numbers)):
        size=size+numbers[i]
    
    money=size*2
    
    return (size,money)    
    


sheeps= RandomGenerator() #Đẻ cừu
print("Hello my name is Tuong and here are my sheeps :")
print(sheeps)

owns_sheep=True
Month=0
while owns_sheep:
    Month=Month+1
    print("MONTH ",Month)
    
    print("One month have passed and here are my sheeps :")
    sheeps=MonthPass(sheeps) #1 tháng trôi
    print(sheeps)
    
    thinking=True
    while thinking:
        do=input("Will I sheer one of them or will I sell them ?").lower()
        
        if do == "sheer":
            print("Now my biggest sheep has size {} lets sheer it. ".format(max(sheeps)))
            sheeps=Sheer(sheeps) #xỉa cừu
            
            print("After shearing here is my flock :")
            print(sheeps)
            thinking=False
        
        elif do == "sell":
            (a,b)=Sell(sheeps)
            print("My flock has size in total: ",a)
            
            print("I would get ",a," * 2$ = ",b,"$",sep="")  
            owns_sheep=False
            thinking=False
        
        else:
            print("Not a decision.")
