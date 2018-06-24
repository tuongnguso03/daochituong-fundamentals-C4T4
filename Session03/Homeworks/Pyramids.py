Số_Hàng_Và_Cột = int(input("Enter the number of columns and rows : "))
#a.
for i in range (1,Số_Hàng_Và_Cột+1) :
    print("* "*i)
print(" ")    
#b
for i in range (1,Số_Hàng_Và_Cột+1) :
    print("  "*(Số_Hàng_Và_Cột-i)+"* "*i)  
print(" ")     
#c
for i in range (1,Số_Hàng_Và_Cột+1) :
    if i !=1 and i != Số_Hàng_Và_Cột:
        print("  "*(Số_Hàng_Và_Cột-i)+"* ") 
    else:
        print("* "*Số_Hàng_Và_Cột)   