dict_t = {
    "hc":"học",
    "ys":"Đấng Sáng Thế",
    "ls":"Thầy Tu Mù",
    "xz":"Thần Thông",
    "stt":"Số thứ tự" ,   
}

working=True
while working:
    for key in dict_t.keys():
        print(key, end ="\t")
    print()

    k1=input("Your code: ")
    if k1 in dict_t:
        print("*"*20)
        print("Code : ",k1)
        print("Meaning : ",dict_t[k1])
        print("*"*20)
    else:
        
        asking=True
        while asking:
            print("*"*20)
            con=input("Would you like to contribute this word (Y/N) ? :").upper()
            if con == "Y" :
                dict_t[k1]=input("Meaning ?: ")
                print("Updated")
                print("*"*20)
                asking=False
            elif con == "N":
                #end
                print("*"*20)
                asking=False
                working=False
  
                    