#food1="pizza"
#food2="mì"
#food3="hamburger"
#food4="cơm"
#food5="xôi"

menu=["pizza","mì","hamburger","cơm","xôi gà"]

#menu[0] = "Thịt chó"

#print(menu) #in tập này ra
#print(*menu) #in các phần tử ra

#print(len(menu)) #in số pt
#seperator 
#print(*menu, sep=", ") #tách cách phần tủ

menu.append("trà sữa") #thêm 1 thằng vaò cuối
#print(*menu, sep=", ") #in lại ra

#print(len(menu)) #in số phần tử 

#fud=menu[4] #Truy xuất thằng số 5 của phần tử (Python đếm từ số 0)
#print(fud)

#for i in range (len(menu)):
#    print(menu[i])

#for index, item in enumerate(menu):
#    print(index,item)

#for fud in menu:
#    print(fud)    

menu.pop(1) #
print(menu)
del menu[3] #
print(menu)
menu.remove("trà sữa") #Xoá 
print(menu)